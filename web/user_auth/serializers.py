from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]

        if (email and User.objects.filter(email=email).exclude(
                username=username).exists()):
            raise serializers.ValidationError(
                {"email": "Email addresses must be unique."})

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        return user
