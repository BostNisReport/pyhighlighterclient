__author__ = 'Mykhailo'

from pyhighlighterclient import Experiments, ExperimentResult, ExperimentComment, TrainingRun
from pprint import pprint

"""
    examples - Get All Data, Find Data, Create / Update the experiments
"""
experiments = Experiments(apitoken='c5c37a60fed25025f6501351e8aba08603306177117da46d97e38531ae11d463', apiurl='https://staging.highlighter.ai/graphql')

print('-------------------- get_all_experiments Test --------------------')
result1 = experiments.get_all_experiments()
print('-------------------- find_experiment_by_id(5) Test --------------------')
result2 = experiments.find_experiment_by_id("4")

print('-------------------- create_experiment Test --------------------')
result3 = experiments.create_experiment(research_plan_id="5",
                                     title="title1234",
                                     description="desc1234",
                                     assigned_to_id=85,
                                     observation="observation1234",
                                     hypothesis="hypothesis1234",
                                     conclusion="conclusion1234",
                                     notes="notes1234",
                                     effort_estimated=12.34,
                                     effort_actual=34.12)

print('-------------------- update_experimentTest --------------------')
result4 = experiments.update_experiment(id="35",
                                     research_plan_id="5",
                                     title="title4321",
                                     description="desc4321",
                                     assigned_to_id=85,
                                     observation="observation4321",
                                     hypothesis="hypothesis14321",
                                     conclusion="conclusion4321",
                                     notes="notes43321",
                                     effort_estimated=34.12,
                                     effort_actual=12.12)

"""
    examples - Create / Update the experiment result
"""
experimentresult = ExperimentResult(apitoken='c5c37a60fed25025f6501351e8aba08603306177117da46d97e38531ae11d463', apiurl='https://staging.highlighter.ai/graphql')
result5 = experimentresult.create_experiment_result(research_plan_id="3", experiment_id="4", research_plan_metric_id="6", object_class_id=1, occured_at="2019-05-28T00:00:00+10:00", result=0.1)
result6 = experimentresult.update_experiment_result(id='4', research_plan_id="3", experiment_id="4", research_plan_metric_id="6", object_class_id=2, occured_at="2019-05-28T00:00:00+10:00", result=0.2)

"""
    examples - Create the experiment comment
"""
experimentcomment = ExperimentComment(apitoken='c5c37a60fed25025f6501351e8aba08603306177117da46d97e38531ae11d463', apiurl='https://staging.highlighter.ai/graphql', presignedurl='https://staging.highlighter.ai/presign')
result7 = experimentcomment.create_experiment_comment(research_plan_id="3", experiment_id="4", comment="asdqwe", attach_file_path=None)
result8 = experimentcomment.create_experiment_comment(research_plan_id="3", experiment_id="4", comment="dfasdfas dfasdfwer wer", attach_file_path="E:\\foo.png")

"""
    examples - Create the Training Run
"""
trainingrun = TrainingRun(apitoken='c5c37a60fed25025f6501351e8aba08603306177117da46d97e38531ae11d463', apiurl='https://staging.highlighter.ai/graphql', presignedurl='https://staging.highlighter.ai/presign')
result9 = trainingrun.create_training_run(research_plan_id="3", experiment_id="4", model_id="8", project_id="68", image_queue_id="159", name="Test Training Run", source_code_url="sourceCodeUrl", source_code_commit_hash="sourceCodeCommitHash", started_at="2019-05-23T00:00:00+10:00", finished_at="2019-05-29T00:00:00+10:00", model_implementation_file_path="E:\\foo.png", training_logs_file_path="E:\\test.txt")