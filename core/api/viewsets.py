from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import AppLoginSerializer, AppSamuraicupomSerializer, ShowMetaSerializer
from core.models import AppLogin, ShowMeta, AppSamuraicupom


class AppLoginViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AppLogin.objects.all()
    serializer_class = AppLoginSerializer
    # permission_classes = [permissions.IsAuthenticated]


class AppSamuraicupomViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AppSamuraicupom.objects.all().order_by('-data')
    serializer_class = AppSamuraicupomSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(codigorca=self.request.user.codigorca)


class ShowMetaViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AppSamuraicupom.objects.all().order_by('-data')
    serializer_class = ShowMetaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(codigorca=self.request.user.codigorca)