import pytest

from ..async_mock import AsyncMock


class TestAsyncMock:

    @pytest.mark.asyncio
    async def test_async_mock_should_be_awaitable(self):
        m = AsyncMock()
        m.with_args(1, a=1).returns(123)
        assert await m(1, a=1) == 123

    @pytest.mark.asyncio
    async def test_async_mock_side_effect_can_take_async_function(self):
        m = AsyncMock()

        async def side_effect():
            return 123

        m.side_effect = side_effect
        assert await m() == 123
