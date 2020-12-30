# NextMock

NextMock is an enhanced mock for [unittest.mock.Mock](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock).

## Features

- Argument matching supported.
- Async version (AsyncMock) provided.
- Compatible with [unittest.mock.Mock](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock).

## Usage

First install `nextmock` from pip:

```shell
$ pip install nextmock
```

then import Mock for common usage, AsyncMock for async usage:

```python
from nextmock import Mock
from nextmock import AsyncMock
```

## API with Examples

### with_args

Return/raise stub result/error only when given args are matched.

> Check out [`/nextmock/test/test_mock_with_args.py`](https://github.com/pilagod/nextmock/blob/master/nextmock/test/test_mock_with_args.py) for comprehensive exmaples.

- args matching

    ```python
    m = Mock()

    m.with_args(1, 2, 3).returns(123)

    assert m(1, 2, 3) == 123
    assert m(3, 2, 1) != 123
    ```

- kwargs matching

    ```python
    m = Mock()

    m.with_args(a=1, b=2, c=3).returns(123)

    assert m(a=1, b=2, c=3) == 123
    assert m(a=3, b=2, c=1) != 123
    ```

- class matching

    ```python
    class Cmd:
        def __init__(self, a: int, b: str):
            self.a = a
            self.b = b
    
    m = Mock()

    m.with_args(Cmd(1, "123")).returns(123)

    assert m(Cmd(1, "123")) == 123
    assert m(Cmd(999, "321")) != 123
    ```

- args matcher

    ```python
    from nextmock import Arg

    m = Mock()

    m.with_args(1, 2, Arg.Any).returns(123)

    assert m(1, 2, 1) == 123
    assert m(1, 2, 9) == 123
    assert m(1, 2, "123") == 123
    ```

- error raising

    ```python
    m = Mock()

    m.with_args(1, 2, 3).raises(ValueError("value error"))

    with pytest.raises(ValueError) as e:
        m(1, 2, 3)

    assert str(e.value) == "value error"
    ```

### returns

Return stub result without matching args.

```python
m = Mock()

m.returns(123)

assert m(1, 2, 3) == 123
assert m(a=1, b=2, c=3) == 123
```

### raises

Raise stub error without matching args.

```python
m = Mock()

m.raises(ValueError("value error"))

with pytest.raises(ValueError) as e:
    m(1, 2, 3)

with pytest.raises(ValueError) as e:
    m(a=1, b=2, c=3)
```

## Compatibility

Inherit behavior from [unittest.mock.Mock](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock).

> Check out [`/nextmock/test/test_mock_compatibility.py`](https://github.com/pilagod/nextmock/blob/master/nextmock/test/test_mock_compatibility.py) for comprehensive examples.

```python
m = Mock()

m.return_value = 123

assert m(1, 2, 3) == 123

m.assert_called_once()
m.assert_called_with(1, 2, 3)
```

## License

© Chun-Yan Ho (pilagod), 2020-NOW

Released under the [MIT License](https://github.com/pilagod/nextmock/blob/master/LICENSE)
