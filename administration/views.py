from django.shortcuts import render, get_object_or_404, redirect
from basics.models import Userdata, Groupdata
from django.contrib.auth.models import User, Group
#from .forms import GroupForm
from basics.views import getAddress


# Create your views here.

def categories(request):
	return render(request, 'administration/categories.html')

def groups(request):
	groups = Group.objects.all()
	return render(request, 'administration/groups.html', {'groups': groups})

def informations(request):
	return render(request, 'administration/informations.html')

def mails(request):
	return render(request, 'administration/mails.html')

def needs(request):
	return render(request, 'administration/needs.html')

def users(request):
	users = Userdata.objects.order_by('pseudonym')
	return render(request, 'administration/users.html', {'users': users})

def user_delete(request, pk):
	# User somehow doesn't have attribute pk (only Userdata has), so we get the email from userdata and with that we get the user and can delete him
	userDa = get_object_or_404(Userdata, pk=pk)
	user = User.objects.get(username=userDa.user)
	user.delete()
	return redirect('administration:users')

def new_group(request):
	return render(request, 'administration/new_group.html')