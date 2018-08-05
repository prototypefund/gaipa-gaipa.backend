# -*- coding: utf-8 -*-

from plone.dexterity.interfaces import IDexterityContent
from plone.restapi.interfaces import IFieldSerializer
from plone.restapi.serializer.converters import json_compatible
from zope.component import adapter
from zope.component import getUtility
from zope.interface import implementer
from zope.interface import Interface
from zope.schema.interfaces import IChoice
from zope.schema.interfaces import ICollection
from zope.schema.interfaces import IVocabularyFactory

import six


def _get_vocab_term(context, field, value):
    """ Get vocab term dict
        returns: {'token': token, 'title': title}
    """
    vocab_term = {
        'token': None,
        'title': None,
    }
    vocab_term['token'] = value
    factory = getUtility(IVocabularyFactory, field)
    if not factory:
        return vocab_term

    # collective.taxonomy support:
    if hasattr(factory, 'translate'):
        vocab_term['title'] = _get_taxonomy_vocab_title(
            context,
            factory,
            value,
        )
    elif IVocabularyFactory.providedBy(factory):
        vocab_term['title'] = _get_vocab_title(
            context,
            factory,
            value,
        )
    return vocab_term


def _get_taxonomy_vocab_title(context, factory, value):
        vocab_title = factory.translate(
            value,
            context=context,
        )
        return vocab_title


def _get_vocab_title(context, factory, value):
    vocab = factory(context)
    vocab_title = vocab.getTermByToken(value).title
    return vocab_title


class BaseFieldSerializer(object):

    def __init__(self, field, context, request):
        self.context = context
        self.request = request
        self.field = field

    def __call__(self):
        return json_compatible(self.get_value())


@adapter(IChoice, IDexterityContent, Interface)
@implementer(IFieldSerializer)
class ChoiceFieldSerializer(BaseFieldSerializer):
    """
    """
    def get_value(self, default=None):
        value = getattr(
            self.field.interface(self.context),
            self.field.__name__,
            default,
        )
        if not value:
            return

        term = _get_vocab_term(
            self.context,
            self.field.vocabularyName,
            value,
        )
        return term


@adapter(ICollection, IDexterityContent, Interface)
@implementer(IFieldSerializer)
class CollectionFieldSerializer(BaseFieldSerializer):
    """
    """
    def get_value(self, default=None):
        terms = []
        values = getattr(
            self.field.interface(self.context),
            self.field.__name__,
            default,
        )
        if not values:
            return
        if not IChoice.providedBy(self.field.value_type):
            return

        for value in values:
            term = _get_vocab_term(
                self.context,
                self.field.value_type.vocabularyName,
                value,
            )
            terms.append(term)
        return terms
