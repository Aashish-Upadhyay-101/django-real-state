from dataclasses import fields
from this import d
from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from apps.ratings.serializers import RatingSerializer
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    full_name = serializers.SerializerMethodField(read_only=True)
    country = CountryField(name_only=True) 
    reviews = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Profile 
        fields = [ "username", "first_name", "last_name", "full_name", "email", 
                "id", "phone_number", "profile_picture", "about_me", "real_estate_license", 
                "gender", "country", "city", "is_buyer", "is_seller", "is_agent", 
                "rating", "num_of_reviews", "reviews",]

    # it this not work then will do it later
    def get_full_name(self, obj):
        return obj.user.get_full_name

    def get_reviews(self, obj):
        reviews = obj.agent_review.all()
        serializer = RatingSerializer(reviews, many=True)
        return serializer.data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.top_agent:
            representation["top_agent"] = True

        return representation


class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)
 
    class Meta:
        model = Profile
        fields = ["phone_number", "profile_picture", "about_me", "real_estate_license", "gender",
                 "country", "city", "is_buyer", "is_seller", "is_agent"]


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.top_agent:
            representation["top_agent"] = True

        return representation

