import os

from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from configs.celery import app
from core.dataclasses.user_dataclass import UserDataClass
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken

UserModel = get_user_model()


class EmailService:
    @staticmethod
    @app.task
    def __send_email(to: str, template_name: str, context: dict, subject: '') -> None:
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @classmethod
    def ad_review(cls, manager: UserDataClass, ad):
        url = f'http://localhost/api/advert/{ad}'
        cls.__send_email.delay(
            manager.email,
            'advertReview.html',
            {'name': manager.profile.name, 'url': url},
            'Advert Review'
        )

    @classmethod
    def register(cls, user: UserDataClass):
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://localhost:3000/activate/{token}'
        cls.__send_email.delay(
            user.email,
            'register.html',
            {'name': user.profile.name, 'url': url},
            'Register'
        )

    @classmethod
    def recovery_password(cls, user: UserDataClass):
        token = JWTService.create_token(user, RecoveryToken)
        url = f'http://localhost:3000/recovery/{token}'
        cls.__send_email.delay(
            user.email,
            'recovery.html',
            {'url': url},
            'Recovery'
        )

