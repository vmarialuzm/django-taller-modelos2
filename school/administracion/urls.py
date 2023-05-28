from django.urls import path
from . import views

urlpatterns = [
    path('',views.AdministracionView.as_view(),name="index"),
    path('create/',views.ClassRoomCreate.as_view(),name="create"),
    path('delete/<int:id>',views.deleteClassRoom,name="delete"),
    path('vista1/',views.vista1,name="vista1"),
    path('vista2/',views.Vista2.as_view(),name="vista2"),
    path('create_student/',views.StudentCreate.as_view(),name="create_student"),
    path('student/<first_name>',views.obtenerStudent,name="student"),
    path('NoTemplate/',views.NoTemplate.as_view(),name='NoTemplate'),
    path('TemplateExample/',views.TemplateExample.as_view(),name='TemplateExample'),
    path('Otro/',views.Otro.as_view(),name='Otro'),
]

