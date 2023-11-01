from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_superuser",
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    id = serializers.UUIDField(read_only=True)
    username = serializers.CharField(validators=[
        UniqueValidator(
            queryset=Account.objects.all(),
            message="A user with that username already exists.",
        )
    ])
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[
        UniqueValidator(
            queryset=Account.objects.all(),
            message="user with this email already exists.",
        )
    ])
    is_superuser = serializers.BooleanField(required=False)

    def create(self, validated_data: dict) -> Account:
        is_superuser = validated_data.get("is_superuser", False)
        if is_superuser:
            return Account.objects.create_superuser(**validated_data)
        else:
            return Account.objects.create_user(**validated_data)
