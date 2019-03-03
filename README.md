# prettyprint

[![Build Status](https://travis-ci.org/sherry255/prettyprint.svg?branch=master)](https://travis-ci.org/sherry255/prettyprint)

# Install
```
pip install git+git://github.com/sherry255/prettyprint.git
```

# Usage
```pycon
    >>> from prettyprint import pprint
    >>> pprint(True)
    True
    >>> pprint("aaaaa")
    'aaaaa'
    >>> pprint(b"aaaaa")
    b'aaaaa'
    >>> pprint(bytearray(b"123"))
    bytearray(b'123')
    >>> pprint(1)
    1
    >>> pprint(1.0)
    1.0
    >>> pprint({1, 2, 3})
    {
      1,
      2,
      3,
    }
    >>> pprint(frozenset([1,2,3]))
    {
      1,
      2,
      3,
    }
    >>> pprint([1, 2, 3])
    [
      1,
      2,
      3,
    ]
    >>> pprint({"a": {"b": "c"}})
    {
      'a': {
        'b': 'c',
      },
    }
    >>> class A:
    ...     def __init__(self):
    ...         self.a = 1
    ...         self.b = 2
    ...
    >>> pprint(A())
    A {
      'a': 1,
      'b': 2,
    }
    >>> class B:
    ...     def __pprint__(self, depth, end):
    ...         print("<B>", end=end)
    >>> pprint(B())
    <B>
```
