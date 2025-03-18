from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("Index Page Giz")
    
    
def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello  %s</h1>" %username)

def about(request):
    return HttpResponse('About')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects,safe = False)

def tasks(request, id):
    task =get_object_or_404(Task, id=id)
    return HttpResponse('task: ' % task.title)

def home(request):
    return render(request, 'Users/home.html')  # Importante incluir la subcarpeta 'Users/'
