from rest_framework import serializers, validators
from django.contrib.auth.models import User, Group

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        # read_only_fields = ('is_staff', 'is_superuser', 'is_active',)

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            # 'is_staff': {'write_only': True},
            # 'is_superuser': {'write_only': True},
            'password': {'write_only': True},
            'email': {
                'required': True,
                'allow_blank': False,
                'validators': [
                    validators.UniqueValidator(
                        User.objects.all(), 'ya existe una usuario con ese email'
                    )
                ]
            }
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        is_superuser = True
        is_staff = True

        user = User.objects.create(
            username = username,
            email = email,
            first_name = first_name,
            last_name = last_name,
            is_superuser = is_superuser,
            is_staff = is_staff
        )

        user.set_password(password)
        user.save()

        return user