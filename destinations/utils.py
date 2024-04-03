from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, NotFound, PermissionDenied, AuthenticationFailed

def custom_exception_handler(exc, context):
    # Call default exception handler first
    response = exception_handler(exc, context)

    if response is not None:
        # Customize error responses based on the exception
        if isinstance(exc, ValidationError):
            errors = []
            for field, error in exc.detail.items():
                errors.append({
                    'field': field,
                    'message': error[0] if isinstance(error, list) else error
                })
            custom_response = {
                'error': True,
                'detail': 'Validation Error',
                'errors': errors,
                'status_code': status.HTTP_400_BAD_REQUEST
            }
        elif isinstance(exc, NotFound):
            custom_response = {
                'error': True,
                'detail': 'Not found.',
                'status_code': status.HTTP_404_NOT_FOUND
            }
        elif isinstance(exc, PermissionDenied):
            custom_response = {
                'error': True,
                'detail': 'Permission denied.',
                'status_code': status.HTTP_403_FORBIDDEN
            }
        elif isinstance(exc, AuthenticationFailed):
            custom_response = {
                'error': True,
                'detail': 'Authentication failed.',
                'status_code': status.HTTP_401_UNAUTHORIZED
            }
        else:
            custom_response = {
                'error': True,
                'detail': 'An error occurred.',
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR
            }

        response.data = custom_response

    return response
