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
        self.context = context
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

        solution_categories = [c for c in self.context.solution_category]
        article_brains = api.content.find(
            portal_type="Chapter",
            solution_category={
                'query': solution_categories,
                'operator': 'and',
            }
        )
        items = []
        for article in article_brains:
            items.append({
                'title': article.Title,
                '@id': article.getURL(),
            })

        result['related-articles']['items'] = items
        return result


class RelatedArticlesGet(Service):

    def reply(self):
        related_articles = RelatedArticles(self.context, self.request)
        return related_articles(expand=True)['related-articles']
