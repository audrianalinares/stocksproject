from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

#pk_2d493df3ace74135846b58fb4fc7eeb9