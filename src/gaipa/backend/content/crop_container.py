# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class ICropContainer(model.Schema):
    """ Marker interface for CropContainer
    """


@implementer(ICropContainer)
class CropContainer(Container):
    """
    """
