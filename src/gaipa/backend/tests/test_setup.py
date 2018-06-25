# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from gaipa.backend.testing import GAIPA_BACKEND_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that gaipa.backend is properly installed."""

    layer = GAIPA_BACKEND_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if gaipa.backend is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'gaipa.backend'))

    def test_browserlayer(self):
        """Test that IGaipaBackendLayer is registered."""
        from gaipa.backend.interfaces import (
            IGaipaBackendLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IGaipaBackendLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = GAIPA_BACKEND_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['gaipa.backend'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if gaipa.backend is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'gaipa.backend'))

    def test_browserlayer_removed(self):
        """Test that IGaipaBackendLayer is removed."""
        from gaipa.backend.interfaces import \
            IGaipaBackendLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IGaipaBackendLayer,
            utils.registered_layers())
