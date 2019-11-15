from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_range(value):
    if value < 0 or value > 1:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
