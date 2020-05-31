from django.shortcuts import render


def homePage(request):
    return render(request, 'index.html')

def menuPage(request):
    return render(request, 'menu.html')

def aboutPage(request):
    return render(request, 'about.html')
