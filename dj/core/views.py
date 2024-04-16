from django.shortcuts import render, redirect

from khejas.models import Category, Khejas

from .forms import SignupForm

def index(request):
    khejass = Khejas.objects.filter(is_vacant=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'khejass': khejass,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })