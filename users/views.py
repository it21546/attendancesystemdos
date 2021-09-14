from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm #προεγκατεστημενη φορμα για user login από την django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            it_number = form.cleaned_data.get('it_number')
            messages.success(request, f'Yor account has been created! You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required 	#show page only if user is logged in
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)#instance is to show his existing it_number and staff before giving him the chance to update them
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)# the request.FILES is because of the photo (jpg file) that is gonna be updated
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!') #provide success input message
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)#instance is to show his existing it_number and staff before giving him the chance to update them
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}

	return render(request, 'users/profile.html', context)
