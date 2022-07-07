from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from .models import Portfolio, Contact

# Create your views here.
def portfolio(request, username):
    user_obj = get_object_or_404(User, username=username)

    if request.method == 'POST':
        sender = request.POST['sender']
        subject = request.POST['subject']
        name = request.POST['name']
        message = request.POST['message']

        c = Contact()
        c.reciever = user_obj
        c.sender = sender
        c.subject = subject
        c.name = name
        c.message = message
        c.save()

        user_obj.portfolio.contacts.add(c)
        user_obj.portfolio.save()

    context = {
        'user': user_obj
    }

    return render(request, 'portfolio/portfolio.html', context)
