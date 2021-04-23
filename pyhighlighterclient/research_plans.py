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


class ResearchPlans(object):
    """
      all functions of researchPlans schema
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

    def get_all_research_plans(self):
        """
            get all research plans
        """
        op = Operation(silverpond_schema.Query)
        parent = op.research_plans()

        # Field set
        fieldset_research_plan(parent)
        fieldset_experiment(parent.experiments())
        fieldset_research_plan_metrics(parent.research_plan_metrics())

        ql_endpoint = HTTPEndpoint(self.GRAPHQL_API_ENDPOINT, self.headers)
        data = ql_endpoint(op)
        if data.get('errors') is not None:
            raise Exception(data.get('errors')[0]['message'])

        obj = op + data
        return obj.research_plans

    def find_research_plan_by_id(self, id):
        """
            get research plan by id
        :param id: research plan id
        """
        op = Operation(silverpond_schema.Query)
        parent = op.research_plan(id=id)

        # Field set
        fieldset_research_plan(parent)
        fieldset_experiment(parent.experiments())
        fieldset_research_plan_metrics(parent.research_plan_metrics())

        ql_endpoint = HTTPEndpoint(self.GRAPHQL_API_ENDPOINT, self.headers)
        data = ql_endpoint(op)
        if data.get('errors') is not None:
            raise Exception(data.get('errors')[0]['message'])

        obj = op + data
        return obj.research_plan

    def create_research_plan(self, title, description, assigned_to_id, objective, evaluation_process):
        """
            create the research plan. but title and assigned_to_id are required.
        :param title:
        :param description:
        :param assigned_to_id:
        :param objective:
        :param evaluation_process:
        """
        if (title is None or title == '') or \
                (assigned_to_id is None or assigned_to_id == '' or assigned_to_id == 0):
            raise Exception('title and assigned_to_id are required.')

        op = Operation(silverpond_schema.Mutation)
        parent = op.create_research_plan(title=title, description=description, assigned_to_id=assigned_to_id,
                                         objective=objective, evaluation_process=evaluation_process)

        # Field Set
        parent.errors()
        researchplan = parent.research_plan()
        fieldset_research_plan(researchplan)
        fieldset_experiment(researchplan.experiments())
        fieldset_research_plan_metrics(researchplan.research_plan_metrics())

        ql_endpoint = HTTPEndpoint(self.GRAPHQL_API_ENDPOINT, self.headers)
        data = ql_endpoint(op)
        obj = op + data
        if len(obj.create_research_plan.errors) > 0:
            raise Exception(obj.create_research_plan.errors[0])
        return obj.create_research_plan.research_plan

    def update_research_plan(self, id, title, description, assigned_to_id, objective, evaluation_process):
        """
            update the research plan. but id, title, assigned_to_id are required.
        :param id:
        :param title:
        :param description:
        :param assigned_to_id:
        :param objective:
        :param evaluation_process:
        """
        if (id is None or id == '' or id == 0) or \
                (title is None or title == '') or \
                (assigned_to_id is None or assigned_to_id == '' or assigned_to_id == 0):
            raise Exception('id and title, assigned_to_id are required.')

        op = Operation(silverpond_schema.Mutation)
        parent = op.update_research_plan(id=id, title=title, description=description, assigned_to_id=assigned_to_id,
                                         objective=objective, evaluation_process=evaluation_process)

        # Field Set
        parent.errors()
        researchplan = parent.research_plan()
        fieldset_research_plan(researchplan)
        fieldset_experiment(researchplan.experiments())
        fieldset_research_plan_metrics(researchplan.research_plan_metrics())

        ql_endpoint = HTTPEndpoint(self.GRAPHQL_API_ENDPOINT, self.headers)
        data = ql_endpoint(op)
        obj = op + data
        if len(obj.update_research_plan.errors) > 0:
            raise Exception(obj.update_research_plan.errors[0])
        return obj.update_research_plan.research_plan
