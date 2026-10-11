"""No GPU, network, or Unsloth installation is used in these behavior checks."""
import copy
import json
import unittest
from practice.rag_gate_demo import CANDIDATES, QUERY, mock_judge, run_pipeline


class RagGateTests(unittest.TestCase):
    def test_complete_evidence_is_ready_but_does_not_generate(self):
        result = run_pipeline(QUERY, CANDIDATES, mock_judge)
        self.assertEqual(result["decision"], "ready_for_generation")
        self.assertEqual(result["kept_ids"], ["C1", "C3"])
        self.assertFalse(result["generation_called"])

    def test_second_judgment_sees_only_retained_evidence(self):
        calls = []
        def recording_judge(payload):
            calls.append(copy.deepcopy(payload))
            return mock_judge(payload)
        run_pipeline(QUERY, CANDIDATES, recording_judge)
        self.assertEqual(len(calls), 2)
        second_ids = [c["id"] for c in json.loads(calls[1]["state"])["passages"]]
        self.assertEqual(second_ids, ["C1", "C3"])

    def test_high_relevance_does_not_replace_answerability(self):
        partial = [c for c in CANDIDATES if c["id"] != "C3"]
        result = run_pipeline(QUERY, partial, mock_judge)
        self.assertEqual(result["kept_ids"], ["C1"])
        self.assertEqual(result["reason"], "insufficient_evidence")
        self.assertEqual(result["context_for_generator"], [])

    def test_stricter_relevance_filter_can_remove_needed_evidence(self):
        result = run_pipeline(QUERY, CANDIDATES, mock_judge, relevance_threshold=0.90)
        self.assertEqual(result["reason"], "insufficient_evidence")

    def test_no_candidates_skips_model_calls(self):
        def never_called(_):
            self.fail("The model must not be called for empty retrieval.")
        self.assertEqual(run_pipeline(QUERY, [], never_called)["reason"], "no_candidates")

    def test_no_passing_candidates_skips_second_call(self):
        calls = []
        def recording_judge(payload):
            calls.append(payload)
            return mock_judge(payload)
        result = run_pipeline(QUERY, CANDIDATES, recording_judge, relevance_threshold=0.99)
        self.assertEqual(result["reason"], "no_relevant_passages")
        self.assertEqual(len(calls), 1)

    def test_malformed_scores_fail_instead_of_becoming_abstentions(self):
        for value in (True, "0.9", -0.1, 1.1, float("nan"), None):
            with self.subTest(value=value):
                def bad_judge(payload):
                    result = mock_judge(payload)
                    result["answers"]["C1"]["noul"] = value
                    return result
                with self.assertRaises(ValueError):
                    run_pipeline(QUERY, CANDIDATES, bad_judge)

    def test_missing_answer_fails(self):
        with self.assertRaises(ValueError):
            run_pipeline(QUERY, CANDIDATES, lambda _: {"answers": {}})


if __name__ == "__main__":
    unittest.main()
