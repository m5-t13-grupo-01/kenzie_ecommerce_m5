from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from addresses.models import Address
from addresses.serializers import AddressSerializers
from carts.models import Cart
import ipdb


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
            "is_seller",
            "is_admin",
            "address",
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
        if validated_data.get("address"):
            address = validated_data.pop("address")
            address_obj = Address.objects.filter(pk=instance.address.id).first()

            for key, value in address.items():
                setattr(address_obj, key, value)
            address_obj.save()

        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(validated_data.get("password"))
            else:
                setattr(instance, key, value)

        instance.save()

        return User.objects.filter(pk=instance.id).first()
