from django.urls import path
from countries import views


urlpatterns = [
    path('', views.wiki, name='wiki'),
    # path('wiki', views.wiki, name='wiki')
]