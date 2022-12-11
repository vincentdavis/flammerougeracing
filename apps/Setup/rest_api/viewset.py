from django_filters.rest_framework import DjangoFilterBackend
from rest_access_policy import AccessViewSetMixin
from rest_framework import mixins, filters, status, viewsets
from rest_framework.decorators import action, schema
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.viewsets import GenericViewSet
from apps.Setup import models
from apps.Setup.rest_api import serializers
from apps.Setup.rest_api import access_policy
from backend.helpers.Helpers import (form_name , fields)


class AppBasicViewSet(AccessViewSetMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      GenericViewSet):
    serializer_class = serializers.AppBasicserserializer
    queryset = models.AppBasic.objects.all()
    access_policy = access_policy.AppBasicAccessPolicy
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['id', 'config_name']

    @action(detail=False, methods=['POST'])
    def authentication(self, request):
        try:
            appbasic_obj = models.AppBasic.objects.get(config_name=request.data.get('config_name', None))
        except:
            appbasic_obj = None
        if appbasic_obj:
            ser = self.get_serializer(appbasic_obj, data=request.data)
        else:
            ser = self.get_serializer(data=request.data)

        if ser.is_valid(raise_exception=True):
            ser.save()
        return Response("Authentication Updated", status=status.HTTP_200_OK)


class FormsModelViewset(AccessViewSetMixin, mixins.ListModelMixin,
                        mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        GenericViewSet):
    pagination_class = None
    access_policy = access_policy.FormsPolicy
    serializer_class = serializers.FormsModelSerializers
    queryset = models.FormsModel.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name']

    @action(detail=False, methods=['GET'], schema=ManualSchema(fields=[form_name]))
    def get_form(self, request):
        serializer_context = {'request': request.query_params}
        form = models.FormsModel.objects.get(name=request.query_params.get("form_name"))
        ser = serializers.FormsModelSerializers(form)
        formser = serializers.LayoutSeralizers(data=ser.data['layout'], many=True, context=serializer_context)
        formser.is_valid(raise_exception=True)
        return Response(formser.data)


class DropDownFieldValuesViewset(viewsets.ModelViewSet):
    serializer_class = serializers.DropDownFieldValuesSerializers
    queryset = models.DropDownFieldValues.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['fieldname']
