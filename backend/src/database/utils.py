from .models import Drink


def get_all_drinks(is_short=True):
    """
    Get all drinks in serialized form using Drink.short method for serialization if is_short is True else Drink.long.

    :param is_short:
    :return:
    """
    drinks = Drink.query.all()
    return [drink.short() for drink in drinks] if is_short else [drink.long() for drink in drinks]
