from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

Usuario = get_user_model()


class CriarUsuarioSerializer(ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'password', 'codigorca', 'nomerca', 'codigosv', 'nomesv',
                  'modelo', 'faixa', 'funcao', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        usuario = Usuario(username=validated_data['email'], **validated_data)
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        # fields = ['foto', 'first_name', 'last_name', 'cidade', ]
        fields = "__all__"
