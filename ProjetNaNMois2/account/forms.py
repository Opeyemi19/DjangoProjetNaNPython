from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate # Cette Class intervient lors du processus de 'Login'

from account.models import Account


class RegistrationForm(UserCreationForm):
    # email = forms.EmailField(max_length=254, help_text='Entrez un Email valide SVP!.')

    class Meta:
        model = Account
        # On va afficher les champs mentionés ds le 'fields'
        fields = ('fullname','username','email', 'password1', 'password2',)


class AccountAuthenticationForm(forms.ModelForm):
    
	# password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
        # On va afficher que nos deux champs (email et password)
		fields = ('email', 'password')

	def clean(self):
        # Verifie si les entré sont valid
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('fullname','username','email')
    
    def clean_fullname(self):
        fullname = self.cleaned_data['fullname']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(fullname=fullname)
        except Account.DoesNotExist:
            return fullname
        raise forms.ValidationError('Fullname "%s" is already in use.' % fullname)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % fullname)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % email)