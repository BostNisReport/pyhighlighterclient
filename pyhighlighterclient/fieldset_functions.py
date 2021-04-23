# coding=utf-8
__author__ = 'Mykhailo'

def fieldset_research_plan(objparent):
    """

    :param objparent:
    """
    objparent.id()
    objparent.account_id()
    objparent.assigned_to_id()
    objparent.created_at()
    objparent.created_by_id()
    objparent.description()
    objparent.evaluation_process()
    objparent.objective()
    objparent.title()
    objparent.updated_at()
    # experiments
    # research_plan_metrics

def fieldset_experiment(objparent):
    """

    :param objparent:
    """
    objparent.id()
    objparent.assigned_to_id()
    objparent.conclusion()
    objparent.created_at()
    objparent.description()
    # objparent.due_on() # failed this field
    objparent.effort_actual()
    objparent.effort_estimated()
    objparent.hypothesis()
    objparent.notes()
    objparent.observation()
    # objparent.started_on() # failed this field
    objparent.title()
    objparent.updated_at()
    # research_plan
    # experiment_comments
    # experiment_results
    # training_runs
    # research_plan

def fieldset_research_plan_metrics(objparent):
    """

    :param objparent:
    """
    objparent.id()
    objparent.code()
    objparent.created_at()
    objparent.description()
    objparent.name()
    objparent.iou()
    objparent.weighted()
    objparent.object_class_id()
    objparent.updated_at()
    # research_plan

def fieldset_experiment_comments(objparent):
    """

    :param objparent:
    """
    objparent.id()
    objparent.attachment_url()
    objparent.comment()
    objparent.created_at()
    objparent.created_by_id()
    objparent.updated_at()
    # experiment

def fieldset_experiment_results(objparent):
    """

    :param objparent:
    """
    objparent.id()
    objparent.created_at()
    objparent.occured_at()
    objparent.result()
    objparent.updated_at()
    objparent.object_class_id()
    fieldset_research_plan_metrics(objparent.research_plan_metric()) # research_plan_metric
    # experiment

def fieldset_training_runs(objparent):
    """

    :param objparent:
    """
    objparent.id()
    objparent.created_at()
    # objparent.finished_at()
    objparent.image_queue_id()
    objparent.model_id()
    objparent.name()
    objparent.project_id()
    objparent.requested_by_id()
    objparent.source_code_commit_hash()
    objparent.source_code_url()
    # objparent.started_at()
    objparent.updated_at()
    objparent.model_implementation_file_url()
    objparent.training_logs_file_url()
    # experiment
