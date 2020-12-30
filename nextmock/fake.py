from typing import Any, Optional

from .arg import Arg


class Fake:

    def __init__(
        self,
        *args,
        always_matched: bool = False,
        **kwargs
    ):
        self._always_matched = always_matched
        self._args = args
        self._kwargs = kwargs
        self._result: Any = None
        self._exception: Optional[Exception] = None

    def raises(self, e: Exception):
        self._exception = e

    def returns(self, result: Any):
        self._result = result

    # private

    def _can_apply(self, *args, **kwargs) -> bool:
        if self._always_matched:
            return True
        return (
            self._check_args_matched(*args)
            and self._check_kwargs_matched(**kwargs)
        )

    def _check_args_matched(self, *args) -> bool:
        for idx, arg in enumerate(self._args):
            if arg == Arg.Any:
                continue
            if len(args) <= idx or not self._match(arg, args[idx]):
                return False
        return True

    def _check_kwargs_matched(self, **kwargs) -> bool:
        for k in self._kwargs:
            if self._kwargs[k] == Arg.Any:
                continue
            if k not in kwargs or not self._match(self._kwargs[k], kwargs[k]):
                return False
        return True

    def _execute(self) -> Any:
        if self._result:
            return self._result
        if self._exception:
            raise self._exception

    def _match(self, arg1: Any, arg2: Any) -> bool:
        if self._is_object(arg1):
            return self._match_object(arg1, arg2)
        return self._match_value(arg1, arg2)

    def _is_object(self, arg: Any) -> bool:
        return hasattr(arg, "__dict__")

    def _match_object(self, arg1: Any, arg2: Any) -> bool:
        if not (self._is_object(arg1) and self._is_object(arg2)):
            return False

        d1 = arg1.__dict__
        d2 = arg2.__dict__
        for k in d1:
            if k not in d2 or not self._match(d1[k], d2[k]):
                return False
        return True

    def _match_value(self, arg1: Any, arg2: Any) -> bool:
        return arg1 == arg2
