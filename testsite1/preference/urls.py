from django.conf.urls import url
from . import views

app_name = "preference"
urlpatterns =[
    url(r'^$', views.preferencehomepage, name="preference-homepage"),
    url(r'^add/$', views.add_choice, name = "add-choice"),
    url(r'^contact/$', views.contact, name = "contact"),
]
