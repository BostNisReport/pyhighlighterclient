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


class TrainingRun(object):
    """
      all functions of TrainingRun schema
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

    def create_training_run(self, research_plan_id, experiment_id, model_id, project_id, image_queue_id, name, source_code_url,
                            source_code_commit_hash, started_at, finished_at, model_implementation_file_path, training_logs_file_path):
        """
            create the training run. but research_plan_id and experiment_id, model_id, project_id, image_queue_id, name are required.
        :param research_plan_id:
        :param experiment_id:
        :param model_id:
        :param project_id:
        :param image_queue_id:
        :param name:
        :param source_code_url:
        :param source_code_commit_hash:
        :param started_at:
        :param finished_at:
        :param model_implementation_file_path:
        :param training_logs_file_path:
        """
        if (research_plan_id is None or research_plan_id == '' or research_plan_id == 0) or \
                (experiment_id is None or experiment_id == '' or experiment_id == 0) or \
                (model_id is None or model_id == '' or model_id == 0) or \
                (project_id is None or project_id == '' or project_id == 0) or \
                (image_queue_id is None or image_queue_id == '' or image_queue_id == 0) or \
                (name is None or name == ''):
            raise Exception('research_plan_id and experiment_id, model_id, project_id, image_queue_id, name are required.')

        modelimplementationfiledata = None
        if model_implementation_file_path is not None and model_implementation_file_path != '':
            modelimplementationfiledata = self.__upload_a_file_to_s3_using_presigned_url(model_implementation_file_path)
            if modelimplementationfiledata is None:
                # failed in upload file to s3 bucket
                raise Exception('failed in upload a file to s3 using presigned url.')

        traininglogsfiledata = None
        if training_logs_file_path is not None and training_logs_file_path != '':
            traininglogsfiledata = self.__upload_a_file_to_s3_using_presigned_url(training_logs_file_path)
            if traininglogsfiledata is None:
                # failed in upload file to s3 bucket
                raise Exception('failed in upload a file to s3 using presigned url.')

        op = Operation(silverpond_schema.Mutation)
        parent = op.create_training_run(research_plan_id=research_plan_id,
                                        experiment_id=experiment_id,
                                        model_id=model_id,
                                        project_id=project_id,
                                        image_queue_id=image_queue_id,
                                        name=name,
                                        source_code_url=source_code_url,
                                        source_code_commit_hash=source_code_commit_hash,
                                        started_at=started_at,
                                        finished_at=finished_at,
                                        model_implementation_file_data=modelimplementationfiledata,  # ShrineFileType
                                        training_logs_file_data=traininglogsfiledata  # ShrineFileType
                                        )

        # Field Set
        parent.errors()
        trainingrun = parent.training_run()
        fieldset_training_runs(trainingrun)

        ql_endpoint = HTTPEndpoint(self.GRAPHQL_API_ENDPOINT, self.headers)
        data = ql_endpoint(op)
        if data.get('errors') is not None:
            raise Exception(data.get('errors')[0]['message'])
        obj = op + data
        return obj.create_training_run.training_run