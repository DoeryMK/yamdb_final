import re

from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class UserDataValidation:
    RESTRICTED_USERNAME = 'me'
    PATTERN = re.compile(r'[\w.@+-]+')

    def validate_username(self, username):
        matches = self.PATTERN.fullmatch(username)
        restricted_symbols = self.PATTERN.sub('', username)
        if matches is None:
            raise ValidationError(
                f'В username допустимо использовать только буквы, цифры и '
                f'знаки @.+-_. Применение {restricted_symbols} запрещено.')
        if username == self.RESTRICTED_USERNAME:
            raise ValidationError(
                f'Использовать имя {self.RESTRICTED_USERNAME} '
                'в качестве username запрещено.')
        return username

    def validate_email(self, email):
        try:
            validate_email(email)
        except Exception:
            raise ValidationError('Введен некорректный почтовый ящик')
        return email
