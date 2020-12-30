from .mock import Mock


class AsyncMock(Mock):

    async def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)
