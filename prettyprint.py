#!/usr/bin/env python3
from functools import partial

__all__ = ('pprint', 'get_pprint_func')
__author__ = 'sherry'


def _pprint_dict(o, depth, end):
    print("{")
    for k, v in sorted(o.items()):
        pprint(k, depth + 1, end=": ")
        pprint(v, depth + 1, indent=False, end=",\n")
    print("  " * depth + "}", end=end)


def _pprint_sequence(o, depth, end, delim):
    print(delim[0])
    for v in o:
        pprint(v, depth + 1, end=",\n")
    print("  " * depth + delim[1], end=end)


def _pprint_list(o, depth, end):
    _pprint_sequence(o, depth, end, "[]")


def _pprint_tuple(o, depth, end):
    _pprint_sequence(o, depth, end, "()")


def _pprint_set(o, depth, end):
    _pprint_sequence(o, depth, end, "{}")


def _pprint_repr(o, depth, end):
    print(repr(o), end=end)


def _pprint_instance(o, depth, end):
    mod = "" if o.__class__.__module__ == "__main__" else (o.__class__.__module__ + ".")
    print(mod + o.__class__.__name__, end=" ")
    pprint(o.__dict__, depth, indent=False, end=end)


PPRINT_FUNCS = {
    list: _pprint_list,
    tuple: _pprint_tuple,
    dict: _pprint_dict,
    set: _pprint_set,
    frozenset: _pprint_set,
}


def get_pprint_func(o):
    if type(o).__flags__ & (1 << 9):  # Py_TPFLAGS_HEAPTYPE
        return getattr(o, "__pprint__", partial(_pprint_instance, o))
    else:
        return partial(PPRINT_FUNCS.get(type(o), _pprint_repr), o)


def pprint(o, depth=0, *, indent=True, end="\n"):
    """
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
    """
    if indent:
        print("  " * depth, end="")
    return get_pprint_func(o)(depth, end)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
