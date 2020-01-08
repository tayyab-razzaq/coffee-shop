"""Docstring."""

from flask import Flask, abort, jsonify

from flask_cors import CORS

from .database import get_all_drinks, setup_db

from .constants import (
    STATUS_BAD_REQUEST, STATUS_FORBIDDEN, STATUS_CODE_MESSAGES, STATUS_INTERNAL_SERVER_ERROR,
    STATUS_METHOD_NOT_ALLOWED, STATUS_NOT_FOUND, STATUS_UNAUTHORIZED, STATUS_UNPROCESSABLE_ENTITY
)

app = Flask(__name__)
setup_db(app)
CORS(app, resources={r"*": {"origins": "*"}})


@app.after_request
def after_request(response):
    response.headers.add(
        'Access-Control-Allow-Headers',
        'Content-Type, Authorization'
    )
    response.headers.add(
        'Access-Control-Allow-Methods',
        'GET, POST, PUT, PATCH, DELETE, OPTIONS'
    )
    return response


"""
@TODO uncomment the following line to initialize the database
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
"""
# db_drop_and_create_all()

# ROUTES
"""
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks}
    where drinks is the list of drinks
    or appropriate status code indicating reason for failure
"""


@app.route('/drinks')
def get_drinks():
    try:
        return jsonify({
            'success': True,
            'drinks': get_all_drinks()
        })
    except Exception as exp:
        abort(exp.code)


"""
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks}
    where drinks is the list of drinks
    or appropriate status code indicating reason for failure
"""

"""
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink}
    where drink an array containing
    only the newly created drink or appropriate status code
    indicating reason for failure
"""

"""
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink}
    where drink an array containing
    only the updated drink or appropriate status code
    indicating reason for failure
"""

"""
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id}
    where id is the id of the deleted record
        or appropriate status code indicating reason for failure
"""

"""
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

"""

"""
@TODO implement error handler for 404
    error handler should conform to general task above
"""

"""
@TODO implement error handler for AuthError
    error handler should conform to general task above
"""

# Error Handling


@app.errorhandler(STATUS_BAD_REQUEST)
def bad_request(error):
    """
    Error handler for bad request with status code 400.

    :param: error
    :return:
    """
    return jsonify({
        'success': False,
        'error': STATUS_BAD_REQUEST,
        'message': STATUS_CODE_MESSAGES[STATUS_BAD_REQUEST]
    }), STATUS_BAD_REQUEST


@app.errorhandler(STATUS_UNAUTHORIZED)
def unauthorized(error):
    """
    Error handler for unauthorized with status code 401.

    :param error:
    :return:
    """
    return jsonify({
        'success': False,
        'error': STATUS_UNAUTHORIZED,
        'message': STATUS_CODE_MESSAGES[STATUS_UNAUTHORIZED]
    }), STATUS_UNAUTHORIZED


@app.errorhandler(STATUS_FORBIDDEN)
def forbidden(error):
    """
    Error handler for forbidden with status code 403.

    :param error:
    :return:
    """
    return jsonify({
        'success': False,
        'error': STATUS_FORBIDDEN,
        'message': STATUS_CODE_MESSAGES[STATUS_FORBIDDEN]
    }), STATUS_FORBIDDEN


@app.errorhandler(STATUS_NOT_FOUND)
def not_found(error):
    """
    Error handler for not found with status code 404.

    :param error:
    :return:
    """
    return jsonify({
        'success': False,
        'error': STATUS_NOT_FOUND,
        'message': STATUS_CODE_MESSAGES[STATUS_NOT_FOUND]
    }), STATUS_NOT_FOUND


@app.errorhandler(STATUS_METHOD_NOT_ALLOWED)
def method_not_allowed(error):
    """
    Error handler for method not allowed with status code 405.

    :param error:
    :return:
    """
    return jsonify({
        'success': False,
        'error': STATUS_METHOD_NOT_ALLOWED,
        'message': STATUS_CODE_MESSAGES[STATUS_METHOD_NOT_ALLOWED]
    }), STATUS_METHOD_NOT_ALLOWED


@app.errorhandler(STATUS_UNPROCESSABLE_ENTITY)
def unprocessable_entity(error):
    """
    Error handler for unprocessable entity with status code 422.

    :param error:
    :return:
    """
    return jsonify({
        'success': False,
        'error': STATUS_UNPROCESSABLE_ENTITY,
        'message': STATUS_CODE_MESSAGES[STATUS_UNPROCESSABLE_ENTITY]
    }), STATUS_UNPROCESSABLE_ENTITY


@app.errorhandler(STATUS_INTERNAL_SERVER_ERROR)
def internal_server_error(error):
    """
    Error handler for internal server error with status code 500.

    :param error:
    :return:
    """
    return jsonify({
        'success': False,
        'error': STATUS_INTERNAL_SERVER_ERROR,
        'message': STATUS_CODE_MESSAGES[STATUS_INTERNAL_SERVER_ERROR]
    }), STATUS_INTERNAL_SERVER_ERROR
