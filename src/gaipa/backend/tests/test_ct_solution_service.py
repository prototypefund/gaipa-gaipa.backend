# -*- coding: utf-8 -*-
from gaipa.backend.content.solution_service import ISolutionService  # NOQA E501
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


class SolutionServiceIntegrationTest(unittest.TestCase):

    layer = GAIPA_BACKEND_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'SolutionServices',
            self.portal,
            'parent_id',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_solution_service_schema(self):
        fti = queryUtility(IDexterityFTI, name='Solution Service')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('Solution Service')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_solution_service_fti(self):
        fti = queryUtility(IDexterityFTI, name='Solution Service')
        self.assertTrue(fti)

    def test_ct_solution_service_factory(self):
        fti = queryUtility(IDexterityFTI, name='Solution Service')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ISolutionService.providedBy(obj),
            u'ISolutionService not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_solution_service_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Solution Service',
            id='solution_service',
        )

        self.assertTrue(
            ISolutionService.providedBy(obj),
            u'ISolutionService not provided by {0}!'.format(
                obj.id,
            ),
        )
