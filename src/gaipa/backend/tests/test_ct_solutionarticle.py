# -*- coding: utf-8 -*-
from gaipa.backend.content.solutionarticle import ISolutionarticle  # NOQA E501
from gaipa.backend.testing import GAIPA_BACKEND_INTEGRATION_TESTING  # noqa
from plone import api
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


class SolutionarticleIntegrationTest(unittest.TestCase):

    layer = GAIPA_BACKEND_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'SolutionArticles',
            self.portal,
            'parent_id',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_solutionarticle_schema(self):
        fti = queryUtility(IDexterityFTI, name='SolutionArticle')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('SolutionArticle')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_solutionarticle_fti(self):
        fti = queryUtility(IDexterityFTI, name='SolutionArticle')
        self.assertTrue(fti)

    def test_ct_solutionarticle_factory(self):
        fti = queryUtility(IDexterityFTI, name='SolutionArticle')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ISolutionarticle.providedBy(obj),
            u'ISolutionarticle not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_solutionarticle_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='SolutionArticle',
            id='solutionarticle',
        )

        self.assertTrue(
            ISolutionarticle.providedBy(obj),
            u'ISolutionarticle not provided by {0}!'.format(
                obj.id,
            ),
        )
