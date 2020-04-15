from django.shortcuts import render
from django.http import HttpResponse
from  django.template import loader
from django.shortcuts import get_object_or_404

from .models import Album, Artist, Contact, Booking
from .form import ContactForm
# Create your views here.
# Affiche la liste des albums disponible

def  index(request):

    # afficher les albums disponibles dont le parametre available est truels

    # Order_by permet d'ordonner la liste des albums selon la date de creation

    albums = Album.objects.filter(available = True).order_by('-created_at')[:12]

    #formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    #message = "<ul>{}</ul>".format("\n".join(formatted_albums))

    #template = loader.get_template('store/index.html')
    context = {'albums': albums}

    return render(request ,'store/index.html',context)

    #return HttpResponse(message)


# liste de tous les albums

def listing(request):

    albums = Album.objects.filter(available=True)
    #formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    #message = " <ul>{}</ul>".format("\n".join(formatted_albums))

    context = {'albums': albums}

    return render(request ,'store/listing.html',context)

# les caracteristique d'un specifique album

def detail(request, album_id):

    album = get_object_or_404(Album, pk = album_id)
    # album = Album.objects.get(pk = album_id)
    artists_name = " ".join([artist.name for artist in album.artist.all()])

    context = {
        'album_title': album.title,
        'artists_name': artists_name,
        'album_id': album_id,
        'thumbnail': album.picture
    }

    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            '''
            email = form.POST.get('email')
            name = form.POST.get('name')
            '''
            contact = Contact.objects.filter(email=email)
            if not contact.exists():
                # if a contact is not registered, create a new one.
                contact = Contact.objects.create(
                    email=email,
                    name=name
                )

            album = get_object_or_404(Album, id=album_id)


            booking = Booking.objects.create(
                contact=contact,
                album=album
            )

            album.available=False
            album.save()
            context = {
                'album_title':album.title
            }
            return  render(request, 'store/merci.html', context)
        else:
            context['errors'] = form.errors.items()
    #message = "Le nom de l'album est {}, il a été écrit par {}".format(album.title, artists)
    else:
        form = ContactForm()

    context['form'] = form

    return render(request ,'store/detail.html',context)

# page pour recherche un element dans ma base de données

def search(request):

    query = request.GET.get('query')

    if not query:

        albums = Album.objects.all()

    else:

        albums = Album.objects.filter(title__icontains = query)


        if not albums.exists():

            albums = Album.objects.filter(artist__name__icontains = query)

        '''
        if not albums.exists():

            message = " Misère de misère, nous n'avons trouvé aucun résultat ! "


        else:

            albums = ["<li>{}</li>".format(albums.title) for album in albums]

            message = """
               nous avons trouvé les albums correspondant à votre requete ! les voici : 
               <ul>{}</ul>""".format("<li></li>".join(albums))
    '''
    title = "Résiltats pour la requéte %s"%query
    context ={
        'albums': albums,
        'title': title,
    }


    return render(request ,'store/search.html',context)







