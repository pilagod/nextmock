from ..mock import Mock


class TestMockReturns:

    def test_returns_should_always_return_stub_result(self):
        m = Mock()
        m.returns(123)
        assert m() == 123
        assert m(1, 2, 3) == 123
