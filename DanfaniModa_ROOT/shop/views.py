from itertools import count
import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import  Produit,Commande,Lignecommande
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProductForm
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Q
# from django.core.paginator import Paginator
#from .forms import OrderForm
# Create your views here.


#@login_required
def index(request):
	produit_objet=Produit.objects.all()
	#slider=Produit.objects.get(id=request)
	messages_error = messages.get_messages(request)
	item=request.GET.get("items-name")
	if item!= ' ' and item is not None:
		try:
			item=int(item)
			produit_objet=Produit.objects.filter(prix__lte=item)
		except ValueError:
			produit_objet=Produit.objects.filter(Q(titre__icontains=item))
		
			
		
			

	#paginator=Paginator(produit_objet,6)
	#page=request.GET.get('page')
	#produit_objet=paginator.get_page(page)
	return render(request,"posts/index.html",{'produit_objet':produit_objet,'messages_error':messages_error})




def detail(request,id):
	Dproduit=Produit.objects.get(id=id)
	sim=Dproduit.similaire
	prod=Produit.objects.filter(similaire=sim)

	if not request.user.is_authenticated:
		messages.error(request,"Veuillez vous connecter pour acceder a cette page")
		return redirect('index')
	
	return render(request,"posts/detail.html",{"Dproduit":Dproduit,"prod":prod})

def pagne(request):
	mes_pagne=Produit.objects.filter(titre__icontains="Pagnes")
	return render(request,"posts/pagne.html",{"mes_pagne":mes_pagne})

def porter(request):
	# pret_a_porter=Produit.objects.filter(titre__icontains="Habit")
	pret_a_porter=Produit.objects.filter(Q(titre__icontains="Habit") | Q(titre__icontains="Chemise"))
	return render(request,"posts/porter.html",{"pret_a_porter":pret_a_porter})

def produit_similaire_details(request,titre):
	Dproduit=get_object_or_404(Produit,titre=titre)
	return render(request,"posts/details.html",{"Dproduit":Dproduit})



def ajouter_au_panier(request,titre):
	# user=request.user
	# product=get_object_or_404(Produit,titre=titre)
	# cart,_=Lignecommande.objects.get_or_create(user=user)
	# order,created=Order.objects.get_or_create(user=user,article=product)
	# if created:
	# 	cart.orders.add(order)
	# 	cart.save()
	# else:
	# 	order.quantite+=1
	# 	order.save()

	return redirect(reverse('details',kwargs={'titre':titre}))


def panier(request):
	# mon_panier=get_object_or_404(Panier,user=request.user)
	# total=mon_panier.totaux()
	return render(request,"posts/panier.html")



        
# def supprimer(request):
# 	if panier:=request.user.panier:
# 		panier.orders.all().delete()
# 		panier.delete()
# 		return redirect('index')
	
# def supprimer_produit(request,my_id):
	
# 	prod_supp=get_object_or_404(Order,id=my_id)
	
# 	if request.method=='POST':
# 		prod_supp.delete()
# 		return redirect('panier')
# 	return render(request,"posts/delete.html")


# def modifier(request,my_id):
# 	prod_mod=get_object_or_404(Order,id=my_id)
# 	form=OrderForm(request.POST,request.FILES or None,instance=prod_mod)
# 	if form.is_valid():
# 		form.save()
# 		return redirect('panier')
# 	return render(request,"posts/update.html",{'form':form})

@login_required
def commande(request):
	if request.method=='POST':
		
		#panier_id=request.POST['panier_id']
		#mon_panier=get_object_or_404(Panier,user=user,id=panier_id
		
		itemdonnee=request.POST.get('item')
		print(itemdonnee)
		if itemdonnee=='{}':
			messages.error(request,'Desole,vous ne pouvez pas commander un panier vide')
		else:
			items=json.loads(itemdonnee)
			print(items)
			user=request.user
			#commande=Commande.objects.get(user=user)

			cart,created=Commande.objects.get_or_create(user=user)

			telephone=request.POST['Telephone']
			pays=request.POST['pays']
			ville=request.POST['ville']
			rue=request.POST['rue']
		
		
			cart.tel=telephone
			cart.pays=pays
			cart.ville=ville
			cart.rue=rue
			cart.save()

			for item,valeur in items.items():
				print(item)
				produit_key = item  
				produit = Produit.objects.get(pk=int(produit_key))

				quantite=valeur[2]
				
				maligne,_=Lignecommande.objects.get_or_create(command=cart,produit=produit)
				
				
				maligne.quantite=quantite
		
				maligne.save()

			# mon_panier.orders.ordered=True
			# mon_panier.orders.all().delete()
			return redirect('final')
		
	else:
		print("mauvais")
		messages.error(request,"une erreur s'est produite")
	return render(request,'posts/panier.html')


def final(request):
	user=request.user
	return render(request,"posts/verification.html",{"user":user})

def tableau(request):
	
	return render(request,'posts/tableau.html')

