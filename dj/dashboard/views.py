from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from khejas.models import Khejas

@login_required
def index(request):
    khejass = Khejas.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'khejass': khejass,
    })