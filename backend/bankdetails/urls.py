from django.urls import re_path as url
from bankdetails import views 
 
urlpatterns = [ 
    url(r'^api/bankdetails$', views.bankdetails_list),
    url(r'^api/bankdetails/(?P<pk>[0-9]+)$', views.bankdetails_detail),
    # url(r'^api/bankdetails/i$', views.bankdetails_detail),
    url(r'^api/bankdetails/updates$', views.updates_list),
    url(r'^api/users$', views.users_list),
    url(r'^api/users/login$', views.users_login),
]