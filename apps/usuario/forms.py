from django import forms
from django.contrib.auth.forms import AuthenticationForm
from apps.usuario.models import Usuario
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Fieldset,ButtonHolder,Submit
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


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
                   css_class='btn btn-lg btn-success btn-block'),
		) 
	

class FormularioUsuario(forms.ModelForm):
	password1 = forms.CharField(label = 'Password',widget=forms.PasswordInput(
		attrs={
			'class':'form-control',
			'placeholder':'Ingrese su password...',
			'id':'password1',
			'required':'required',
		}
	))

	password2 = forms.CharField(label = 'Password de confirmacion',widget=forms.PasswordInput(
		attrs={
			'class':'form-control',
			'placeholder':'Ingrese nuevamente su password...',
			'id':'password2',
			'required':'required',
		}
	))

	class Meta:
		model = Usuario
		fields = ('email','username','nombres','apellidos','rol')
		widget = {
			'email': forms.EmailInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Correo Electronico',
				}
			),
			'nombres':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Ingrese su nombre',
				}
			),
			'apellidos':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Ingrese sus apellidos',
				}
			),
			'username':forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Ingrese su nombre de usuario',
				}
			),
			'rol': forms.Select(
				attrs={
					'class':'form-control'
				}
			)
		}

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


class CambiarPasswordForm(forms.Form):
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

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 != password2:
			raise forms.ValidationError('Password no coincide!')
		return password2