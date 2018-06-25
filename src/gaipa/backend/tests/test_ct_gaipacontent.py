# -*- coding: utf-8 -*-
from gaipa.backend.content.gaipacontent import IGaipacontent  # NOQA E501
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


class GaipacontentIntegrationTest(unittest.TestCase):

    layer = GAIPA_BACKEND_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_gaipacontent_schema(self):
        fti = queryUtility(IDexterityFTI, name='GaipaContent')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('GaipaContent')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_gaipacontent_fti(self):
        fti = queryUtility(IDexterityFTI, name='GaipaContent')
        self.assertTrue(fti)

    def test_ct_gaipacontent_factory(self):
        fti = queryUtility(IDexterityFTI, name='GaipaContent')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IGaipacontent.providedBy(obj),
            u'IGaipacontent not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_gaipacontent_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='GaipaContent',
            id='gaipacontent',
        )

        self.assertTrue(
            IGaipacontent.providedBy(obj),
            u'IGaipacontent not provided by {0}!'.format(
                obj.id,
            ),
        )
