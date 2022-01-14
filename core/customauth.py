# from rest_framework.authentication import BaseAuthentication
# from django.contrib.auth.models import User
# from core.models import AppLogin
#
#
# class CustomAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         codigorca = request.GET.get('codigorca')
#         if codigorca is None:
#             return None
#
#         try:
#             usuario = AppLogin.objects.get(codigorca=codigorca)
#         except AppLogin.