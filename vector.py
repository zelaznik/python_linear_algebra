from __future__ import division
from functools import wraps as wraps
from numbers import Number
import unittest

def assertcompatible(func):
    @wraps(func)
    def wrappped(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors have unequal lengths")
        else:
            return func(self, other)
    return wrappped

def assert_other_is(klass, is_operator=True):
    if is_operator:
        def decorator(func):
            @wraps(func)
            def wrapped(self, other):
                if isinstance(other, klass):
                    return func(self, other)
                else:
                    return NotImplemented
            return wrapped
    else:
        def decorator(func):
            @wraps(func)
            def wrapped(self, other):
                if isinstance(other, klass):
                    return func(self, other)
                else:
                    raise TypeError("Other argument must be an instance of %s" %(klass.__name__,))
            return wrapped

    return decorator

class Vector(object):
    __slots__ = ('__numbers',)

    def __init__(self, numbers):
        self.__numbers = list(numbers)

    def __getitem__(self, key):
        if key < 0:
            raise IndexError("Index %r is out of range" % (key,))
        return self.__numbers[key]

    def __iter__(self):
        for item in self.__numbers:
            yield item

    def __len__(self):
        return len(self.__numbers)

    def __abs__(self):
        return self.dot(self) ** 0.5

    @assert_other_is(Number)
    def __mul__(self, number):
        return self.__class__(value*number for value in self)

    __rmul__ = __mul__

    @assert_other_is(Number)
    def __truediv__(self, number):
        return self.__class__(value/number for value in self)

    def __repr__(self):
        return '%s([%s])' % (self.__class__.__name__, ', '.join(repr(r) for r in self))

    @assertcompatible
    def dot(self, vector):
        return sum(value*vector[i] for i, value in enumerate(self))

    def normalized(self):
        abs_v = abs(self)
        return self.__class__( v / abs_v for v in self)

    @assertcompatible
    def projection_onto(self, vector):
        return (self.dot(vector) / vector.dot(vector)) * vector


class VectorText(unittest.TestCase):
    def test_dot_product(self):
        a = Vector([1, 2])
        b = Vector([3, 4])
        self.assertEqual(a.dot(b), 11)

