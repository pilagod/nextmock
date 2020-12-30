from ..mock import Mock


class TestMockClass:

    def test_mock_as_class_work_properly(self):
        m = Mock()
        assert isinstance(m.func, Mock)
        m.func.with_args(1, a=1).returns(123)
        assert m.func(1, a=1) == 123
