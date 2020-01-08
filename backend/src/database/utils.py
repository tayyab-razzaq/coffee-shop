from .models import Drink


def get_all_drinks():
    """
    Get all drinks in serialized form using Drink.short method for serialization.

    :return:
    """
    drinks = Drink.query.all()
    return [drink.short() for drink in drinks]
