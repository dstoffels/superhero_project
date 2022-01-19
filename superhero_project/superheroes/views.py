import imp
from django.shortcuts import render
from .models import Superhero

# Create your views here.
def index(request):
  all_heroes = Superhero.objects.all()
  context = { 'all_heroes': all_heroes }
  return render(request, 'superheroes/index.html', context)

def detail(request, hero_id):
  hero = Superhero.objects.get(pk=hero_id)
  context = { 'hero': hero}
  return render(request, 'superheroes/detail.html', context)

def create(request):
  return render(request, 'superheroes/create.html')