from django.conf.urls import url

from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<account_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add_account/$', views.add_account, name='add_account'),
    url(r'^(?P<account_id>[0-9]+)/add_transaction/$', views.add_transaction, name='add_transaction'),
]