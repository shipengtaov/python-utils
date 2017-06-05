# -*- coding: utf-8 -*-


def anyin(elements, holder):
    """

    >>> anyin(['foo', 'bar'], 'aa_foo_bb')
    True

    >>> anyin(['foo', 'bar'], 'test')
    False
    """
    return any([i in holder for i in elements])
