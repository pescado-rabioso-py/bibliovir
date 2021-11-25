from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import PrependedText

from apps.usuario.models import Usuario


class FormularioLogin(AuthenticationForm):
	def __init__(self,*args,**kwargs):
		super(FormularioLogin, self).__init__(*args,**kwargs)
		self.fields["username"].label = ""
		self.fields["password"].label = ""
		self.helper = FormHelper()
		self.helper.layout = Layout(
			PrependedText('username','@',placeholder='Ingrese su Usuario'
			),
			PrependedText('password', '<i class="fa fa-key"></i>', placeholder="Ingrese su contraseña"),

			Submit('sign_in', 'Acceder',
                   css_class='btn btn-lg btn-success btn-block')
		)

class FormularioUsuario(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	nombres = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
	apellidos = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Usuario
		fields = ('username','nombres','apellidos','email','password1','password2')

	def __init__(self,*args,**kwargs):
		super(FormularioUsuario, self).__init__(*args,**kwargs)
		
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'


	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 != password2:
			raise forms.ValidationError('Password no coincide!')
		return password2

	def save(self,commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user


class CambiarPasswordForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
	password1 = forms.CharField(label = 'Password',widget=forms.PasswordInput(
		attrs = {
			'class':'form-control',
			'placeholder':'Ingrese su nuevo password...',
			'id':'password1',
			'required':'required',
		}
	))

	password2 = forms.CharField(label = 'Password de confirmacion',widget=forms.PasswordInput(
		attrs = {
			'class':'form-control',
			'placeholder':'Ingrese nuevamente su nuevo password...',
			'id':'password2',
			'required':'required',
		}
	))

	class Meta:
		model = User
		fields = ('old_password','new_password1','new_password2')

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 != password2:
			raise forms.ValidationError('Password no coincide!')
		return password2