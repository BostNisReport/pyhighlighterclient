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


class Experiments(object):
    """
      all functions of Experments schema
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

    def get_all_experiments(self):
        """
            get all experiments
        """
        op = Operation(silverpond_schema.Query)
        parent = op.experiments()

        # Field set
        fieldset_experiment(parent)
        fieldset_research_plan(parent.research_plan())
        fieldset_experiment_comments(parent.experiment_comments())
        fieldset_experiment_results(parent.experiment_results())
        fieldset_training_runs(parent.training_runs())

        ql_endpoint = HTTPEndpoint(self.GRAPHQL_API_ENDPOINT, self.headers)
        data = ql_endpoint(op)
        if data.get('errors') is not None:
            raise Exception(data.get('errors')[0]['message'])

        obj = op + data
        return obj.experiments

    def find_experiment_by_id(self, id):
        """
            get experiment by id
        :param id:
        """
        op = Operation(silverpond_schema.Query)
        parent = op.experiment(id=id)

        # Field set
        fieldset_experiment(parent)
        fieldset_research_plan(parent.research_plan())
        fieldset_experiment_comments(parent.experiment_comments())
        fieldset_experiment_results(parent.experiment_results())
        fieldset_training_runs(parent.training_runs())

        ql_endpoint = HTTPEndpoint(self.GRAPHQL_API_ENDPOINT, self.headers)
        data = ql_endpoint(op)
        if data.get('errors') is not None:
            raise Exception(data.get('errors')[0]['message'])

        obj = op + data
        return obj.experiment

    def create_experiment(self, research_plan_id, title, description, assigned_to_id, observation, hypothesis,
                          conclusion, notes, effort_estimated, effort_actual):
        """
            create the experiment. but research_plan_id and title, assigned_to_id is required.
        :param research_plan_id:
        :param title:
        :param description:
        :param assigned_to_id:
        :param observation:
        :param hypothesis:
        :param conclusion:
        :param notes:
        :param effort_estimated:
        :param effort_actual:
        """
        if (research_plan_id is None or research_plan_id == '' or research_plan_id == 0) or \
                (title is None or title == '') or \
                (assigned_to_id is None or assigned_to_id == '' or assigned_to_id == 0):
            raise Exception('research_plan_id and title, assigned_to_id are required.')

        op = Operation(silverpond_schema.Mutation)
        parent = op.create_experiment(research_plan_id=research_plan_id,
                                      title=title,
                                      description=description,
                                      assigned_to_id=assigned_to_id,
                                      observation=observation,
                                      hypothesis=hypothesis,
                                      conclusion=conclusion,
                                      notes=notes,
                                      effort_estimated=effort_estimated,
                                      effort_actual=effort_actual
                                      )

        # Field Set
        parent.errors()
        experiment = parent.experiment()
        fieldset_experiment(experiment)

        ql_endpoint = HTTPEndpoint(self.GRAPHQL_API_ENDPOINT, self.headers)
        data = ql_endpoint(op)
        obj = op + data
        if len(obj.create_experiment.errors) > 0:
            raise Exception(obj.create_experiment.errors[0])
        return obj.create_experiment.experiment

    def update_experiment(self, id, research_plan_id, title, description, assigned_to_id, observation, hypothesis,
                          conclusion, notes, effort_estimated, effort_actual):
        """
            update the experiment. but id and research_plan_id, title, assigned_to_id are required.
        :param id:
        :param research_plan_id:
        :param title:
        :param description:
        :param assigned_to_id:
        :param observation:
        :param hypothesis:
        :param conclusion:
        :param notes:
        :param effort_estimated:
        :param effort_actual:
        """
        if (id is None or id == '' or id == 0) or \
                (research_plan_id is None or research_plan_id == '' or research_plan_id == 0) or \
                (title is None or title == '') or \
                (assigned_to_id is None or assigned_to_id == '' or assigned_to_id == 0):
            raise Exception('id and research_plan_id, title, assigned_to_id are required.')

        op = Operation(silverpond_schema.Mutation)
        parent = op.update_experiment(id=id,
                                      research_plan_id=research_plan_id,
                                      title=title,
                                      description=description,
                                      assigned_to_id=assigned_to_id,
                                      observation=observation,
                                      hypothesis=hypothesis,
                                      conclusion=conclusion,
                                      notes=notes,
                                      effort_estimated=effort_estimated,
                                      effort_actual=effort_actual
                                      )

        # Field Set
        parent.errors()
        experiment = parent.experiment()
        fieldset_experiment(experiment)

        ql_endpoint = HTTPEndpoint(self.GRAPHQL_API_ENDPOINT, self.headers)
        data = ql_endpoint(op)
        obj = op + data
        if len(obj.update_experiment.errors) > 0:
            raise Exception(obj.update_experiment.errors[0])
        return obj.update_experiment.experiment
