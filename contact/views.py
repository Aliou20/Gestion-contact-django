from django.shortcuts import render , get_object_or_404 , redirect
from .models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    message = "Bonjour tous le monde !"
    return render(request , 'Pages/index.html' , {"message" : message})


def about(request):
    message = "vous etez sur about"
    return render(request , 'Pages/about.html' , {"message" : message })


@login_required(login_url="/login/")
def contact_list(request):
    user  = request.user
    contacts = Contact.objects.filter(auteur=user , archiver=False)
    return render(request , "Contacts/contact_list.html" , {"contacts" : contacts})

@login_required(login_url="/login/")
def contact_detail(request , id):
    contacts = get_object_or_404(Contact , id = id)
    print(contacts)
    return render(request , 'contacts/contact_detail.html' , {'contact' : contacts})

@login_required(login_url="/login/")
def new_contact(request):
    if request.method == 'POST':
        auteur = request.user
        nom = request.POST["nom"]
        prenom = request.POST["prenom"]
        telephone = request.POST["telephone"]
        email = request.POST["email"]

        contact = Contact.objects.create(auteur=auteur,nom=nom,prenom=prenom,telephone=telephone,email=email)
        contact.save()
        return redirect('/contacts/')
    return render(request , 'Contacts/contact_new.html')


@login_required(login_url="/login/")
def edit_contact(request ,id):
    contact = get_object_or_404(Contact , id=id)
    if request.method == "POST":
        nom = request.POST["nom"]
        prenom = request.POST["prenom"]
        telephone = request.POST["telephone"]
        email = request.POST["email"]
        contact = Contact.objects.filter(pk=contact.id).update(
            nom = nom , 
            prenom = prenom,
            telephone = telephone,
            email = email   
        )

        return redirect("/contacts")
    return render(request , 'Contacts/contact_edit.html' , {'contact': contact})


@login_required(login_url="/login/")
def delete_contact(request , id):
    contact = get_object_or_404(Contact ,id=id)
    if request.method == 'POST':
        Contact.objects.filter(pk = contact.id).update(archiver = True)
        return redirect("/contacts")
    return render(request , 'Contacts/contact_delete.html' , {"contact" : contact})
