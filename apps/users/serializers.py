from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.Serializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField(source="get_full_name")
    gender = serializers.CharField(source="profile.gender")
    phone_number = PhoneNumberField(source="profile.phone_number")
    profile_picture = serializers.ImageField(source="profile.profile_picture")
    country = CountryField(source="profile.country")
    city = serializers.CharField(source="profile.city")
    top_agent = serializers.BooleanField(source="profile.top_agent")

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "gender",
            "profile_picture",
            "country",
            "city",
            "phone_number",
            "top_agent",
        ]

    def get_first_name(self, obj):
        return obj.first_name.title()

    def get_last_name(self, obj):
        return obj.last_name.title()

    def to_representation(self, instance):
        representation = super(UserCreateSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation["admin"] = True

        return representation


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "password"]


class UserDeleteSerializer(serializers.Serializer):
    pass
