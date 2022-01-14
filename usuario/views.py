from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render
import requests
from core.models import AppLogin
from usuario.forms import UsuarioForm
from usuario.models import Usuario

usuario = get_user_model()


def criar_usuario(request):
    applogins = AppLogin.objects.all()
    if applogins:
        print(applogins.count())
        # for applogin in applogins:
        #     data = {
        #         'first_name': 'Teste',
        #         'last_name': 'Sobrenome',
        #         'codigorca': applogin.codigorca,
        #         'nomerca': applogin.nomerca,
        #         'codigosv': applogin.codigosv,
        #         'nomesv': applogin.nomesv,
        #         'modelo': applogin.modelo,
        #         'faixa': applogin.faixa,
        #         'funcao': applogin.funcao,
        #         'username': applogin.email,
        #         'email': applogin.email,
        #         'password': applogin.senha,
        #
        #     }
        #     r = requests.post('http://127.0.0.1:8000/api/usuario/', data=data)
        #     print(r.json())
    else:
        print('Erro ao buscar')
    return render(request, 'usuario/novo.html', {})
