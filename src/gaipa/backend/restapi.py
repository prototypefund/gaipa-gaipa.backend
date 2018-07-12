from plone.dexterity.interfaces import IDexterityContent
from plone.restapi.interfaces import IFieldSerializer
from plone.restapi.serializer.converters import json_compatible
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from zope.schema.interfaces import IChoice
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility


@adapter(IChoice, IDexterityContent, Interface)
@implementer(IFieldSerializer)
class ChoiceFieldSerializer(object):

    def __init__(self, field, context, request):
        self.context = context
        self.request = request
        self.field = field

    def __call__(self):
        return json_compatible(self.get_value())

    def get_value(self, default=None):
        vocab_value = {
            'token': None,
            'title': None,
        }
        value = getattr(
            self.field.interface(self.context),
            self.field.__name__,
            default,
        )
        if not value:
            return
        vocab_value['token'] = value
        factory = getUtility(IVocabularyFactory, self.field.vocabularyName)
        if not factory:
            return vocab_value
        # collective.taxonomy:
        if hasattr(factory, 'translate'):
            vocab_value['title'] = factory.translate(value, context=self.context)
        elif IVocabularyFactory.providedBy(factory):
            vocab = factory(self.context)
            vocab_value['title'] = vocab.getTermByToken(value).title
        return vocab_value
