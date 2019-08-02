from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccount(BaseUserManager):
    def create_user(self, email, fullname, username, password=None):
        if not email:
            raise ValueError('Veuillez entrer un Email Valide')
        if not username:
            raise ValueError('Entrer un Username Valide')

        user = self.model(
            # 'normalize_email' verifie si c est un Email
			email=self.normalize_email(email),
            fullname=fullname,
			username=username,
		)

        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, email, fullname, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            fullname = fullname,
            username = username,
        )
        
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
    fullname 				= models.CharField(max_length=200)
    username 				= models.CharField(max_length=30, unique=True)
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname', 'username']

    objects = MyAccount()

    # Il va ns retourner ds notre Vue que les (Email) des Utilisateurs si l on veut retounner d'autre valeur a pas 'email' Alors on va faire par example qu il ns retourne (return self.email + ', ' + self.username)  ou on affiche ds ntre template grace á Djinja
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
    	return self.is_admin

    # Ns donne la Permission de se Connecté a la Page Admin 
    def has_module_perms(self, app_label):
        return True