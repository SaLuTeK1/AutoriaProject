from django.contrib.auth import get_user_model

from rest_framework import serializers

from core.services.email_service import EmailService

from apps.users.models import ProfileModel

UserModel = get_user_model()

# перевірка двох запитів в базу
from django.db.transaction import atomic


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age', 'phone', 'avatar')


class ProfileAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('avatar',)
        extra_kwargs = {'avatar': {'required': True}}


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_premium', 'is_staff', 'is_superuser',
            'last_login', 'created_at', 'updated_at', 'profile', 'cars', 'role'
        )
        read_only_fields = (
        'id', 'is_active', 'is_premium', 'is_staff', 'role', 'is_superuser', 'last_login', 'created_at', 'updated_at',
        'cars')

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        EmailService.register(user)
        return user
