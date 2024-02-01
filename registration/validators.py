from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.translation import gettext_lazy as _

class CustomPasswordValidator(BaseValidator):
    message = _(
        "The password must contain at least %(limit_value)d characters, "
        "including both letters and numbers."
    )
    code = "invalid_password"

    def __init__(self, limit_value=8):
        self.limit_value = limit_value
        print(f"Validator initialized with limit_value: {self.limit_value}")

    def __call__(self, password, user=None):
        if len(password) < self.limit_value:
            print(password, "less than", self.limit_value)
            raise ValidationError(
                _('Password must be at least %(limit_value)d characters long.') % {'limit_value': self.limit_value}
            )

        contains_digit = any(char.isdigit() for char in password)
        contains_alpha = any(char.isalpha() for char in password)
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        contains_special_char = any(char in special_characters for char in password)

        print("Validator called!")
        print(f"Password: {password}")
        print(f"Contains digit: {any(char.isdigit() for char in password)}")
        print(f"Contains alpha: {any(char.isalpha() for char in password)}")
        print(f"Contains special char: {any(char in special_characters for char in password)}")

        if not contains_digit:
            raise ValidationError(_('Password must contain at least one number.') % {'limit_value': self.limit_value})
        if not contains_alpha:
            raise ValidationError(_('Password must contain at least one character.') % {'limit_value': self.limit_value})
        if not contains_special_char:
            raise ValidationError(_('Password must contain at least one special character.') % {'limit_value': self.limit_value})