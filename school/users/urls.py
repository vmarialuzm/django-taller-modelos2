from django.urls import path
#django tiene un template preparado para el login
#Es decir nos prevee de la clase LoginView para poder mostrar el formulario de inicio de sesion
from django.contrib.auth.views import LoginView,logout_then_login
from .views import RegisterView

#Segun el documento de django la url correcta para que funcione debe ser account/login/
urlpatterns = [
    path('account/login/', LoginView.as_view(), name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('logout/',logout_then_login,name='logout')
]

""" 
LoginView
va a buscar al archivo registration/login
template_name = "registration/login.html"
Esta clase recibe 2 cosas username y password
Dentro de la clase va a verificar que el username y password
ingresados sean correctos

Para que esto funcione hay que seguir ciertas reglas
1: La url se debe llamar: accouts/login/
2: El template de login debe estar en la carpeta registration/login.html
"""