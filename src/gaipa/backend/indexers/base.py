# -*- coding: utf-8 -*-
from plone.dexterity.interfaces import IDexterityContent
from plone.indexer import indexer


@indexer(IDexterityContent)
def dummy(obj):
    """Dummy to prevent indexing child objects"""
    raise AttributeError('This field should not indexed here!')

