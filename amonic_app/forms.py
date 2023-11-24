from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
import time
from django.contrib.auth import authenticate

class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        # Попытка аутентификации пользователя
        user = authenticate(username=email, password=password)

        if user is not None:
            # Если аутентификация прошла успешно, устанавливаем user_cache
            self.user_cache = user
        else:
            # Добавьте вашу логику проверки счетчика попыток и блокировки здесь
            # В данном примере, блокировка происходит после 3 неудачных попыток

            # Замените этот блок на вашу собственную логику
            if email and password:
                user = self.user_cache
                if not user.check_password(password):
                    # Увеличиваем счетчик неудачных попыток
                    user.failed_login_attempts += 1
                    user.save()

                    # Если достигнут лимит попыток, блокируем пользователя
                    if user.failed_login_attempts >= 3:
                        user.locked_until = int(time.time()) + 10  # Блокируем пользователя на 10 секунд
                        user.failed_login_attempts = 0  # Сбрасываем счетчик
                        user.save()
                        raise ValidationError('This account is temporarily locked. Please try again later.')

        return super().clean()