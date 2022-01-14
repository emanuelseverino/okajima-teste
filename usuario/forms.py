from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import Usuario


class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name',)
        labels = {'username': 'e-mail'}

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data['password1'])
        usuario.email = self.cleaned_data['username']
        if commit:
            usuario.save()
        return usuario


class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name',)


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ('password',)
