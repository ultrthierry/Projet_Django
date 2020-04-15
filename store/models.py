from django.db import models

# Create your models here.

class Artist(models.Model):

    name = models.CharField(max_length= 200, unique= True)

    #
    def __str__(self):
        return self.name

class Contact(models.Model):

    objects = models.Manager()
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Album(models.Model):

    objects = models.Manager()
    reference = models.IntegerField(null=True)  # null = True c.a.d optionnel
    created_at = models.DateTimeField(auto_now_add= True) # auto_now_add = True permet d'enregistre automatique la date d'enregistrement de l'objet
    available = models.BooleanField(default=True) # default = true signifie que l'album est disponible a peine enregistre dans la base de donnees
    title = models.CharField(max_length=200)
    picture = models.URLField(max_length=600, null= True)  # lien vers l'image de l'album
    artist = models.ManyToManyField(Artist, related_name='albums', blank=True) # related_name te permet de  connaitre tous les albums d'un artiste

    def __str__(self):
        return self.title



class Booking(models.Model):

    objects = models.Manager()
    created_at = models.DateTimeField(auto_now_add= True)
    contacted = models.BooleanField(default= False) # indique si la demande a ete traite ou pas
    contact = models.ForeignKey(Contact, on_delete= models.CASCADE) # on_delete permet de supprimer toutes les reservations qd le contact est supprmé et ne supprime pas le contact si une reservation est suprimée
    album = models.OneToOneField(Album, on_delete= models.CASCADE)


    def __str__(self):
        return self.contact.name


