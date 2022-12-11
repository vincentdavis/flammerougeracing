import json

import coreapi
import coreschema
from backend.helpers.Exception import exception
#Apps
from apps.Setup import models as setupModel
from apps.Setup.rest_api import serializers as setupserializers

# Schema
form_name = coreapi.Field("form_name", location="query", schema=coreschema.String(description="Form Name"))
fields = coreapi.Field("fields", location="query", schema=coreschema.String(description="Fields to Return"))


def generate_fields(view, model, includeactions=False):
    try:
        defaultview = []
        ConfigView = []
        try:
            ConfigView = json.loads(setupModel.AppBasic.objects.get(config_name="Views", value='defaultview').options).get(view)
        except Exception as e:
            exception(e)
        # Looping fields
        for field in model._meta.fields:
            if field.name in ConfigView:
                if field.name in  ['name', 'start_date', 'end_date']:
                    defaultview.append({"value": field.name, "text": field.verbose_name, "is_default": True, "width" : "120"})
                else:
                    defaultview.append({"value": field.name, "text": field.verbose_name, "is_default": True})
            elif():
                pass
            else:
                defaultview.append({"value": field.name, "text": field.verbose_name, "is_default": False})
        # Adding CR
        if view == 'ProjectView':
            defaultview.insert(3, {"value": "risk", "text": "Risks", "is_default": True, "sortable": False, "width" : "120"})
            defaultview.insert(3, {"value": "dependencies", "text": "Dependencies", "is_default": True, "sortable": False, "width" : "120"})
            defaultview.insert(3, {"value": "milestones", "text": "Milestones", "is_default": True, "sortable": False, "width" : "120"})
            defaultview.insert(3, {"value": "cr", "text": "Change Request", "is_default": True, "sortable": False, "width" : "120"})
        if view == 'ResourceSearch':
            defaultview.append({"value": "availability", "text": "Availability", "is_default": True, "sortable": False, "align": "center"})
        # if includeactions :
        defaultview.append({"value": "actions", "text": "Actions", "is_default": True})
        return defaultview
    except Exception as e:
        exception(e)
        return []

def generate_customview_list(type):
    customview_list = setupserializers.CustomViewSerializers(setupModel.CustomView.objects.filter(type=type), many=True)
    return customview_list.data

def generate_customview(type, id):
    if id:
        return setupserializers.CustomViewSerializers(setupModel.CustomView.objects.get(type=type, id=id)).data
    else:
        return setupserializers.CustomViewSerializers(setupModel.CustomView.objects.get(type=type, is_default=True)).data

def get_status(obj, look_up_table, status):

    if look_up_table == 'milestone':
        if status == 'Completed':
            return obj.ProjectMilestone.filter(status=6).count()
        if status == 'InProgress':
            return obj.ProjectMilestone.exclude(status=6).count()
    if look_up_table == 'dependency':
        if status == 'Completed':
            return obj.ProjectDependencies.filter(status='Closed').count()
        if status == 'InProgress':
            return obj.ProjectDependencies.exclude(status='Closed').count()
    if look_up_table == 'risk':
        if status == 'Completed':
            return obj.ProjectRisk.filter(status=3).count()
        if status == 'InProgress':
            return obj.ProjectRisk.exclude(status=3).count()
