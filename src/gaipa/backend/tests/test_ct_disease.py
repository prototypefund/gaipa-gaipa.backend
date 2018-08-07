# -*- coding: utf-8 -*-
from gaipa.backend.content.disease import IDisease  # NOQA E501
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


class DiseaseIntegrationTest(unittest.TestCase):

    layer = GAIPA_BACKEND_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Diseases',
            self.portal,
            'disease',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_disease_schema(self):
        fti = queryUtility(IDexterityFTI, name='Disease')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('Disease')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_disease_fti(self):
        fti = queryUtility(IDexterityFTI, name='Disease')
        self.assertTrue(fti)

    def test_ct_disease_factory(self):
        fti = queryUtility(IDexterityFTI, name='Disease')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IDisease.providedBy(obj),
            u'IDisease not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_disease_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Disease',
            id='disease',
        )

        self.assertTrue(
            IDisease.providedBy(obj),
            u'IDisease not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_disease_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Disease')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_disease_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Disease')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'disease_id',
            title='Disease container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
