# -*- coding: utf-8 -*-
from datetime import date
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from zope import schema
from zope.interface import Interface
import os 


class IControlPanel(Interface):

    mattermost_host = schema.URI(
        title=u'Mattermost Host',
        description = u'url for the mattermost host',
        required=True,
        default= os.environ['MATTERMOST_HOST']
    )

    use_mattermost = schema.Bool(
        title=u'Mattermost Chat',
        description=u'enable to use mattermost',
        default=True,
        required=True,
    )


class ControlPanelForm(RegistryEditForm):
    schema = IControlPanel
    schema_prefix = "quito.core"
    label = u'Quito Core Settings'


ControlPanelView = layout.wrap_form(
    ControlPanelForm, ControlPanelFormWrapper)