__author__ = 'Mykhailo'

from pyhighlighterclient import ResearchPlans, ResearchPlanMetric


"""
    examples - Get All Data, Find Data, Create / Update the research plan
"""
researchplans = ResearchPlans(apitoken='c5c37a60fed25025f6501351e8aba08603306177117da46d97e38531ae11d463', apiurl='https://staging.highlighter.ai/graphql')

# Testing Code - Get Object using schema
print('-------------------- get_all_research_plans Test --------------------')
result1 = researchplans.get_all_research_plans()
print('-------------------- find_research_plan_by_id(11111) Test --------------------')
try:
    result2 = researchplans.find_research_plan_by_id("11111")
except Exception as e:
    print(str(e))


print('-------------------- create_research_plan Test --------------------')
try:
    result3 = researchplans.create_research_plan(title="aaaaa", description="ddddd", assigned_to_id=1185, objective="test objective", evaluation_process="test evaluation")
except Exception as e:
    print(str(e))

print('-------------------- update_research_plan Test --------------------')
result4 = researchplans.update_research_plan(id="38", title="Updated Title Id=32", description="desc", assigned_to_id=85, objective="test objective132", evaluation_process="test evaluation452")

"""
    examples - Create / Update the research plan metric
"""
researchplanmetric = ResearchPlanMetric(apitoken='c5c37a60fed25025f6501351e8aba08603306177117da46d97e38531ae11d463', apiurl='https://staging.highlighter.ai/graphql')
result5 = researchplanmetric.create_research_plan_metric(research_plan_id='4', code='mAP', name='test metricBBB', description='test metricBBBB', iou=1.1, weighted=True, object_class_id=1)
result6 = researchplanmetric.update_research_plan_metric(id='16', research_plan_id='4', code='MaAD', name='test metric222', description='test metricCCC', iou=2.2, weighted=False, object_class_id=2)