from django.shortcuts import render


def dashboard_user(request):
    return render(request, 'pagos.html')


def token_credit_card(request):
	print 'llego'
	token = request.POST['token_id']
	print token
	return render(request, 'user_dashboard.html')

