from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewKhejasForm, EditKhejasForm
from .models import Category, Khejas

def khejass(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    khejass = Khejas.objects.filter(is_vacant=False)

    if category_id:
        khejass = khejass.filter(category_id=category_id)

    if query:
        khejass = khejass.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'khejas/khejas.html', {
        'khejass': khejass,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def detail(request, pk):
    khejas = Khejas.objects.all()
    khejas = get_object_or_404(khejas, pk=pk)
    related_khejass = Khejas.objects.filter(category=khejas.category, is_vacant=False).exclude(pk=pk)[0:5]

    return render(request, 'khejas/detail.html', {
        'khejas': khejas,
        'related_khejass': related_khejass
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewKhejasForm(request.POST, request.FILES)

        if form.is_valid():
            khejas = form.save(commit=False)
            khejas.created_by = request.user
            khejas.save()

            return redirect('khejas:detail', pk=khejas.id)
    else:
        form = NewKhejasForm()

    return render(request, 'khejas/form.html', {
        'form': form,
        'title': 'New khejas',
    })

@login_required
def edit(request, pk):
    khejas = get_object_or_404(Khejas, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditKhejasForm(request.POST, request.FILES, instance=khejas)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=khejas.id)
    else:
        form = EditKhejasForm(instance=khejas)

    return render(request, 'khejas/form.html', {
        'form': form,
        'title': 'Edit khejas',
    })

@login_required
def delete(request, pk):
    khejas = get_object_or_404(Khejas, pk=pk, created_by=request.user)
    khejas.delete()

    return redirect('dashboard:index')