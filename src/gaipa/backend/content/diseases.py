# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IDiseases(model.Schema):
    """ Marker interface for Diseases
    """


@implementer(IDiseases)
class Diseases(Container):
    """
    """
