from django.shortcuts import render

def dashboard_user(request):
	return render(request, 'userData.html')