"""Module for database utils."""

from .models import Drink


def get_all_drinks(is_short=True):
    """
    Get all drinks in serialized form using Drink.short method for serialization if is_short is True else Drink.long.

    :param is_short:
    :return:
    """
    drinks = Drink.query.all()
    return [drink.short() for drink in drinks] if is_short else [drink.long() for drink in drinks]


def add_new_drink(drink):
    """
    Create a new drink in the table.

    :param drink:
    :return:
    """
    instance = Drink(**drink)
    instance.insert()
    return instance.long()


def update_drink_in_db(drink_id, drink_data):
    """
    Update drink in db by given drink id and drink data and return the updated drink detail.

    :param drink_id:
    :param drink_data:
    :return:
    """
    drink = Drink.query.filter_by(id=drink_id).first()
    drink.title = drink_data.get('title')
    drink.recipe = drink_data.get('recipe')
    drink.update()
    return drink.long()
