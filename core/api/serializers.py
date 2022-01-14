from rest_framework.serializers import ModelSerializer

from core.models import AppLogin, ShowMeta, AppSamuraicupom


class AppLoginSerializer(ModelSerializer):
    class Meta:
        model = AppLogin
        fields = '__all__'


class AppSamuraicupomSerializer(ModelSerializer):
    class Meta:
        model = AppSamuraicupom
        fields = '__all__'


class ShowMetaSerializer(ModelSerializer):
    class Meta:
        model = ShowMeta
        fields = '__all__'
