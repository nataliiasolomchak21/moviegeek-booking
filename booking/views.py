from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def booking(request):
    return render(request, 'booking.html')