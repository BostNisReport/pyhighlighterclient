# coding=utf-8
__author__ = 'Mykhailo'

import os
from pathlib import Path
from dotenv import load_dotenv
import requests
import mimetypes

from sgqlc.endpoint.http import HTTPEndpoint as HTTPEndpoint
import logging
from .schema.silverpond_schema import silverpond_schema
from sgqlc.operation import Operation

from .fieldset_functions import *


class ExperimentComment(object):
    """
      all functions of experimentComment schema
    """
    logger = logging.getLogger('silverpond')

    def __init__(self, apitoken=None, apiurl=None, presignedurl=None):
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

        if presignedurl is None:
            self.PRESIGNED_GET_URL = os.getenv("PRESIGNED_GET_URL")
        else:
            self.PRESIGNED_GET_URL = presignedurl

        if self.GRAPHQL_API_TOKEN is None:
            raise Exception('API TOKEN is not validate.')
        if self.GRAPHQL_API_ENDPOINT is None:
            raise Exception('API URL is not validate.')
        if self.PRESIGNED_GET_URL is None:
            raise Exception('PRESIGNED S3 URL is not validate.')

        self.headers = {'Authorization': 'Token ' + self.GRAPHQL_API_TOKEN, 'Content-Type': 'application/json'}
        pass

    def __get_s3_presigned_url(self):
        r = requests.get(url=self.PRESIGNED_GET_URL, headers=self.headers)
        jsondata = r.json()
        return jsondata

    def __upload_a_file_to_s3_using_presigned_url(self, filepath):
        jsonpresigned = self.__get_s3_presigned_url()
        files = {'file': open(filepath, 'rb')}
        values = {
            'key': jsonpresigned['fields']['key'],
            'policy': jsonpresigned['fields']['policy'],
            'x-amz-credential': jsonpresigned['fields']['x-amz-credential'],
            'x-amz-algorithm': jsonpresigned['fields']['x-amz-algorithm'],
            'x-amz-date': jsonpresigned['fields']['x-amz-date'],
            'x-amz-signature': jsonpresigned['fields']['x-amz-signature']
        }
        response = requests.post(jsonpresigned['url'], files=files, data=values)
        if (200 <= response.status_code) and (response.status_code <= 299):
            return {
                'id': jsonpresigned['fields']['key'].split('/')[1],
                'storage': jsonpresigned['fields']['key'].split('/')[0],
                'metadata': {
                    'size': os.stat(filepath).st_size,
                    'filename': os.path.basename(filepath),
                    'mime_type': mimetypes.MimeTypes().guess_type(filepath)[0]
                }
            }
        # failed in uploading...
        return None

    def create_experiment_comment(self, research_plan_id, experiment_id, comment, attach_file_path):
        """
            create the experimentComment. but research_plan_id and experiment_id are required.
        :param research_plan_id:
        :param experiment_id:
        :param comment:
        :param attach_file_path:
        """
        if (research_plan_id is None or research_plan_id == '' or research_plan_id == 0) or \
                (experiment_id is None or experiment_id == '' or experiment_id == 0):
            raise Exception('research_plan_id and experiment_id are required.')

        op = Operation(silverpond_schema.Mutation)
        if attach_file_path is None or attach_file_path == '':
            parent = op.create_experiment_comment(research_plan_id=research_plan_id,
                                                  experiment_id=experiment_id,
                                                  comment=comment)
        else:
            attachmentdata = self.__upload_a_file_to_s3_using_presigned_url(attach_file_path)
            if attachmentdata is None:
                # failed in upload file to s3 bucket
                raise Exception('failed in upload a file to s3 using presigned url.')
            parent = op.create_experiment_comment(research_plan_id=research_plan_id,
                                                  experiment_id=experiment_id,
                                                  comment=comment,
                                                  attachment_data=attachmentdata)

        # Field Set
        parent.errors()
        experimentcomment = parent.experiment_comment()
        fieldset_experiment_comments(experimentcomment)

        ql_endpoint = HTTPEndpoint(self.GRAPHQL_API_ENDPOINT, self.headers)
        data = ql_endpoint(op)
        if data.get('errors') is not None:
            raise Exception(data.get('errors')[0]['message'])
        obj = op + data
        return obj.create_experiment_comment.experiment_comment

