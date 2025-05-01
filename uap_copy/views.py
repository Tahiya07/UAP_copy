from django.shortcuts import render
from django.shortcuts import get_object_or_404



def home(request):
    return render(request, 'home.html')

def undergraduate(request):
    return render(request, 'hard_html/undergraduate.html')

def graduate(request):
    return render(request, 'hard_html/graduate.html')

def tuition(request):
    return render(request, 'hard_html/tuition.html')

def why_cse(request):
    return render(request, 'hard_html/why_cse.html')



def clubs(request):
    return render(request, 'hard_html/clubs.html')

def gallery(request):
    return render(request, 'hard_html/gallery.html')



