# -*- coding: utf-8 -*-

from ..content.chapter import IChapter
from plone.indexer import indexer


@indexer(IChapter)
def crop_category(obj):
    context = obj.aq_inner.aq_parent
    return context.crop_category
