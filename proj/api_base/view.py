from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import ErrorDetail, ValidationError
from .exceptions import APIException
import sys, traceback


class GenericAPIView(generics.GenericAPIView):

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)
        exception, code, message, data = getattr(response, 'exception', None), 1, None, getattr(response, 'data', None)
        default_message = 'please see data result for error info'
        print(data)

        if isinstance(data, dict):
            message = data.get('detail', None) or data.get('error', None) or data.get('non_field_errors', None)
            if data.get('non_field_errors', None):
                message = ''.join(message)
            if message:
                code, data = 0, None
            elif exception:
                message, code = default_message, 0

        elif isinstance(data, (list, tuple)) and data and isinstance(data[0], ErrorDetail):
            # print('data is list or tuple and the first element is ErrorDetail')
            response.status_code = 200
            code, message, data = 0, data[0], None
        # 自定义异常
        elif isinstance(data, APIException):
            # print('APIException')
            code, message, data = 0, data.message, None
        elif isinstance(data, ValidationError):
            print('ValidationError')
            response.status_code = 200
            try:
                x = data.detail.popitem()
                code, message, data = 0, x[0] + ": " + x[1][0], None
            except Exception:
                code, message, data = 0, 'System Error', None


        # 系统异常
        elif isinstance(data, Exception):
            # print('Sys Exception')
            response.status_code = 200
            code, message, data = 0, 'System Error', None

        data = {'Results': data} if (data is not None and 'Results' not in data) else data
        response.data = {'StatusCode': code, 'Msg': message, 'Data': data}

        return response

    def get_exception_handler(self):
        return exception_handler


def exception_handler(exc, context):
    # print(exc)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    # print("*** print_tb:")
    traceback.print_tb(exc_traceback, limit=100, file=sys.stdout)
    if isinstance(exc, APIException) or getattr(context['request'], 'from_app', None):
        return Response(exc)
    else:
        return context.get('view').settings.EXCEPTION_HANDLER(exc, context)
