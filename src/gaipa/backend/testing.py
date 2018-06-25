# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import gaipa.backend


class GaipaBackendLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=gaipa.backend)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'gaipa.backend:default')


GAIPA_BACKEND_FIXTURE = GaipaBackendLayer()


GAIPA_BACKEND_INTEGRATION_TESTING = IntegrationTesting(
    bases=(GAIPA_BACKEND_FIXTURE,),
    name='GaipaBackendLayer:IntegrationTesting',
)


GAIPA_BACKEND_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(GAIPA_BACKEND_FIXTURE,),
    name='GaipaBackendLayer:FunctionalTesting',
)


GAIPA_BACKEND_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        GAIPA_BACKEND_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='GaipaBackendLayer:AcceptanceTesting',
)
