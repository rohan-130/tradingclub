from django.shortcuts import render


def view_main_page(request):
    return render(request, 'mainPage.html')


def contact(request):
    return render(request, 'contact.html', {})


def portal(request):
    return render(request, 'portal.html')