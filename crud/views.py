from django.shortcuts import render
from django.http import HttpResponse
def agent(request):
   return render(request, 'agent.html')
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def blog_single(request):
    return render(request, 'blog_single.html')
def main(request):
    return render(request, 'main.html')
def properties(request):
    return render(request, 'properties.html')
def properties_single(request):
    return render(request, 'properties_single.html')
def services(request):
    return render(request, 'services.html')
def home(request):
    return render(request, 'home.html')
                