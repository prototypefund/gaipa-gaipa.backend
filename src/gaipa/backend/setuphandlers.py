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
    app = api.content.get('/app')
    if 'card' not in app.objectIds():
        obj_id = ptypes.constructContent(
            'NavAssistantCards',
            app,
            'card',
            title=u'Navigation Assistant Cards',
        )
        cards = app[obj_id]
        logger.info('Added {0} database'.format(
            cards.absolute_url_path()))
    if 'solution' not in app.objectIds():
        obj_id = ptypes.constructContent(
            'SolutionArticles',
            app,
            'solution',
            title=u'Solution Articles',
        )
        solutions = app[obj_id]
        logger.info('Added {0} database'.format(
            solutions.absolute_url_path()))
    if 'service' not in app.objectIds():
        obj_id = ptypes.constructContent(
            'SolutionServices',
            app,
            'service',
            title=u'Solution Services',
        )
        service = app[obj_id]
        logger.info('Added {0} database'.format(
            service.absolute_url_path()))
    if 'provider' not in app.objectIds():
        obj_id = ptypes.constructContent(
            'SolutionProvider',
            app,
            'provider',
            title=u'Solution Provider',
        )
        provider = app[obj_id]
        logger.info('Added {0} database'.format(
            provider.absolute_url_path()))

    wanted_indexes = (
        ('solution_category', 'FieldIndex'),
    )
    add_catalog_indexes(context, logger=logger, wanted=wanted_indexes)


def add_catalog_indexes(context, logger=None, wanted=None):
    """Method to add our wanted indexes to the portal_catalog.
    """
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger(PACKAGE_NAME)

    # Run the catalog.xml step as that may have defined new metadata
    # columns.  We could instead add <depends name="catalog"/> to
    # the registration of our import step in zcml, but doing it in
    # code makes this method usable as upgrade step as well.  Note that
    # this silently does nothing when there is no catalog.xml, so it
    # is quite safe.
    setup = api.portal.get_tool('portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'catalog')

    catalog = api.portal.get_tool('portal_catalog')
    indexes = catalog.indexes()
    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info('Added %s for field %s.', meta_type, name)
    if len(indexables) > 0:
        logger.info('Indexing new indexes %s.', ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
