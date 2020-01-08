from .models import Drink


def get_all_drinks():
    drinks = Drink.query.all()
    return [drink.short() for drink in drinks]
