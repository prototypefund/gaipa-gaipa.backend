# -*- coding: utf-8 -*-
from gaipa.backend.testing import GAIPA_BACKEND_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.interfaces import IVocabularyTokenized

import unittest


class CropCategoriesIntegrationTest(unittest.TestCase):

    layer = GAIPA_BACKEND_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.mycrop = api.content.create(
            type='Crop',
            container=self.portal.app.crop,
            id='my-crop',
            title='My Crop',
        )
        api.content.create(
            type='Crop',
            container=self.portal.app.crop,
            id='tomato',
            title='Tomato',
        )

    def test_vocab_crop_categories(self):
        vocab_name = 'gaipa.backend.CropCategories'
        factory = getUtility(IVocabularyFactory, vocab_name)
        self.assertTrue(IVocabularyFactory.providedBy(factory))

        vocabulary = factory(self.portal)
        self.assertTrue(IVocabularyTokenized.providedBy(vocabulary))
        self.assertEqual(
            vocabulary.getTerm(self.mycrop.absolute_url_path()).title,
            u'My Crop',
        )