# def affiche(request):
# 	message=""
# 	#form=ContactForm()
# 	if request.method=="POST":
# 		#form=ContactForm(request.POST)
# 		item=request.POST.get('item')
# 		total=request.POST.get('total')
# 		nom=request.POST.get('nom')
# 		prenom=request.POST.get('prenom')
# 		email=request.POST.get('email')
# 		ville=request.POST.get('ville')
# 		pays=request.POST.get('pays')
# 		tel=request.POST.get('tel')
# 		commande=Commande(items=item,nom=nom,prenom=prenom,email=email,ville=ville,pays=pays,telephone=tel,total=total)
# 		commande.save()
		
# 		#if form.is_valid():
# 		#new=Commande.objects.create(**form.cleaned_data)
# 		#new.save()
# 		#form=ContactForm()
# 		return redirect('verifie')

# 	return render(request,"posts/afficher.html")

# @login_required
# def verification(request):
# 	com=Commande.objects.all()[:1]
# 	for c in com:
# 		prenom=c.prenom
# 	return render(request,"posts/verifivation.html",{"prenom":prenom})

# def pagne(request):
# 	pane=Produit.objects.filter(titre__icontains="Pagnes")
# 	return render(request,"posts/pagne.html",{"pane":pane})

# def porter(request):
# 	habit=Produit.objects.filter(titre__icontains="Habits")
# 	return render(request,"posts/pret_a_porter.html",{"habit":habit})



def register(request):
	#form=UserForm()
	if request.method=="POST":
		username=request.POST['username']
		firstname=request.POST['name']
		lastname=request.POST['surname']
		email=request.POST['email']
		password=request.POST['password']
		password1=request.POST['pass']
		if User.objects.filter(username=username):
			messages.error(request,"Ce nom existe déja")
			return redirect('register')
		if User.objects.filter(email=email):
			messages.error(request,request,"Ce email existe déja")
		if not username.isalnum():
			messages.error(request,"le nom d'utilisateur ne doit pas comporter du numerique")
			return redirect('register')
		if password!=password1:
			messages.error(request,"les mots de passe sont differents")
			return redirect('register')

		utilisateur=User.objects.create_user(username,email,password)


		utilisateur.first_name=firstname
		utilisateur.last_name=lastname
		utilisateur.save()
		messages.success(request,"votre compte a été crée avec succés")
		return redirect('connect')
		#form=UserForm(data=request.POST)
		#if form.is_valid:
			#form.save()
			#messages.success(request,"Votre compte a bien été crée")
			#form=UserForm()
			#return redirect('create')
		#else:
			#messages.error(request,form.errors)
	return render(request,"posts/register.html")


def connect(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		if user is not None and user.is_active:
			login(request,user)
			#messages.success(request,"Bienvenu")
			firstname=user.username
			return redirect('index')
		else:
			messages.error(request,"erreur d'autentification")
			return redirect('connect')
	return render(request,"posts/login.html")
			

@login_required
def deconnect(request):
	logout(request)
	messages.success(request,"vous etes deconnecté")
	#return redirect('index')
	return redirect('connect')

@login_required
def ajouter(request):
	#form=ProductForm()
	#if request.method=='POST':
	messages=''
	form=ProductForm(request.POST,request.FILES or None)
	if form.is_valid():
		form.save()
		form=ProductForm()
		messages="Ajout effectué avec succes "
	else:
		print("mauvais")
	return render(request,"posts/ajouter.html",{"form":form})


def commandeUser(request):
	
	com = Lignecommande.objects.all()
	
	item=request.GET.get("items-name")
	if item!= ' ' and item is not None:
		
		try:
			com=Lignecommande.objects.filter(Q(command__user__username__icontains=item))
			# produit_objet=Produit.objects.filter(prix__lte=item)
		except ValueError:
			# produit_objet=Produit.objects.filter(Q(titre__icontains=item))
			print('erreur')

	
	
	# date = com.first().date_commande if com.exists() else None
	return render(request,'posts/commande.html',{'com':com})

def modifier(request):
	mesProduit=Produit.objects.all()
	item=request.GET.get("items-name")
	if item!= ' ' and item is not None:
		try:
			item=int(item)
			mesProduit=Produit.objects.filter(prix__icontains=item)
		except ValueError:
			mesProduit=Produit.objects.filter(titre__icontains=item)
	return render(request,'posts/modifierProduit.html',{'mesProduit':mesProduit})

@login_required
def modifier_Produit(request,my_id):
	objet=get_object_or_404(Produit,id=my_id)
	form=ProductForm(request.POST,request.FILES or None,instance=objet)
	if form.is_valid():
		form.save()
		form=ProductForm()
	return render(request,"posts/modifier.html",{'form':form})


@login_required
def supprimer(request,my_id):
	objet=get_object_or_404(Produit,id=my_id)
	name=objet.titre
	if request.method=='POST':
		objet.delete()
		return redirect('supprimer')
	return render(request,"posts/delete.html",{'name':name})