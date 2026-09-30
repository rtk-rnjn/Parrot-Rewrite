import unittest

from bot.math.detector import looks_like_math


class DetectorTests(unittest.TestCase):
    def test_accepts_basic_math(self) -> None:
        for text in ("25 + 5", "2 * (10 + 3)", "x^2 + 1", "sqrt(16)", "x = 10", "(2 + 3) * 4"):
            with self.subTest(text=text):
                self.assertTrue(looks_like_math(text))

    def test_rejects_conversation(self) -> None:
        for text in ("hello", "what are you doing?", "I ate 25 apples", "this is a test", "25 apples"):
            with self.subTest(text=text):
                self.assertFalse(looks_like_math(text))

    def test_rejects_unknown_function_calls(self) -> None:
        self.assertFalse(looks_like_math("system(1)"))


if __name__ == "__main__":
    unittest.main()
