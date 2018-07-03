# -*- coding: utf-8 -*-
from plone import api
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


def _get_base_path(path):
    base_obj = api.content.get(path)
    if not base_obj:
        return
    base_path = '/'.join(base_obj.getPhysicalPath())
    return base_path


def get_solutions_base_path(context):
    """
    """
    return _get_base_path('/app/solution')


class INavassistantcard(model.Schema):
    """ Marker interface for Navassistantcard
    """
    model.load('navassistantcard.xml')

    directives.widget(
        'solutions',
        pattern_options={
            'basePath': get_solutions_base_path,
            'selectableTypes': ['SolutionArticle']
        }
    )


@implementer(INavassistantcard)
class Navassistantcard(Container):
    """
    """
