import pytest

from ..mock import Mock


class TestMockRaises:

    def test_raises_should_always_raises_stub_exception(self):
        m = Mock()
        m.raises(ValueError("value error"))

        with pytest.raises(ValueError):
            m()

        with pytest.raises(ValueError):
            m(1, 2, 3)
