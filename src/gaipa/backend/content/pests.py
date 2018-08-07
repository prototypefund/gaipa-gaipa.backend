# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IPests(model.Schema):
    """ Marker interface for Pests
    """


@implementer(IPests)
class Pests(Container):
    """
    """
