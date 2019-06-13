# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import quito.core


class QuitoCoreLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=quito.core)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'quito.core:default')


QUITO_CORE_FIXTURE = QuitoCoreLayer()


QUITO_CORE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(QUITO_CORE_FIXTURE,),
    name='QuitoCoreLayer:IntegrationTesting',
)


QUITO_CORE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(QUITO_CORE_FIXTURE,),
    name='QuitoCoreLayer:FunctionalTesting',
)


QUITO_CORE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        QUITO_CORE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='QuitoCoreLayer:AcceptanceTesting',
)
