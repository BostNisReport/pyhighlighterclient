# coding=utf-8
__author__ = 'Mykhailo'

import os
from pathlib import Path
from dotenv import load_dotenv

from sgqlc.endpoint.http import HTTPEndpoint as HTTPEndpoint
import logging
from .schema.silverpond_schema import silverpond_schema
from sgqlc.operation import Operation

from .fieldset_functions import *


class ResearchPlanMetric(object):
    """
      all functions of ResearchPlanMetric schema
    """
    logger = logging.getLogger('silverpond')

    def __init__(self, apitoken=None, apiurl=None):
        env_path = Path('.') / '.env'
        load_dotenv(dotenv_path=env_path)

        if apitoken is None:
            self.GRAPHQL_API_TOKEN = os.getenv("GRAPHQL_API_TOKEN")
        else:
            self.GRAPHQL_API_TOKEN = apitoken

        if apiurl is None:
            self.GRAPHQL_API_ENDPOINT = os.getenv("GRAPHQL_API_ENDPOINT")
        else:
            self.GRAPHQL_API_ENDPOINT = apiurl

        if self.GRAPHQL_API_TOKEN is None:
            raise Exception('API TOKEN is not validate.')
        if self.GRAPHQL_API_ENDPOINT is None:
            raise Exception('API URL is not validate.')

        self.headers = {'Authorization': 'Token ' + self.GRAPHQL_API_TOKEN, 'Content-Type': 'application/json'}
        pass

    def create_research_plan_metric(self, research_plan_id, code, name, description, iou, weighted, object_class_id):
        """
            create the researchPlanMetric. but research_plan_id and code, name are required.
        :param research_plan_id:
        :param code:
        :param name:
        :param description:
        :param iou:
        :param weighted:
        :param object_class_id:
        """
        if (research_plan_id is None or research_plan_id == '' or research_plan_id == 0) or \
                (code is None or code == '') or \
                (name is None or name == ''):
            raise Exception('research_plan_id and code, name are required.')

        op = Operation(silverpond_schema.Mutation)
        parent = op.create_research_plan_metric(research_plan_id=research_plan_id,
                                                code=code,
                                                name=name,
                                                description=description,
                                                iou=iou,
                                                weighted=weighted,
                                                object_class_id=object_class_id
                                                )

        # Field Set
        parent.errors()
        researchplanmetric = parent.research_plan_metric()
        fieldset_research_plan_metrics(researchplanmetric)

        ql_endpoint = HTTPEndpoint(self.GRAPHQL_API_ENDPOINT, self.headers)
        data = ql_endpoint(op)
        obj = op + data
        if len(obj.create_research_plan_metric.errors) > 0:
            raise Exception(obj.create_research_plan_metric.errors[0])
        return obj.create_research_plan_metric.research_plan_metric

    def update_research_plan_metric(self, id, research_plan_id, code, name, description, iou, weighted, object_class_id):
        """
            update the experiment. but id, research_plan_id, code, name are required.
        :param id:
        :param research_plan_id:
        :param code:
        :param name:
        :param description:
        :param iou:
        :param weighted:
        :param object_class_id:
        """
        if (id is None or id == '' or id == 0) or \
                (research_plan_id is None or research_plan_id == '' or research_plan_id == 0) or \
                (code is None or code == '') or \
                (name is None or name == ''):
            raise Exception('id and research_plan_id, code, name are required.')

        op = Operation(silverpond_schema.Mutation)
        parent = op.update_research_plan_metric(id=id,
                                                research_plan_id=research_plan_id,
                                                code=code,
                                                name=name,
                                                description=description,
                                                iou=iou,
                                                weighted=weighted,
                                                object_class_id=object_class_id
                                                )

        # Field Set
        parent.errors()
        researchplanmetric = parent.research_plan_metric()
        fieldset_research_plan_metrics(researchplanmetric)

        ql_endpoint = HTTPEndpoint(self.GRAPHQL_API_ENDPOINT, self.headers)
        data = ql_endpoint(op)
        obj = op + data
        if len(obj.update_research_plan_metric.errors) > 0:
            raise Exception(obj.update_research_plan_metric.errors[0])
        return obj.update_research_plan_metric.research_plan_metric
