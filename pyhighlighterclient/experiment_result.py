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


class ExperimentResult(object):
    """
      all functions of ExpermentResult schema
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

    def create_experiment_result(self, research_plan_id, experiment_id, research_plan_metric_id, object_class_id, occured_at, result):
        """
            create the experimentResult. but all params are required
        :param research_plan_id:
        :param experiment_id:
        :param research_plan_metric_id:
        :param object_class_id:
        :param occured_at:
        :param result:
        """
        if (research_plan_id is None or research_plan_id == '' or research_plan_id == 0) or \
                (experiment_id is None or experiment_id == '' or experiment_id == 0) or \
                (research_plan_metric_id is None or research_plan_metric_id == '' or research_plan_metric_id == 0) or \
                (occured_at is None or occured_at == '') or \
                (result is None or result == ''):
            raise Exception('all params are required')

        op = Operation(silverpond_schema.Mutation)
        parent = op.create_experiment_result(research_plan_id=research_plan_id,
                                             experiment_id=experiment_id,
                                             research_plan_metric_id=research_plan_metric_id,
                                             object_class_id=object_class_id,
                                             occured_at=occured_at,
                                             result=result
                                             )

        # Field Set
        parent.errors()
        experimentresult = parent.experiment_result()
        fieldset_experiment_results(experimentresult)

        ql_endpoint = HTTPEndpoint(self.GRAPHQL_API_ENDPOINT, self.headers)
        data = ql_endpoint(op)
        obj = op + data
        if len(obj.create_experiment_result.errors) > 0:
            raise Exception(obj.create_experiment_result.errors[0])
        return obj.create_experiment_result.experiment_result

    def update_experiment_result(self, id, research_plan_id, experiment_id, research_plan_metric_id, object_class_id, occured_at, result):
        """
            update the experimentResult. but all params are required
        :param id:
        :param research_plan_id:
        :param experiment_id:
        :param research_plan_metric_id:
        :param object_class_id:
        :param occured_at:
        :param result:
        """
        if (research_plan_id is None or research_plan_id == '' or research_plan_id == 0) or \
                (experiment_id is None or experiment_id == '' or experiment_id == 0) or \
                (research_plan_metric_id is None or research_plan_metric_id == '' or research_plan_metric_id == 0) or \
                (occured_at is None or occured_at == '') or \
                (result is None or result == '') or \
                (id is None or id == '' or id == 0):
            raise Exception('all params are required')

        op = Operation(silverpond_schema.Mutation)
        parent = op.update_experiment_result(id=id,
                                             research_plan_id=research_plan_id,
                                             experiment_id=experiment_id,
                                             research_plan_metric_id=research_plan_metric_id,
                                             object_class_id=object_class_id,
                                             occured_at=occured_at,
                                             result=result
                                             )

        # Field Set
        parent.errors()
        experimentresult = parent.experiment_result()
        fieldset_experiment_results(experimentresult)

        ql_endpoint = HTTPEndpoint(self.GRAPHQL_API_ENDPOINT, self.headers)
        data = ql_endpoint(op)
        obj = op + data
        if len(obj.update_experiment_result.errors) > 0:
            raise Exception(obj.update_experiment_result.errors[0])
        return obj.update_experiment_result.experiment_result