# -*- coding: utf-8 -*-
from gaipa.backend.content.solutionproviders import ISolutionproviders  # NOQA E501
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


class SolutionprovidersIntegrationTest(unittest.TestCase):

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

    def test_ct_solutionproviders_schema(self):
        fti = queryUtility(IDexterityFTI, name='SolutionProviders')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('SolutionProviders')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_solutionproviders_fti(self):
        fti = queryUtility(IDexterityFTI, name='SolutionProviders')
        self.assertTrue(fti)

    def test_ct_solutionproviders_factory(self):
        fti = queryUtility(IDexterityFTI, name='SolutionProviders')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ISolutionproviders.providedBy(obj),
            u'ISolutionproviders not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_solutionproviders_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='SolutionProviders',
            id='solutionproviders',
        )

        self.assertTrue(
            ISolutionproviders.providedBy(obj),
            u'ISolutionproviders not provided by {0}!'.format(
                obj.id,
            ),
        )
