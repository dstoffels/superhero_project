from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render

from .helpers import hero_details_context, save_hero_details
from .models import Superhero

# Create your views here.
def index(request):
  all_heroes = Superhero.objects.all()
  context = { 'all_heroes': all_heroes }
  return render(request, 'superheroes/index.html', context)

def detail(request, hero_id):
  context = hero_details_context(hero_id)
  return render(request, 'superheroes/detail.html', context)

def create(request):
  if request.method == 'POST':
    save_hero_details(request)
    return HttpResponseRedirect(reverse('superheroes:index'))
  else:
    return render(request, 'superheroes/create.html')

def edit(request, hero_id):
  context = hero_details_context(hero_id)
  if request.method == 'POST':
    save_hero_details(request, hero_id)
    return HttpResponseRedirect(reverse(f'superheroes:detail', args=(hero_id,)))
  else:
    return render(request, 'superheroes/edit.html', context)

def delete(request, hero_id):
  hero = Superhero.objects.get(pk=hero_id)
  hero.delete()
  