from django.urls import path
from loginPage import views

urlpatterns = [
    path('', views.landingpage, name='landingpage' ),
    path('signup', views.signup),
    path('signin', views.signin),
    path('signout', views.signout),
]