# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class ISolutionservices(model.Schema):
    """ Marker interface for Solutionservices
    """


@implementer(ISolutionservices)
class Solutionservices(Container):
    """
    """
