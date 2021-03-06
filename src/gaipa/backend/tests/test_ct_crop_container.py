# -*- coding: utf-8 -*-
from gaipa.backend.content.crop_container import ICropContainer  # NOQA E501
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


class CropContainerIntegrationTest(unittest.TestCase):

    layer = GAIPA_BACKEND_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_crop_container_schema(self):
        fti = queryUtility(IDexterityFTI, name='CropContainer')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('CropContainer')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_crop_container_fti(self):
        fti = queryUtility(IDexterityFTI, name='CropContainer')
        self.assertTrue(fti)

    def test_ct_crop_container_factory(self):
        fti = queryUtility(IDexterityFTI, name='CropContainer')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ICropContainer.providedBy(obj),
            u'ICropContainer not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_crop_container_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='CropContainer',
            id='crop_container',
        )

        self.assertTrue(
            ICropContainer.providedBy(obj),
            u'ICropContainer not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_crop_container_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='CropContainer')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_crop_container_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='CropContainer')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'crop_container_id',
            title='CropContainer container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
