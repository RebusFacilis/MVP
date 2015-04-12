from django.conf.urls import include, url
from django.contrib import admin
from app import views as app_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'rebus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', app_views.Login.as_view(), name='login'),
    url(r'^investment/$', app_views.UserInvestmentView.as_view(), name='user'),
    url(r'^investment/confirm/$', app_views.UserInvestmentConfirmationView.as_view(), name='investment-confirm'),
    url(r'^dashboard/$', app_views.dashboard_user, name='dashboard-user'),
    url(r'^token/$', app_views.token_credit_card, name="token"),
    url(r'^cards/$', app_views.cardform, name="cards"),
]