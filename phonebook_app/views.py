
from django.shortcuts import render
from phonebook_app.models import Contact

def search(request):
    query = request.GET.get('query')
    if query:
        contacts = Contact.objects.filter(name__icontains=query)
    else:
        contacts = []
    return render(request, 'phonebook_app/search.html', {'contacts': contacts})
