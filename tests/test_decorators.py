from pysign.core.decorators import *

from unittest import TestCase


def f_mul(a, b):
    return a * b * 0.5


def f_mul_int_typed(a: int, b: int) -> float:
    return f_mul(a, b)


def f_mul_int_missing_one(a: int, b) -> float:
    return f_mul(a, b)


def f_mul_int_missing_two(a, b) -> float:
    return f_mul(a, b)


def f_mul_int_missing_all(a, b):
    return f_mul(a, b)


def f_mul_int_typed_kwd(a: int, b: int = 0) -> float:
    return f_mul(a, b)


class SubInt(int):
    pass


class TestDecorators(TestCase):
    def test_assert_correct_typing(self):

        f = assert_correct_typing(f_mul_int_typed)
        f_1 = assert_correct_typing(f_mul_int_missing_one)
        f_2 = assert_correct_typing(f_mul_int_missing_two)
        f_a = assert_correct_typing(f_mul_int_missing_all)
        f_k = assert_correct_typing(f_mul_int_typed_kwd)

        # 1. Check with correct typing

        a, b = 1, 2

        f(a, b)
        f_1(a, b)
        f_2(a, b)
        f_a(a, b)
        f_k(a, b)
        f_k(a, b=b)

        # 2. Check with incorrect typing
        assert_msg = "AssertionError should have been raised"
        no_assert_msg = "Not error should have been raised"

        a, b = 1, 0.5

        error = None
        try:
            f(a, b)
        except AssertionError as e:
            error = e
        assert isinstance(error, AssertionError), assert_msg

        error = None
        try:
            f_1(a, b)
        except AssertionError as e:
            error = e
        self.assertEqual(error, None, msg=no_assert_msg)

        error = None
        try:
            f_2(a, b)
        except AssertionError as e:
            error = e
        self.assertEqual(error, None, msg=no_assert_msg)

        error = None
        try:
            f_a(a, b)
        except AssertionError as e:
            error = e
        self.assertEqual(error, None, msg=no_assert_msg)

        error = None
        try:
            f_k(a, b)
        except AssertionError as e:
            error = e
        assert isinstance(error, AssertionError), assert_msg

        error = None
        try:
            f_k(a, b=b)
        except AssertionError as e:
            error = e
        assert isinstance(error, AssertionError), assert_msg

        a, b = 1, 1j

        error = None
        try:
            f(a, b)
        except AssertionError as e:
            error = e
        assert isinstance(error, AssertionError), assert_msg

        error = None
        try:
            f_1(a, b)
        except AssertionError as e:
            error = e
        assert isinstance(error, AssertionError), assert_msg

        error = None
        try:
            f_2(a, b)
        except AssertionError as e:
            error = e
        assert isinstance(error, AssertionError), assert_msg

        error = None
        try:
            f_a(a, b)
        except AssertionError as e:
            error = e
        self.assertEqual(error, None, msg=no_assert_msg)

        error = None
        try:
            f_k(a, b)
        except AssertionError as e:
            error = e
        assert isinstance(error, AssertionError), assert_msg

        error = None
        try:
            f_k(a, b=b)
        except AssertionError as e:
            error = e
        assert isinstance(error, AssertionError), assert_msg

        # 3. Check with subclasses

        a, b = SubInt(1), SubInt(2)

        f(a, b)

        # 4. Check unpacked multiple errors

        f_u = assert_correct_typing(f, join=False)

        a, b = 1.0, 2.0

        error = None
        try:
            f_u(a, b)
        except AssertionError as e:
            error = e
        assert isinstance(error, AssertionError), assert_msg
