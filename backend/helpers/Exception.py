import logging
import os
import sys
import traceback

from django.core.exceptions import RequestDataTooBig, ValidationError
from django.db import IntegrityError
from django.db.models import ProtectedError
from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response
# from apps.Project import models
log = logging.getLogger('apps')


def exception(e):
    try:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)
        log.error(f' Error: {e}  Error Type:  {exc_type}  Module Name: {fname} Line No : {exc_tb.tb_lineno}')
    except Exception :
        log.error(e)


# def get_user(user_id, look_up="emp_fullname"):
#     try:
#         return model_to_dict(models.UserInfo.objects.filter(emp_userid=user_id).first()).get(look_up, "emp_fullname")
#     except Exception as e:
#         exception(e)
#         return user_id

def custom_rest_exception_handler(exc, context):
    """ Custom rest api exception handler """
    from rest_framework import exceptions
    from rest_framework.views import exception_handler, set_rollback
    response = exception_handler(exc, context)
    err_msg = str(exc)
    if isinstance(exc, RequestDataTooBig):
        return Response({'reason': 'too big data or file upload'}, status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)

    if isinstance(exc, ProtectedError):
        data = {'reason': ' Not able to delete, there are links to this record and is protected.'}
        traceback.print_exc()
        set_rollback()
        return Response(data, status=status.HTTP_412_PRECONDITION_FAILED)

    if isinstance(exc, IntegrityError) and ('already exists' in err_msg or 'must make a unique set' in err_msg or
                                            'must be unique' in err_msg):
        data = {'reason': 'duplicate unique key'}
        set_rollback()
        return Response(data, status=status.HTTP_409_CONFLICT)

    if response is None:
        if isinstance(exc, ValidationError):
            return Response(exc.message_dict, status=status.HTTP_400_BAD_REQUEST)
        traceback.print_exc()
        return Response({'reason': 'unexpected server error'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=True)

    if isinstance(exc, exceptions.NotAuthenticated):
        response.status_code = status.HTTP_401_UNAUTHORIZED
    elif isinstance(exc, exceptions.ValidationError) and (
            'already exists' in err_msg or 'must make a unique set' in err_msg or 'must be unique' in err_msg):
        response.status_code = status.HTTP_409_CONFLICT

    return response