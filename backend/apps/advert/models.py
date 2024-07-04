
from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

from core.models import BaseModel
from core.services.email_service import EmailService


class AdvertModel(BaseModel):
    class Meta:
        db_table = 'advert'

    name = models.CharField(max_length=20, validators=[V.MinLengthValidator(10)])
    info = models.TextField(validators=[V.MinLengthValidator(2), V.MaxLengthValidator(180)])
    status = models.CharField(max_length=10,
                              choices=[('active', 'Active'), ('inactive', 'Inactive'), ('pending', 'Pending')],
                              default='pending')
    edit_attempts = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.edit_attempts >= 3:
            self.status = 'inactive'
            self.notify_manager()
        else:
            if self.contains_prohibited_language(self.info) or self.contains_prohibited_language(self.name):
                self.status = 'pending'
                self.edit_attempts += 1
            else:
                self.status = 'active'
                self.edit_attempts = 0

        super().save(*args, **kwargs)

    def contains_prohibited_language(self, text):
        prohibited_words = ['badword1', 'badword2']
        return any(word in text.lower() for word in prohibited_words)

    def notify_manager(self):
        users = get_user_model()
        manager = users.objects.filter(role='manager', is_active=True).first()
        if manager:
            EmailService.ad_review(manager, self.id)


