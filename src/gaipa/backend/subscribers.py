# -*- coding: utf-8 -*-
from plone import api

import logging


logger = logging.getLogger("gaipa.backend.subscribers")


def create_service_and_solution_containers(obj, event):
    """
    """
    portal = api.portal.get()
    ptypes = portal.portal_types

    import pdb;pdb.set_trace()
    if 'service' not in obj.objectIds():
        obj_id = ptypes.constructContent(
            'SolutionServices',
            obj,
            'service',
            title=u'Solution Services',
        )
        service = obj[obj_id]
        logger.info('Added {0} container to SolutionProvider: {1}'.format(
            service.id,
            obj.absolute_url_path(),
            )
        )
    if 'solution' not in obj.objectIds():
        obj_id = ptypes.constructContent(
            'SolutionArticles',
            obj,
            'solution',
            title=u'Solution Articles',
        )
        solution = obj[obj_id]
        logger.info('Added {0} container to SolutionProvider: {1}'.format(
            solution.id,
            obj.absolute_url_path(),
            )
        )

