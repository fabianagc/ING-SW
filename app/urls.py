from django.urls import path
from .views import pagLogin, pagADM, pagBase, pagPrincipal
from . import views


urlpatterns = [
    path('', pagLogin, name="pagLogin"),

    path('pagLogin/', pagLogin, name="pagLogin"),

    path('pagADM/', pagADM, name="pagADM"),

    path('pagBase/', pagBase, name="pagBase"),

    path('pagPrincipal/', pagPrincipal, name="pagPrincipal"),

    path('pagRegistro/', views.pagRegistro),

    path('pagEliminar/<id>/', views.pagEliminar),

    path('pagEditar/<id>/', views.pagEditar),

    path('pagEdicion/', views.pagEdicion),

]