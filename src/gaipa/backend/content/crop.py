# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class ICrop(model.Schema):
    """ Marker interface for Crop
    """


@implementer(ICrop)
class Crop(Container):
    """
    """
