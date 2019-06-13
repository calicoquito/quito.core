##############################################################################
#
# Copyright (c) 2002 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################
""" Session managemnt product initialization
"""

# This is a file to define public API in the base namespace of the package.

from .interfaces import BrowserIdManagerErr  # NOQA: flake8: F401
from .interfaces import SessionDataManagerErr  # NOQA: flake8: F40


def commit(note):
    import transaction
    transaction.get().note(note)
    transaction.commit()


def install_browser_id_manager(app):
    if hasattr(app, 'browser_id_manager'):
        return

    from . import BrowserIdManager
    bid = BrowserIdManager.BrowserIdManager(
        'browser_id_manager',
        'Browser Id Manager',
    )
    app._setObject('browser_id_manager', bid)
    commit(u'Added browser_id_manager')


def install_session_data_manager(app):
    # Ensure that a session data manager exists
    if hasattr(app, 'session_data_manager'):
        return

    from . import SessionDataManager
    sdm = SessionDataManager.SessionDataManager(
        'session_data_manager',
        title='Session Data Manager',
        path='/temp_folder/session_data',
        requestName='SESSION',
    )
    app._setObject('session_data_manager', sdm)
    commit(u'Added session_data_manager')


def initialize(context):

    from . import BrowserIdManager
    from . import SessionDataManager

    context.registerClass(
        BrowserIdManager.BrowserIdManager,
        permission=BrowserIdManager.ADD_BROWSER_ID_MANAGER_PERM,
        constructors=(BrowserIdManager.constructBrowserIdManagerForm,
                      BrowserIdManager.constructBrowserIdManager))

    context.registerClass(
        SessionDataManager.SessionDataManager,
        permission=SessionDataManager.ADD_SESSION_DATAMANAGER_PERM,
        constructors=(SessionDataManager.constructSessionDataManagerForm,
                      SessionDataManager.constructSessionDataManager))

    # do module security declarations so folks can use some of the
    # module-level stuff in PythonScripts
    #
    # declare on behalf of Transience too, since ModuleSecurityInfo is too
    # stupid for me to declare in two places without overwriting one set
    # with the other. :-(
    from AccessControl import ModuleSecurityInfo
    security = ModuleSecurityInfo('Products')
    security.declarePublic('Sessions')  # NOQA: flake8: D001
    security.declarePublic('Transience')  # NOQA: flake8: D001

    security = ModuleSecurityInfo('Products.Sessions.interfaces')
    security.declareObjectPublic()
    security.setDefaultAccess('allow')

    security = ModuleSecurityInfo('Products.Transience')
    security.declarePublic('MaxTransientObjectsExceeded')  # NOQA: flake8: D001

    # BBB: for names which should be imported from Products.Sessions.interfaces
    security = ModuleSecurityInfo('Products.Sessions')
    security.declarePublic('BrowserIdManagerErr')  # NOQA: flake8: D001
    security.declarePublic('SessionDataManagerErr')  # NOQA: flake8: D001

    app = context.getApplication()  # new API added in Zope 4.0b5
    if app is not None:
        install_browser_id_manager(app)
        install_session_data_manager(app)
