# -*- coding: utf-8 -*-
from plone import api
from plone.restapi.interfaces import IExpandableElement
from plone.restapi.services import Service
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer


@implementer(IExpandableElement)
@adapter(Interface, Interface)
class RelatedServices(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self, expand=False):
        result = {
            'related-services': {
                '@id': '{}/@related-services'.format(
                    self.context.absolute_url(),
                ),
            },
        }
        if not expand:
            return result

        solution_categories = [c for c in self.context.solution_category]
        brains = api.content.find(
            portal_type="Solution Service",
            solution_category={
                'query': solution_categories,
                'operator': 'and',
            }
        )
        items = []
        for brain in brains:
            items.append({
                'title': brain.Title,
                '@id': brain.getURL(),
            })

        result['related-services']['items'] = items
        return result


class RelatedServicesGet(Service):

    def reply(self):
        related_services = RelatedServices(self.context, self.request)
        return related_services(expand=True)['related-services']
