from django.urls import path
from .views import pagLogin, pagADM, pagBase, pagPrincipal, pagHabitacion, pagCheck, pagFecha
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', pagLogin, name="pagLogin"),

    path('pagLogin/', pagLogin, name="pagLogin"),

    path('pagADM/', pagADM, name="pagADM"),

    path('pagHabitacion/', pagHabitacion, name="pagHabitacion"),

    path('pagBase/', pagBase, name="pagBase"),

    path('pagPrincipal/', pagPrincipal, name="pagPrincipal"),

    path('pagCheck/', pagCheck, name="pagCheck"),

    path('pagFecha/', pagFecha, name="pagFecha"),

    path('pagRegistro/', views.pagRegistro),

    path('pagEliminar/<id>/', views.pagEliminar),

    path('pagEditar/<id>/', views.pagEditar),

    path('pagEdicion/', views.pagEdicion),



    path('pagRegistroH/', views.pagRegistroH),

    path('pagEliminarH/<id>/', views.pagEliminarH),

    path('pagEditarH/<id>/', views.pagEditarH),

    path('pagEdicionH/', views.pagEdicionH),

]