import unittest

import sympy

from bot.math.evaluator import EvaluationError, evaluate_input
from bot.math.parser import Assignment, Expression, MathParseError, parse_input
from bot.math.session import InMemoryVariableStore


class MathTests(unittest.TestCase):
    def setUp(self) -> None:
        self.store = InMemoryVariableStore()

    def test_parsing(self) -> None:
        parsed = parse_input("2x + 3(x + 1)", self.store, 1)
        self.assertIsInstance(parsed, Expression)
        self.assertEqual(parsed.value, 5 * sympy.Symbol("x") + 3)

    def test_evaluation(self) -> None:
        self.assertEqual(evaluate_input("25 + 5", self.store, 1), "30")
        self.assertEqual(evaluate_input("sqrt(25)", self.store, 1), "5")
        self.assertEqual(evaluate_input("sin(pi / 2)", self.store, 1), "1")

    def test_assignment_and_lookup(self) -> None:
        self.assertEqual(evaluate_input("x = 5", self.store, 1), "x = 5")
        self.assertEqual(evaluate_input("x + 10", self.store, 1), "15")

    def test_variables_are_isolated(self) -> None:
        evaluate_input("x = 10", self.store, 1)
        self.assertEqual(evaluate_input("x + 2", self.store, 1), "12")
        self.assertEqual(evaluate_input("x + 2", self.store, 2), "x + 2")

    def test_undefined_variables_remain_symbolic(self) -> None:
        self.assertEqual(evaluate_input("x + 2", self.store, 1), "x + 2")

    def test_division_by_zero(self) -> None:
        self.assertEqual(evaluate_input("1 / 0", self.store, 1), "zoo")

    def test_malformed_expression(self) -> None:
        for text in ("2 +", "x =", "sqrt("):
            with self.subTest(text=text):
                with self.assertRaises(EvaluationError):
                    evaluate_input(text, self.store, 1)

    def test_invalid_assignment(self) -> None:
        with self.assertRaises(MathParseError):
            parse_input("x = 1 = 2", self.store, 1)

    def test_assignment_to_constant_is_rejected(self) -> None:
        with self.assertRaises(MathParseError):
            parse_input("pi = 3", self.store, 1)


if __name__ == "__main__":
    unittest.main()
