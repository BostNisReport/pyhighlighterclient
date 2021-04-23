import sgqlc.types


silverpond_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

Float = sgqlc.types.Float

ID = sgqlc.types.ID

class ISO8601DateTime(sgqlc.types.Scalar):
    __schema__ = silverpond_schema


Int = sgqlc.types.Int

class ResearchPlanMetricCodeEnum(sgqlc.types.Enum):
    __schema__ = silverpond_schema
    __choices__ = ('Dice', 'mAP', 'MaAD', 'MeAD')


String = sgqlc.types.String


########################################################################
# Input Objects
########################################################################
class ShrineFileType(sgqlc.types.Input):
    __schema__ = silverpond_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    storage = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='storage')
    metadata = sgqlc.types.Field(sgqlc.types.non_null('ShrineMetadataType'), graphql_name='metadata')


class ShrineMetadataType(sgqlc.types.Input):
    __schema__ = silverpond_schema
    size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='size')
    filename = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='filename')
    mime_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mimeType')



########################################################################
# Output Objects and Interfaces
########################################################################
class CreateExperimentCommentPayload(sgqlc.types.Type):
    __schema__ = silverpond_schema
    errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='errors')
    experiment_comment = sgqlc.types.Field('ExperimentComment', graphql_name='experimentComment')


class CreateExperimentPayload(sgqlc.types.Type):
    __schema__ = silverpond_schema
    errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='errors')
    experiment = sgqlc.types.Field('Experiment', graphql_name='experiment')


class CreateExperimentResultPayload(sgqlc.types.Type):
    __schema__ = silverpond_schema
    errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='errors')
    experiment_result = sgqlc.types.Field('ExperimentResult', graphql_name='experimentResult')


class CreateResearchPlanMetricPayload(sgqlc.types.Type):
    __schema__ = silverpond_schema
    errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='errors')
    research_plan_metric = sgqlc.types.Field('ResearchPlanMetric', graphql_name='researchPlanMetric')


class CreateResearchPlanPayload(sgqlc.types.Type):
    __schema__ = silverpond_schema
    errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='errors')
    research_plan = sgqlc.types.Field('ResearchPlan', graphql_name='researchPlan')


class CreateTrainingRunPayload(sgqlc.types.Type):
    __schema__ = silverpond_schema
    errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='errors')
    training_run = sgqlc.types.Field('TrainingRun', graphql_name='trainingRun')


class Experiment(sgqlc.types.Type):
    __schema__ = silverpond_schema
    assigned_to_id = sgqlc.types.Field(Int, graphql_name='assignedToId')
    conclusion = sgqlc.types.Field(String, graphql_name='conclusion')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    due_on = sgqlc.types.Field(ISO8601DateTime, graphql_name='dueOn')
    effort_actual = sgqlc.types.Field(Float, graphql_name='effortActual')
    effort_estimated = sgqlc.types.Field(Float, graphql_name='effortEstimated')
    experiment_comments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ExperimentComment')), graphql_name='experimentComments')
    experiment_results = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ExperimentResult')), graphql_name='experimentResults')
    hypothesis = sgqlc.types.Field(String, graphql_name='hypothesis')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    observation = sgqlc.types.Field(String, graphql_name='observation')
    research_plan = sgqlc.types.Field(sgqlc.types.non_null('ResearchPlan'), graphql_name='researchPlan')
    started_on = sgqlc.types.Field(ISO8601DateTime, graphql_name='startedOn')
    title = sgqlc.types.Field(String, graphql_name='title')
    training_runs = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TrainingRun')), graphql_name='trainingRuns')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='updatedAt')


class ExperimentComment(sgqlc.types.Type):
    __schema__ = silverpond_schema
    attachment_url = sgqlc.types.Field(String, graphql_name='attachmentUrl')
    comment = sgqlc.types.Field(String, graphql_name='comment')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='createdAt')
    created_by_id = sgqlc.types.Field(Int, graphql_name='createdById')
    experiment = sgqlc.types.Field(sgqlc.types.non_null(Experiment), graphql_name='experiment')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='updatedAt')


