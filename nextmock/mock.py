from typing import Any, List
from unittest.mock import MagicMock

from .fake import Fake


class Mock(MagicMock):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._fakes: List[Fake] = []

    def __call__(self, *args, **kwargs):
        result = super().__call__(*args, **kwargs)
        for s in self._fakes[::-1]:
            if s._can_apply(*args, **kwargs):
                return s._execute()
        return result

    # public

    def raises(self, e: Exception):
        s = self._create_fake(always_matched=True)
        s.raises(e)

    def returns(self, result: Any):
        s = self._create_fake(always_matched=True)
        s.returns(result)

    def with_args(self, *args, **kwargs) -> Fake:
        return self._create_fake(*args, **kwargs)

    # compatibility

    def reset_mock(
        self,
        visited=None,
        *,
        return_value=False,
        side_effect=False
    ):
        self._fakes = []
        return super().reset_mock(
            visited=visited,
            return_value=return_value,
            side_effect=side_effect
        )

    # util

    def _create_fake(self, *args, always_matched: bool = False, **kwargs) -> Fake:
        f = Fake(
            *args,
            always_matched=always_matched,
            **kwargs
        )
        self._fakes.append(f)
        return f
