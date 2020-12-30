import pytest

from typing import List

from ..arg import Arg
from ..mock import Mock


class TestMockWithArgs:

    # args

    def test_with_args_should_return_stub_result_when_args_matched(self):
        m = Mock()
        m.with_args(1, 2, 3).returns(123)
        assert m(1, 2, 3) == 123

    def test_with_args_should_not_return_stub_result_when_args_not_matched(self):
        m = Mock()
        m.with_args(1, 2, 3).returns(123)
        assert m(3, 2, 1) != 123

    def test_with_args_should_return_stub_result_when_dict_in_args_matched(self):
        m = Mock()
        m.with_args({
            "a": 1,
            "b": 2,
            "c": 3
        }).returns(123)
        assert m({
            "a": 1,
            "b": 2,
            "c": 3
        }) == 123

    # kwargs

    def test_with_args_should_return_stub_result_when_kwargs_matched(self):
        m = Mock()
        m.with_args(a=1, b=2, c=3).returns(123)
        assert m(a=1, b=2, c=3) == 123

    def test_with_args_should_not_return_stub_result_when_kwargs_not_matched(self):
        m = Mock()
        m.with_args(a=1, b=2, c=3).returns(123)
        assert m(a=3, b=2, c=1) != 123

    # args & kwargs

    def test_with_args_should_return_stub_result_when_both_args_and_kwargs_matched(self):
        m = Mock()
        m.with_args(1, 2, 3, a=1, b=2, c=3).returns(123)
        assert m(1, 2, 3, a=1, b=2, c=3) == 123

    def test_with_args_should_not_return_stub_result_when_args_matched_but_kwargs_not_matched(self):
        m = Mock()
        m.with_args(1, 2, 3, a=1, b=2, c=3).returns(123)
        assert m(1, 2, 3, a=3, b=2, c=1) != 123

    # class as args & kwargs

    class Cmd:
        def __init__(self, a: int, b: str):
            self.a = a
            self.b = b

    def test_with_args_should_return_stub_result_when_class_properties_matched_in_args(self):
        m = Mock()
        m.with_args(self.Cmd(1, "123")).returns(123)
        assert m(self.Cmd(1, "123")) == 123

    def test_with_args_should_not_return_stub_result_when_class_properties_not_matched_in_args(self):
        m = Mock()
        m.with_args(self.Cmd(1, "123")).returns(123)
        assert m(self.Cmd(999, "321")) != 123

    def test_with_args_should_return_stub_result_when_class_properties_matched_in_kwargs(self):
        m = Mock()
        m.with_args(a=self.Cmd(1, "123")).returns(123)
        assert m(a=self.Cmd(1, "123")) == 123

    def test_with_args_should_not_return_stub_result_when_class_properties_not_matched_in_kwargs(self):
        m = Mock()
        m.with_args(a=self.Cmd(1, "123")).returns(123)
        assert m(a=self.Cmd(999, "321")) != 123

    # nested class as args & kwargs

    class CmdNested:
        def __init__(self, a: List[int], b: dict, c: "TestMockWithArgs.Cmd"):
            self.a = a
            self.b = b
            self.c = c

    def test_with_args_should_return_stub_result_when_nested_class_properties_matched_in_args(self):
        m = Mock()
        m.with_args(
            self.CmdNested(
                [1, 2, 3],
                {
                    "a": 1,
                    "b": 2,
                    "c": 3
                },
                self.Cmd(123, "123")
            )
        ).returns(123)
        assert m(
            self.CmdNested(
                [1, 2, 3],
                {
                    "a": 1,
                    "b": 2,
                    "c": 3
                },
                self.Cmd(123, "123")
            )
        ) == 123

    def test_with_args_should_not_return_stub_result_when_nested_class_properties_not_matched_in_args(self):
        m = Mock()
        m.with_args(
            self.CmdNested(
                [1, 2, 3],
                {
                    "a": 1,
                    "b": 2,
                    "c": 3
                },
                self.Cmd(123, "123")
            )
        ).returns(123)
        assert m(
            self.CmdNested(
                [3, 2, 1],
                {
                    "a": 3,
                    "b": 2,
                    "c": 1
                },
                self.Cmd(321, "321")
            )
        ) != 123

    def test_with_args_should_return_stub_result_when_nested_class_properties_matched_in_kwargs(self):
        m = Mock()
        m.with_args(
            a=self.CmdNested(
                [1, 2, 3],
                {
                    "a": 1,
                    "b": 2,
                    "c": 3
                },
                self.Cmd(123, "123")
            )
        ).returns(123)
        assert m(
            a=self.CmdNested(
                [1, 2, 3],
                {
                    "a": 1,
                    "b": 2,
                    "c": 3
                },
                self.Cmd(123, "123")
            )
        ) == 123

    def test_with_args_should_not_return_stub_result_when_nested_class_properties_not_matched_in_kwargs(self):
        m = Mock()
        m.with_args(
            a=self.CmdNested(
                [1, 2, 3],
                {
                    "a": 1,
                    "b": 2,
                    "c": 3
                },
                self.Cmd(123, "123")
            )
        ).returns(123)
        assert m(
            a=self.CmdNested(
                [3, 2, 1],
                {
                    "a": 3,
                    "b": 2,
                    "c": 1
                },
                self.Cmd(321, "321")
            )
        ) != 123

    # exception

    def test_with_args_should_raise_stub_exception_when_args_matched(self):
        m = Mock()
        m.with_args(1, 2, 3).raises(ValueError("value error"))
        with pytest.raises(ValueError) as e:
            m(1, 2, 3)
        assert str(e.value) == "value error"

    def test_with_args_should_not_raise_stub_exception_when_args_not_matched(self):
        m = Mock()
        m.with_args(1, 2, 3).raises(ValueError("value error"))
        m(3, 2, 1)

    # ordering

    def test_with_args_should_return_last_stub_result_when_multiple_stubs_matched(self):
        m = Mock()
        m.with_args(1, 2, 3).returns(123)
        m.with_args(1, 2, 3).returns(456)
        assert m(1, 2, 3) == 456

    # any

    def test_with_args_should_return_stub_result_when_any_in_args_is_provided(self):
        m = Mock()
        m.with_args(1, 2, Arg.Any).returns(123)
        assert m(1, 2, 1) == 123
        assert m(1, 2, 9) == 123
        assert m(1, 2, "123") == 123

    def test_with_args_should_return_stub_result_when_any_in_kwargs_is_provided(self):
        m = Mock()
        m.with_args(a=1, b=2, c=Arg.Any).returns(123)
        assert m(a=1, b=2, c=1) == 123
        assert m(a=1, b=2, c=9) == 123
        assert m(a=1, b=2, c="123") == 123
