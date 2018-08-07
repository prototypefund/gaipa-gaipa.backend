# -*- coding: utf-8 -*-
from plone import api
from plone.app.upgrade.utils import loadMigrationProfile

import logging


logger = logging.getLogger('gaipa.backend.upgrades')


def reload_gs_profile(context):
    loadMigrationProfile(
        context,
        'profile-gaipa.backend:default',
    )


def upgrade_category_indexes(context):
    wanted = (
        ('solution_category', 'KeywordIndex'),
        ('crop_category', 'KeywordIndex'),
    )
    catalog = api.portal.get_tool('portal_catalog')
    indexes = catalog.indexes()
    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            continue
        for idx in catalog.index_objects():
            if not idx.id == name:
                continue
            if idx.meta_type == meta_type:
                continue
            catalog.delIndex(name)
            logger.info(
                'Deleted old %s index for field %s.',
                idx.meta_type,
                name,
            )
            catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info('Added %s for field %s.', meta_type, name)
    if len(indexables) > 0:
        logger.info('Indexing upgraded indexes %s.', ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)
