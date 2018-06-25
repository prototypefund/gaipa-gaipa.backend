# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IGaipacontent(model.Schema):
    """ Marker interface for Gaipacontent
    """


@implementer(IGaipacontent)
class Gaipacontent(Container):
    """
    """
