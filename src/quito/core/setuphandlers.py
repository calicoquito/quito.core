# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from plone import api
from mattermost import ploneCreateTeam
from mattermost import ploneDeleteTeam
from mattermost import ploneConfigMattermost
from mattermost import  ploneAddAdmin




@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'quito.core:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    ploneConfigMattermost()
    portal = api.portal.get()
    ploneCreateTeam(portal)
    ploneAddAdmin()


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
    portal = api.portal.get()
    ploneDeleteTeam(portal)