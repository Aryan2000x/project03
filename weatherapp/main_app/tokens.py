from django.contrib.auth.tokens import PasswordResetTokenGenerator
# refer to https://forum.djangoproject.com/t/django-passwordresettokengenerator/5872
from six import text_type

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            text_type(user.pk) + text_type(timestamp) +
            text_type(user.is_active)
        )

account_activation_token = TokenGenerator()