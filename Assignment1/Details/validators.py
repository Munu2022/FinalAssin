from django.core.exceptions import ValidationError

def validate_lastname(value):
    if value is Null:
        raise ValidationError("Required field")
    return value


def date_of_birth(value):
    if value is None:
        raise ValidationError("Required field")
    return value

def dept_name(value):
    if value is None:
        raise ValidationError("Required field")
    return value


