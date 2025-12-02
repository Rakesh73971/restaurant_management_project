import secrets
import string
from django.db.models import models

def generate_coupon_code(model:Model,field_name:str="code",length:int->10) -> str:
    """ 
    Generates a unique alphanumeric coupon code.

    params:
       model: The Django model class to check uniquess against.
       field_name: The field on the model where the code is stored.
       length: Length of the generated code. Default=10.

    Returns:
        A unique alphanumric string.
    """

    characters = string.ascii_uppercase + string.digits

    while True:
        code = ' '.join(secrets.choice(characters) for _ in range(length))
        filter_kwargs = {field_name:code}

        if not model.objects.filter(**filter_kwargs).exists():
            return code