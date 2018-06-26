# -*- coding: utf-8 -*-
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

import logging


PACKAGE_NAME = 'gaipa.backend'
PROFILE_ID = 'profile-gaipa.backend:default'


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'gaipa.backend:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    logger = logging.getLogger(PACKAGE_NAME)
    portal = api.portal.get()
    ptypes = portal.portal_types
    # pub_quellen = api.content.get('/publikationen-quellen')
    if 'app' not in portal.objectIds():
        obj_id = ptypes.constructContent(
            'GaipaContent',
            portal,
            'app',
            title=u'gaipa - global farmer empowerment community',
        )
        app = portal[obj_id]
        logger.info('Added {0} database'.format(
            app.absolute_url_path()))
    if 'cards' not in app.objectIds():
        obj_id = ptypes.constructContent(
            'NavAssistantCards',
            app,
            'cards',
            title=u'Navigation Assistant Cards',
        )
        cards = portal[obj_id]
        logger.info('Added {0} database'.format(
            cards.absolute_url_path()))
    if 'solutions' not in app.objectIds():
        obj_id = ptypes.constructContent(
            'SolutionArticles',
            app,
            'solutions',
            title=u'Solution Articles',
        )
        solutions = portal[obj_id]
        logger.info('Added {0} database'.format(
            solutions.absolute_url_path()))

def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
