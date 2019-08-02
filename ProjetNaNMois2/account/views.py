from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
    
    # Ce sont des fctions Crés á partir de 'forms.py'
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm



# def home_page(request):
#     return render(request,"index.html")


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('login')
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
    
    context['registration_form'] = form
    return render(request, 'Account/register.html', context)



def logout_view(request):
    logout(request)
    return redirect('scraping')

def login_view(request):
    
	context = {}

    # Si l' User est connecté et qu il  veut se reconnecter alors cela n est pas Possible dc il le redirige á la page d'acceuil
	user = request.user
	if user.is_authenticated: 
		return redirect("scraping")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)
            
            # Si les cooordonnées entre sont memes que ds la BD, il le connect 
			if user:
				login(request, user)
				return redirect("pari")

	else:
		form = AccountAuthenticationForm()

    # 'login_form' sera appelé ds la vue afin de permettre de manipuler les Champs afin de les afficher
	context['login_form'] = form

	# print(form)
	return render(request, "account/login.html", context)


def account_view(request):
    
	if not request.user.is_authenticated:
	    return redirect("login")

	context = {}

    # On considere que l'Utilisateur existe et qu il veut modifier ses infos
	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial = {
					"fullname": request.POST['fullname'],
					"username": request.POST['username'],
                    "email": request.POST['email'],
			}
			form.save()
			context['success_message'] = "Merci d'avoir modifier vos Informatios"
	else:
		form = AccountUpdateForm(
			initial = {
					"fullname": request.user.fullname, 
					"username": request.user.username,
                    "email": request.user.email, 
				}
			)

	context['account_form'] = form

	return render(request, "account/account.html", context)