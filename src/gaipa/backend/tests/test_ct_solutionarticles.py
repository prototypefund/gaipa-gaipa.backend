# -*- coding: utf-8 -*-
from gaipa.backend.content.solutionarticles import ISolutionarticles  # NOQA E501
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


class SolutionarticlesIntegrationTest(unittest.TestCase):

    layer = GAIPA_BACKEND_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'GaipaContent',
            self.portal,
            'parent_id',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_solutionarticles_schema(self):
        fti = queryUtility(IDexterityFTI, name='SolutionArticles')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('SolutionArticles')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_solutionarticles_fti(self):
        fti = queryUtility(IDexterityFTI, name='SolutionArticles')
        self.assertTrue(fti)

    def test_ct_solutionarticles_factory(self):
        fti = queryUtility(IDexterityFTI, name='SolutionArticles')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ISolutionarticles.providedBy(obj),
            u'ISolutionarticles not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_solutionarticles_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='SolutionArticles',
            id='solutionarticles',
        )

        self.assertTrue(
            ISolutionarticles.providedBy(obj),
            u'ISolutionarticles not provided by {0}!'.format(
                obj.id,
            ),
        )
