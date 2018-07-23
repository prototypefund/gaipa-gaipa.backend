# -*- coding: utf-8 -*-
from gaipa.backend.content.navassistantcard import INavassistantcard  # NOQA E501
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


class NavassistantcardIntegrationTest(unittest.TestCase):

    layer = GAIPA_BACKEND_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'NavAssistantCards',
            self.portal,
            'parent_id',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_navassistantcard_schema(self):
        fti = queryUtility(IDexterityFTI, name='NavAssistantCard')
        schema = fti.lookupSchema()
        # schema_name = portalTypeToSchemaName('NavAssistantCard')
        self.assertEqual('INavassistantcard', schema.getName())

    def test_ct_navassistantcard_fti(self):
        fti = queryUtility(IDexterityFTI, name='NavAssistantCard')
        self.assertTrue(fti)

    def test_ct_navassistantcard_factory(self):
        fti = queryUtility(IDexterityFTI, name='NavAssistantCard')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            INavassistantcard.providedBy(obj),
            u'INavassistantcard not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_navassistantcard_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='NavAssistantCard',
            id='navassistantcard',
        )

        self.assertTrue(
            INavassistantcard.providedBy(obj),
            u'INavassistantcard not provided by {0}!'.format(
                obj.id,
            ),
        )
