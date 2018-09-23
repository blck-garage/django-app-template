from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'message': '{{ app_name }} app works!' }
    return render(request, '{{ app_name }}/index.html', context)
