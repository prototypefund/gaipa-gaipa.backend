# -*- coding: utf-8 -*-
from gaipa.backend.content.solutionservices import ISolutionservices  # NOQA E501
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


class SolutionservicesIntegrationTest(unittest.TestCase):

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

    def test_ct_solutionservices_schema(self):
        fti = queryUtility(IDexterityFTI, name='SolutionServices')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('SolutionServices')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_solutionservices_fti(self):
        fti = queryUtility(IDexterityFTI, name='SolutionServices')
        self.assertTrue(fti)

    def test_ct_solutionservices_factory(self):
        fti = queryUtility(IDexterityFTI, name='SolutionServices')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ISolutionservices.providedBy(obj),
            u'ISolutionservices not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_solutionservices_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='SolutionServices',
            id='solutionservices',
        )

        self.assertTrue(
            ISolutionservices.providedBy(obj),
            u'ISolutionservices not provided by {0}!'.format(
                obj.id,
            ),
        )
