# -*- coding: utf-8 -*-
from gaipa.backend.content.pests import IPests  # NOQA E501
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


class PestsIntegrationTest(unittest.TestCase):

    layer = GAIPA_BACKEND_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_pests_schema(self):
        fti = queryUtility(IDexterityFTI, name='Pests')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('Pests')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_pests_fti(self):
        fti = queryUtility(IDexterityFTI, name='Pests')
        self.assertTrue(fti)

    def test_ct_pests_factory(self):
        fti = queryUtility(IDexterityFTI, name='Pests')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IPests.providedBy(obj),
            u'IPests not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_pests_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Pests',
            id='pests',
        )

        self.assertTrue(
            IPests.providedBy(obj),
            u'IPests not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_pests_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Pests')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_pests_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Pests')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'pests_id',
            title='Pests container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
