"""Docstring."""

from flask import Flask, jsonify

from flask_cors import CORS

from .database.models import setup_db

from .constants import STATUS_BAD_REQUEST, STATUS_CODE_MESSAGES, STATUS_UNAUTHORIZED

app = Flask(__name__)
setup_db(app)
CORS(app)

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

# Error Handling
"""
Example error handling for unprocessable entity
"""


@app.errorhandler(422)
def unprocessable(error):
    """
    Unprocessable.

    :param error:
    :return:
    """
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


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
    return jsonify({
        'success': False,
        'error': STATUS_UNAUTHORIZED,
        'message': STATUS_CODE_MESSAGES[STATUS_UNAUTHORIZED]
    }), STATUS_UNAUTHORIZED
