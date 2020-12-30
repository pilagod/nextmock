import pytest

from unittest.mock import call

from ..mock import Mock

# https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock


class TestMockCompatibility:

    # assert called

    def test_assert_called_should_work_properly(self):
        m = Mock()

        with pytest.raises(AssertionError):
            m.assert_called()

        m(1, 2, 3)
        m.assert_called()

    def test_assert_called_once_should_work_properly(self):
        m = Mock()

        m(1, 2, 3)
        m.assert_called_once()

        m(1, 2, 3)
        with pytest.raises(AssertionError):
            m.assert_called_once()

    def test_assert_called_with_should_work_properly(self):
        m = Mock()

        m(1, a=1)
        m.assert_called_with(1, a=1)

        with pytest.raises(AssertionError):
            m.assert_called_with(2, b=2)

    def test_assert_called_once_with_should_work_properly(self):
        m = Mock()

        with pytest.raises(AssertionError):
            m.assert_called_once_with(1, a=1)

        m(1, a=1)
        m.assert_called_once_with(1, a=1)

        with pytest.raises(AssertionError):
            m.assert_called_once_with(2, b=2)

        m(1, a=1)
        with pytest.raises(AssertionError):
            m.assert_called_once_with(1, a=1)

    def test_assert_any_call_should_work_properly(self):
        m = Mock()

        with pytest.raises(AssertionError):
            m.assert_any_call(1, a=1)

        m(1, a=1)
        m.assert_any_call(1, a=1)

        m(2, b=2)
        m.assert_any_call(1, a=1)

    def test_assert_has_calls_should_work_properly(self):
        m = Mock()

        m(1, a=1)
        m(2, b=2)

        m.assert_has_calls([
            call(1, a=1),
            call(2, b=2)
        ])
        m.assert_has_calls([
            call(2, b=2),
            call(1, a=1)
        ], any_order=True)

    def test_assert_not_called_should_work_properly(self):
        m = Mock()
        m.assert_not_called()
        m(1, 2, 3)
        with pytest.raises(AssertionError):
            m.assert_not_called()

    # return

    def test_return_value_should_work_properly(self):
        m = Mock()
        m.return_value = 123
        assert m() == 123
        assert m(1, 2, 3) == 123

    def test_return_value_should_be_fallback_when_with_args_is_set(self):
        m = Mock()
        m.return_value = 456
        m.with_args(1, 2, 3).returns(123)
        assert m(1, 2, 3) == 123
        assert m() == 456

    # reset

    def test_reset_mock_should_work_properly(self):
        m = Mock()
        m.with_args(1, 2, 3).returns(123)
        assert m(1, 2, 3) == 123
        m.reset_mock()
        assert m(1, 2, 3) != 123

    # side effect

    def test_side_effect_can_raise_exception(self):
        m = Mock()
        m.side_effect = ValueError("value error")
        with pytest.raises(ValueError):
            m()

    def test_side_effect_can_take_function(self):
        m = Mock()

        def side_effect():
            return 123

        m.side_effect = side_effect
        assert m() == 123

    def test_side_effect_should_be_fallback_when_with_args_is_set(self):
        m = Mock()

        # side effect function should have signature to accept any type of args
        def side_effect(*args, **kwargs):
            return 456

        m.side_effect = side_effect
        m.with_args(1, 2, 3).returns(123)

        assert m(1, 2, 3) == 123
        assert m() == 456
