# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IPest(model.Schema):
    """ Marker interface for Pest
    """


@implementer(IPest)
class Pest(Container):
    """
    """
