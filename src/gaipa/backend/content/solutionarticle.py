# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class ISolutionarticle(model.Schema):
    """ Marker interface for Solutionarticle
    """


@implementer(ISolutionarticle)
class Solutionarticle(Container):
    """
    """
