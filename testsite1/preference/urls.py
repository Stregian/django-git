from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^$', views.preferencehomepage),
    url(r'^add/$', views.add_choice ),
    url(r'^contact/$', views.contact),
]
