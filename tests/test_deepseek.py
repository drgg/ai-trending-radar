import os
import sys
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from summarize import AuthError, Summarizer, PROMPT_VERSION

SCHEMA = {"type": "object", "properties": {"ok": {"type": "boolean"}},
          "required": ["ok"], "additionalProperties": False}


def response(status=200, content='{"ok":true}', finish="stop"):
    return Mock(status_code=status, ok=status == 200,
                json=Mock(return_value={"choices": [{"finish_reason": finish, "message": {"content": content}}],
                                        "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}}))


class DeepSeekTests(unittest.TestCase):
    def setUp(self):
        self.summ = Summarizer({"backend": "deepseek", "model": "deepseek-flash", "refresh_after_days": 30})
        self.env = patch.dict(os.environ, {"DEEPSEEK_API_KEY": "test-only"})
        self.env.start()
        self.addCleanup(self.env.stop)

    @patch("summarize.requests.post")
    def test_json_and_usage(self, post):
        post.return_value = response()
        self.assertEqual(self.summ._ask("system", "user", SCHEMA), {"ok": True})
        payload = post.call_args.kwargs["json"]
        self.assertEqual(payload["response_format"], {"type": "json_object"})
        self.assertEqual(self.summ.usage["total_tokens"], 15)

    @patch("summarize.requests.post")
    def test_auth_and_balance_stop_without_retry(self, post):
        for status in (401, 402, 403):
            with self.subTest(status=status):
                post.reset_mock()
                post.return_value = response(status)
                with self.assertRaises(AuthError):
                    self.summ._ask("system", "user", SCHEMA)
                self.assertEqual(post.call_count, 1)

    @patch("summarize.time.sleep")
    @patch("summarize.requests.post")
    def test_invalid_schema_blank_and_truncated_are_not_accepted(self, post, sleep):
        post.side_effect = [response(content='{"ok":"wrong"}'), response(content="   "), response(finish="length")]
        with self.assertRaises(RuntimeError):
            self.summ._ask("system", "user", SCHEMA)
        self.assertEqual(post.call_count, 3)

    @patch("summarize.time.sleep")
    @patch("summarize.requests.post")
    def test_transient_error_retries(self, post, sleep):
        post.side_effect = [response(429), response(503), response()]
        self.assertEqual(self.summ._ask("system", "user", SCHEMA), {"ok": True})
        self.assertEqual(post.call_count, 3)

    def test_model_change_refreshes_unchanged_readme(self):
        cached = {"model": "claude-sonnet-5", "readme_sha": "same", "prompt_version": PROMPT_VERSION}
        self.assertTrue(self.summ._stale(cached, {"readme_sha": "same"}, date.today()))
        cached["model"] = "deepseek-flash"
        self.assertFalse(self.summ._stale(cached, {"readme_sha": "same"}, date.today()))


if __name__ == "__main__":
    unittest.main()
