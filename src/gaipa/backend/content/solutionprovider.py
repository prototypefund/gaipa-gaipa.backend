# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class ISolutionprovider(model.Schema):
    """ Marker interface for Solutionprovider
    """


@implementer(ISolutionprovider)
class Solutionprovider(Container):
    """
    """
