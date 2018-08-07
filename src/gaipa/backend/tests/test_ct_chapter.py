# -*- coding: utf-8 -*-
from gaipa.backend.content.chapter import IChapter  # NOQA E501
from gaipa.backend.testing import GAIPA_BACKEND_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class ChapterIntegrationTest(unittest.TestCase):

    layer = GAIPA_BACKEND_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'SolutionArticle',
            self.portal,
            'chapter',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_chapter_schema(self):
        fti = queryUtility(IDexterityFTI, name='Chapter')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('Chapter')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_chapter_fti(self):
        fti = queryUtility(IDexterityFTI, name='Chapter')
        self.assertTrue(fti)

    def test_ct_chapter_factory(self):
        fti = queryUtility(IDexterityFTI, name='Chapter')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IChapter.providedBy(obj),
            u'IChapter not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_chapter_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Chapter',
            id='chapter',
        )

        self.assertTrue(
            IChapter.providedBy(obj),
            u'IChapter not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_chapter_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Chapter')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_chapter_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Chapter')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'chapter_id',
            title='Chapter container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
