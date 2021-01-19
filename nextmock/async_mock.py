import inspect

from .mock import Mock


class AsyncMock(Mock):

    async def __call__(self, *args, **kwargs):
        result = super().__call__(*args, **kwargs)
        if inspect.iscoroutine(result):
            result = await result
        return result
