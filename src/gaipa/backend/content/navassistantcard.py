# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class INavassistantcard(model.Schema):
    """ Marker interface for Navassistantcard
    """


@implementer(INavassistantcard)
class Navassistantcard(Container):
    """
    """