class ExperimentResult(sgqlc.types.Type):
    __schema__ = silverpond_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='createdAt')
    experiment = sgqlc.types.Field(sgqlc.types.non_null(Experiment), graphql_name='experiment')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    object_class_id = sgqlc.types.Field(Int, graphql_name='objectClassId')
    occured_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='occuredAt')
    research_plan_metric = sgqlc.types.Field(sgqlc.types.non_null('ResearchPlanMetric'), graphql_name='researchPlanMetric')
    result = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='result')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='updatedAt')


class Mutation(sgqlc.types.Type):
    __schema__ = silverpond_schema
    create_experiment = sgqlc.types.Field(CreateExperimentPayload, graphql_name='createExperiment', args=sgqlc.types.ArgDict((
        ('research_plan_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='researchPlanId', default=None)),
        ('title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='title', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('assigned_to_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='assignedToId', default=None)),
        ('observation', sgqlc.types.Arg(String, graphql_name='observation', default=None)),
        ('hypothesis', sgqlc.types.Arg(String, graphql_name='hypothesis', default=None)),
        ('conclusion', sgqlc.types.Arg(String, graphql_name='conclusion', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
        ('due_on', sgqlc.types.Arg(ISO8601DateTime, graphql_name='dueOn', default=None)),
        ('started_on', sgqlc.types.Arg(ISO8601DateTime, graphql_name='startedOn', default=None)),
        ('effort_estimated', sgqlc.types.Arg(Float, graphql_name='effortEstimated', default=None)),
        ('effort_actual', sgqlc.types.Arg(Float, graphql_name='effortActual', default=None)),
))
    )
    create_experiment_comment = sgqlc.types.Field(CreateExperimentCommentPayload, graphql_name='createExperimentComment', args=sgqlc.types.ArgDict((
        ('research_plan_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='researchPlanId', default=None)),
        ('experiment_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='experimentId', default=None)),
        ('comment', sgqlc.types.Arg(String, graphql_name='comment', default=None)),
        ('attachment_data', sgqlc.types.Arg(ShrineFileType, graphql_name='attachmentData', default=None)),
))
    )
    create_experiment_result = sgqlc.types.Field(CreateExperimentResultPayload, graphql_name='createExperimentResult', args=sgqlc.types.ArgDict((
        ('research_plan_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='researchPlanId', default=None)),
        ('experiment_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='experimentId', default=None)),
        ('research_plan_metric_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='researchPlanMetricId', default=None)),
        ('occured_at', sgqlc.types.Arg(sgqlc.types.non_null(ISO8601DateTime), graphql_name='occuredAt', default=None)),
        ('result', sgqlc.types.Arg(sgqlc.types.non_null(Float), graphql_name='result', default=None)),
        ('object_class_id', sgqlc.types.Arg(Int, graphql_name='objectClassId', default=None)),
))
    )
    create_research_plan = sgqlc.types.Field(CreateResearchPlanPayload, graphql_name='createResearchPlan', args=sgqlc.types.ArgDict((
        ('title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='title', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('assigned_to_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='assignedToId', default=None)),
        ('objective', sgqlc.types.Arg(String, graphql_name='objective', default=None)),
        ('evaluation_process', sgqlc.types.Arg(String, graphql_name='evaluationProcess', default=None)),
))
    )
    create_research_plan_metric = sgqlc.types.Field(CreateResearchPlanMetricPayload, graphql_name='createResearchPlanMetric', args=sgqlc.types.ArgDict((
        ('research_plan_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='researchPlanId', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(ResearchPlanMetricCodeEnum), graphql_name='code', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('iou', sgqlc.types.Arg(Float, graphql_name='iou', default=None)),
        ('weighted', sgqlc.types.Arg(Boolean, graphql_name='weighted', default=None)),
        ('object_class_id', sgqlc.types.Arg(Int, graphql_name='objectClassId', default=None)),
))
    )
    create_training_run = sgqlc.types.Field(CreateTrainingRunPayload, graphql_name='createTrainingRun', args=sgqlc.types.ArgDict((
        ('research_plan_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='researchPlanId', default=None)),
        ('experiment_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='experimentId', default=None)),
        ('model_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='modelId', default=None)),
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='projectId', default=None)),
        ('image_queue_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='imageQueueId', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('source_code_url', sgqlc.types.Arg(String, graphql_name='sourceCodeUrl', default=None)),
        ('source_code_commit_hash', sgqlc.types.Arg(String, graphql_name='sourceCodeCommitHash', default=None)),
        ('started_at', sgqlc.types.Arg(ISO8601DateTime, graphql_name='startedAt', default=None)),
        ('finished_at', sgqlc.types.Arg(ISO8601DateTime, graphql_name='finishedAt', default=None)),
        ('model_implementation_file_data', sgqlc.types.Arg(ShrineFileType, graphql_name='modelImplementationFileData', default=None)),
        ('training_logs_file_data', sgqlc.types.Arg(ShrineFileType, graphql_name='trainingLogsFileData', default=None)),
))
    )
    update_experiment = sgqlc.types.Field('UpdateExperimentPayload', graphql_name='updateExperiment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('research_plan_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='researchPlanId', default=None)),
        ('title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='title', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('assigned_to_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='assignedToId', default=None)),
        ('observation', sgqlc.types.Arg(String, graphql_name='observation', default=None)),
        ('hypothesis', sgqlc.types.Arg(String, graphql_name='hypothesis', default=None)),
        ('conclusion', sgqlc.types.Arg(String, graphql_name='conclusion', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
        ('due_on', sgqlc.types.Arg(ISO8601DateTime, graphql_name='dueOn', default=None)),
        ('started_on', sgqlc.types.Arg(ISO8601DateTime, graphql_name='startedOn', default=None)),
        ('effort_estimated', sgqlc.types.Arg(Float, graphql_name='effortEstimated', default=None)),
        ('effort_actual', sgqlc.types.Arg(Float, graphql_name='effortActual', default=None)),
))
    )
    update_experiment_result = sgqlc.types.Field('UpdateExperimentResultPayload', graphql_name='updateExperimentResult', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('research_plan_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='researchPlanId', default=None)),
        ('experiment_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='experimentId', default=None)),
        ('research_plan_metric_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='researchPlanMetricId', default=None)),
        ('occured_at', sgqlc.types.Arg(sgqlc.types.non_null(ISO8601DateTime), graphql_name='occuredAt', default=None)),
        ('result', sgqlc.types.Arg(sgqlc.types.non_null(Float), graphql_name='result', default=None)),
        ('object_class_id', sgqlc.types.Arg(Int, graphql_name='objectClassId', default=None)),
))
    )
    update_research_plan = sgqlc.types.Field('UpdateResearchPlanPayload', graphql_name='updateResearchPlan', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('assigned_to_id', sgqlc.types.Arg(ID, graphql_name='assignedToId', default=None)),
        ('objective', sgqlc.types.Arg(String, graphql_name='objective', default=None)),
        ('evaluation_process', sgqlc.types.Arg(String, graphql_name='evaluationProcess', default=None)),
))
    )
    update_research_plan_metric = sgqlc.types.Field('UpdateResearchPlanMetricPayload', graphql_name='updateResearchPlanMetric', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('research_plan_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='researchPlanId', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(ResearchPlanMetricCodeEnum), graphql_name='code', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('iou', sgqlc.types.Arg(Float, graphql_name='iou', default=None)),
        ('weighted', sgqlc.types.Arg(Boolean, graphql_name='weighted', default=None)),
        ('object_class_id', sgqlc.types.Arg(Int, graphql_name='objectClassId', default=None)),
))
    )


class Query(sgqlc.types.Type):
    __schema__ = silverpond_schema
    experiment = sgqlc.types.Field(Experiment, graphql_name='experiment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    experiments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Experiment))), graphql_name='experiments', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    research_plan = sgqlc.types.Field('ResearchPlan', graphql_name='researchPlan', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    research_plans = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ResearchPlan'))), graphql_name='researchPlans', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )


class ResearchPlan(sgqlc.types.Type):
    __schema__ = silverpond_schema
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    assigned_to_id = sgqlc.types.Field(Int, graphql_name='assignedToId')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='createdAt')
    created_by_id = sgqlc.types.Field(Int, graphql_name='createdById')
    description = sgqlc.types.Field(String, graphql_name='description')
    evaluation_process = sgqlc.types.Field(String, graphql_name='evaluationProcess')
    experiments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Experiment)), graphql_name='experiments')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    objective = sgqlc.types.Field(String, graphql_name='objective')
    research_plan_metrics = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ResearchPlanMetric')), graphql_name='researchPlanMetrics')
    title = sgqlc.types.Field(String, graphql_name='title')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='updatedAt')


