# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class ISolutionService(model.Schema):
    """ Marker interface for SolutionService
    """


@implementer(ISolutionService)
class SolutionService(Container):
    """
    """
