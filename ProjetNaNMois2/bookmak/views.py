from django.shortcuts import render, redirect
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from bookmak.forms import PariForm
from bookmak.models import PariSport


def pariform_view(request):
    if not request.user.is_authenticated:
    	return redirect("login")
        
    context = {}

    if request.POST:
        form = PariForm(request.POST)
        if form.is_valid:
            form.save()
    
#     context['form_regis'] = form
    return render(request, "index.html", context)





        






















