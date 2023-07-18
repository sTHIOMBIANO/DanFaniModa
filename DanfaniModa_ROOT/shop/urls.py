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
    path('commande/',views.commande,name='commande'),
   #  path('supprimer/',views.supprimer,name='supprimer'),
    path('validation/',views.final,name="final"),
    path('administration/',views.tableau,name='tableau'),
    path('administration/ajouter/',views.ajouter,name='ajouter'),
    path('administration/commande',views.commandeUser,name='commandeUser'),
    path('administration/modifier',views.modifier,name='modifier'),
    path('administration/supprimer',views.modifier,name='supprimer'),
    path('administration/modifier/<int:my_id>',views.modifier_Produit,name='modifier_Produit'),
    path('administration/supprimer/<int:my_id>',views.supprimer,name='supprimer_produit'),
    path('<int:id>/',views.detail,name='detail'),
    path('<str:titre>/',views.produit_similaire_details,name='details'),
    path('pagne/<int:id>/',views.detail,name='detail'),
    path('porter/<int:id>/',views.detail,name='detail'),
    
    path("<str:titre>/panier/",views.ajouter_au_panier,name="ajout"),
   #  path('<int:id>/<str:titre>/panier/',views.ajouter_au_panier,name='ajout'),
   #  path('panier/delete/<int:my_id>',views.supprimer_produit,name="supprimer_produit"),
   #  path('panier/update/<int:my_id>',views.modifier,name="modifier"),
    
    
 ]