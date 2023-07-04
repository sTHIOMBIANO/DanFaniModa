from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


#User=get_user_model()

# Create your models here.



class Categorie(models.Model):
    name=models.CharField(max_length=500)
    date_ajout=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-date_ajout']

    def __str__(self):
        return f"{self.name}"

class Produit(models.Model):
    titre=models.CharField(max_length=500)
    prix=models.FloatField()
    description=models.TextField()
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="static/images",blank=True)
    similaire=models.CharField(default="blanc")
    type=models.CharField(default="pagne")
    date_ajout=models.DateTimeField(auto_now=True)


    class Meta:
        ordering=['-date_ajout']

    def __str__(self):
        return f"{self.titre}"
    

    def get_absolute_url(self):
        return reverse("ajout",kwargs={'titre':self.titre})
    

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    article=models.ForeignKey(Produit,on_delete=models.CASCADE)
    quantite=models.IntegerField(default=1)
    ordered=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.article.titre} ({self.quantite})"
    
    def total(self):
        return f"{self.quantite*self.article.prix}"
    
    


class Panier(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    orders=models.ManyToManyField(Order)
    ordered=models.BooleanField(default=False)
    


    def __str__(self):

        return self.user.username
    
    def totaux(self):
        self.total_gene=0
        for article in self.orders.all():
            self.total_gene+=article.total()
            print(self.total_gene)
        return f"{self.total_gene}"
    
    
    
class Commande(models.Model):
    commandes=models.ForeignKey(Panier,on_delete=models.CASCADE)
    date_commande=models.DateTimeField(blank=True,auto_now=True)


    def __str__(self):

        return self.commandes.user.username
    
    
    



# class Commande(models.Model):
#     items=models.CharField(max_length=500)
#     total=models.CharField(max_length=300)
#     nom = models.CharField(max_length=500)
#     prenom = models.CharField(max_length=500)
#     email = models.EmailField()
#     ville = models.CharField(max_length=300) 
#     pays = models.CharField(max_length=200)
#     telephone = models.CharField(max_length=20)
#     produit=models.ForeignKey(Produit,on_delete=models.CASCADE,null=True)
#     date_commande=models.DateTimeField(auto_now=True)


#     class Meta:
#         ordering=['-date_commande']


#     def __str__(self):
#         return f"{self.nom}"


# class Pretporter(models.Model):
#     title=models.CharField(max_length=200)
#     price=models.FloatField()
#     description=models.TextField()
#     image=models.ImageField(upload_to='static/album')
#     date_pret=models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering=['-date_pret']


#     def __str__(self):
#         return f"{self.title}"


# class Pagne(models.Model):
#     libelle=models.CharField(max_length=200)
#     price=models.FloatField()
#     description=models.TextField()
#     image=models.ImageField(upload_to='static/album')
#     date_pagne=models.DateTimeField(auto_now=True)


#     class Meta:
#         ordering=['-date_pagne']


#     def __str__(self):
#         return f"{self.libelle}"


