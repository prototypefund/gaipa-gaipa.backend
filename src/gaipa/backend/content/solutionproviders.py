# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class ISolutionproviders(model.Schema):
    """ Marker interface for Solutionproviders
    """


@implementer(ISolutionproviders)
class Solutionproviders(Container):
    """
    """
