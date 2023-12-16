# contacts/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

def contactList(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contactList.html', {'contacts': contacts})

def contactDetail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/contactDetail.html', {'contact': contact})

def contactCreate(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactList')
    else:
        form = ContactForm()
    return render(request, 'contacts/contactForm.html', {'form': form})

def contactEdit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contactList')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contactForm.html', {'form': form})

def contactDelete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contactList')
    return render(request, 'contacts/contactDelete.html', {'contact': contact})
