from django.shortcuts import render

def index(request):
    # permissions = request.user
    return render(request, 'home/index.html')