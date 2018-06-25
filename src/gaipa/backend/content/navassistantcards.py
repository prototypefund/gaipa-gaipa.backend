# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class INavassistantcards(model.Schema):
    """ Marker interface for Navassistantcards
    """


@implementer(INavassistantcards)
class Navassistantcards(Container):
    """
    """
