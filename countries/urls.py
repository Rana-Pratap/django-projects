from django.urls import path
from countries import views


urlpatterns = [
    path('', views.wiki, name='home'),
    # path('wiki', views.wiki, name='wiki')
]