from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('connect/',views.connect,name='connect'),
    path('register/',views.register,name='register'),
    path('deconnect/',views.deconnect,name='deconnect'),
    path('pagne/',views.pagne,name='pagne'),
    path('porter/',views.porter,name='porter'),
    path('panier/',views.panier,name='panier'),
    path('supprimer/',views.supprimer,name='supprimer'),
    path('<int:id>/',views.detail,name='detail'),
    path('<str:titre>/',views.produit_similaire_details,name='details'),
    path('pagne/<int:id>/',views.detail,name='detail'),
    path('porter/<int:id>/',views.detail,name='detail'),
    path("<str:titre>/panier/",views.ajouter_au_panier,name="ajout"),
    path('<int:id>/<str:titre>/panier/',views.ajouter_au_panier,name='ajout'),
    path('panier/delete/<int:my_id>',views.supprimer_produit,name="supprimer_produit"),
     path('panier/update/<int:my_id>',views.modifier,name="modifier"),
    
    
]