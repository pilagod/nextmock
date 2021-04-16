from ..mock import Mock


class TestMockReturns:

    def test_returns_should_always_return_stub_result(self):
        m = Mock()
        m.returns(123)
        assert m() == 123
        assert m(1, 2, 3) == 123

    def test_returns_when_given_zero_value(self):
        m = Mock()
        m.returns(0)
        assert m() == 0
        assert m(1, 2, 3) == 0
