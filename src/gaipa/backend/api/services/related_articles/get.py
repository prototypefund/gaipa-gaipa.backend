# -*- coding: utf-8 -*-
from plone import api
from plone.restapi.interfaces import IExpandableElement
from plone.restapi.services import Service
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer


@implementer(IExpandableElement)
@adapter(Interface, Interface)
class RelatedArticles(object):

    def __init__(self, context, request):
        self.context = context.aq_explicit
        self.request = request

    def __call__(self, expand=False):
        result = {
            'related-articles': {
                '@id': '{}/@related-articles'.format(
                    self.context.absolute_url(),
                ),
            },
        }
        if not expand:
            return result

        query = {}
        query['portal_type'] = "Chapter"
        solution_categories = [c for c in self.context.solution_category]
        if solution_categories:
            query['solution_category'] = {
                'query': solution_categories,
                'operator': 'and',
            }
        crop_category = self.context.crop_category
        if crop_category:
            query['crop_category'] = crop_category
        brains = api.content.find(**query)
        items = []
        for brain in brains:
            items.append({
                'title': brain.Title,
                '@id': brain.getURL(),
            })

        result['related-articles']['items'] = items
        return result


class RelatedArticlesGet(Service):

    def reply(self):
        related_articles = RelatedArticles(self.context, self.request)
        return related_articles(expand=True)['related-articles']
