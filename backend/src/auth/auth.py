"""Module for auth."""

from flask import request

from functools import wraps

from ..constants import STATUS_CODE_MESSAGES, STATUS_FORBIDDEN, STATUS_UNAUTHORIZED

AUTH0_DOMAIN = 'udacity-fsnd.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'dev'


class AuthError(Exception):
    """A standardized way to communicate auth failure modes."""

    def __init__(self, error, status_code):
        """
        Init method of class.

        :param error:
        :param status_code:
        """
        self.error = error
        self.status_code = status_code


# Auth Header

"""
@TODO implement get_token_auth_header() method
    it should attempt to get the header from the request
        it should raise an AuthError if no header is present
    it should attempt to split bearer and the token
        it should raise an AuthError if the header is malformed
    return the token part of the header.
"""


def raise_auth_error(message):
    raise AuthError({
        'success': False,
        'message': message,
        'error': STATUS_UNAUTHORIZED
    }, STATUS_UNAUTHORIZED)


def get_token_auth_header():
    """
    Get token from authorization header and raise error is header is incorrect.

    :return:
    """
    authorization = request.headers.get('Authorization')
    if not authorization:
        raise_auth_error('Authorization header is expected')

    authorization_parts = authorization.split(' ')
    if authorization_parts[0].lower() != 'bearer':
        raise_auth_error('Authorization header must start with "Bearer".')

    elif len(authorization_parts) == 1:
        raise_auth_error('token not found')

    elif len(authorization_parts) > 2:
        raise_auth_error('Authorization header must be bearer token.')

    token = authorization_parts[1]
    return token


def check_permissions(permission, payload):
    """
    Check permission against a payload.

    :param permission:
    :param payload:
    :return:
    """
    if 'permissions' in payload and permission in payload['permissions']:
        return True

    raise AuthError({
        'success': False,
        'error': STATUS_FORBIDDEN,
        'message': STATUS_CODE_MESSAGES[STATUS_FORBIDDEN]
    }, STATUS_FORBIDDEN)


"""
@TODO implement verify_decode_jwt(token) method
    @INPUTS
        token: a json web token (string)

    it should be an Auth0 token with key id (kid)
    it should verify the token using Auth0 /.well-known/jwks.json
    it should decode the payload from the token
    it should validate the claims
    return the decoded payload
"""


def verify_decode_jwt(token):
    """
    Verify if jwt can be decoded properly and is not tempered.

    :param token:
    :return:
    """
    raise Exception('Not Implemented')


"""
@TODO implement @requires_auth(permission) decorator method
    @INPUTS
        permission: string permission (i.e. 'post:drink')

    it should use the get_token_auth_header method to get the token
    it should use the verify_decode_jwt method to decode the jwt
    it should use the check_permissions method validate claims
    and check the requested permission return the decorator which
    passes the decoded payload to the decorated method
"""


def requires_auth(permission=''):
    """
    Require Auth method.

    :param permission:
    :return:
    """

    def requires_auth_decorator(function):
        """
        Require Auth decorator.

        :param function:
        :return:
        """

        @wraps(function)
        def wrapper(*args, **kwargs):
            """
            Decorate wrapper method.

            :param args:
            :param kwargs:
            :return:
            """
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return function(payload, *args, **kwargs)

        return wrapper

    return requires_auth_decorator
