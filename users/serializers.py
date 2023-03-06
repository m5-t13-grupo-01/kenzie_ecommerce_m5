from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from addresses.models import Address


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that username already exists.",
            )
        ]
    )

    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that email already exists.",
            )
        ]
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_superuser",
            "address",
            "is_admin",
        ]
        read_only_fields = [
            "id",
            "is_superuser",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        address = validated_data.pop("address")

        address_obj = Address.objects.filter(
            street=address["street"], number=address["number"]
        )
        if not address_obj:
            address_obj = Address.objects.create(**address)

        if validated_data["is_admin"]:
            return User.objects.create_superuser(**validated_data, address=address_obj)
        else:
            return User.objects.create_user(**validated_data, address=address_obj)

    def update(self, instance: User, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.set_password(validated_data.get("password"))
        instance.save()

        return instance