class ResearchPlanMetric(sgqlc.types.Type):
    __schema__ = silverpond_schema
    code = sgqlc.types.Field(sgqlc.types.non_null(ResearchPlanMetricCodeEnum), graphql_name='code')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    iou = sgqlc.types.Field(Float, graphql_name='iou')
    name = sgqlc.types.Field(String, graphql_name='name')
    object_class_id = sgqlc.types.Field(Int, graphql_name='objectClassId')
    research_plan = sgqlc.types.Field(sgqlc.types.non_null(ResearchPlan), graphql_name='researchPlan')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='updatedAt')
    weighted = sgqlc.types.Field(Boolean, graphql_name='weighted')


class TrainingRun(sgqlc.types.Type):
    __schema__ = silverpond_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='createdAt')
    experiment = sgqlc.types.Field(sgqlc.types.non_null(Experiment), graphql_name='experiment')
    finished_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='finishedAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    image_queue_id = sgqlc.types.Field(Int, graphql_name='imageQueueId')
    model_id = sgqlc.types.Field(Int, graphql_name='modelId')
    model_implementation_file_url = sgqlc.types.Field(String, graphql_name='modelImplementationFileUrl')
    name = sgqlc.types.Field(String, graphql_name='name')
    project_id = sgqlc.types.Field(Int, graphql_name='projectId')
    requested_by_id = sgqlc.types.Field(Int, graphql_name='requestedById')
    source_code_commit_hash = sgqlc.types.Field(String, graphql_name='sourceCodeCommitHash')
    source_code_url = sgqlc.types.Field(String, graphql_name='sourceCodeUrl')
    started_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='startedAt')
    training_logs_file_url = sgqlc.types.Field(String, graphql_name='trainingLogsFileUrl')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(ISO8601DateTime), graphql_name='updatedAt')


class UpdateExperimentPayload(sgqlc.types.Type):
    __schema__ = silverpond_schema
    errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='errors')
    experiment = sgqlc.types.Field(Experiment, graphql_name='experiment')


class UpdateExperimentResultPayload(sgqlc.types.Type):
    __schema__ = silverpond_schema
    errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='errors')
    experiment_result = sgqlc.types.Field(ExperimentResult, graphql_name='experimentResult')


class UpdateResearchPlanMetricPayload(sgqlc.types.Type):
    __schema__ = silverpond_schema
    errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='errors')
    research_plan_metric = sgqlc.types.Field(ResearchPlanMetric, graphql_name='researchPlanMetric')


class UpdateResearchPlanPayload(sgqlc.types.Type):
    __schema__ = silverpond_schema
    errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='errors')
    research_plan = sgqlc.types.Field(ResearchPlan, graphql_name='researchPlan')



########################################################################
# Unions
########################################################################
