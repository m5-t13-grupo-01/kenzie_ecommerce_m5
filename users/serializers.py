from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from addresses.models import Address
from addresses.serializers import AddressSerializers
from carts.models import Cart


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializers()
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
            "cart",
        ]
        read_only_fields = ["id", "is_superuser", "cart"]
        extra_kwargs = {"password": {"write_only": True}}
        depth = 1

    def create(self, validated_data: dict):
        address = validated_data.pop("address")

        address_obj = Address.objects.create(**address)

        new_cart = Cart.objects.create()

        if validated_data["is_admin"]:
            return User.objects.create_superuser(
                **validated_data, address=address_obj, cart=new_cart
            )
        else:
            return User.objects.create_user(
                **validated_data, address=address_obj, cart=new_cart
            )

    def update(self, instance: User, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.set_password(validated_data.get("password"))
        instance.save()

        return instance
