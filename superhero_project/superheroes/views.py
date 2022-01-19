from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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
  if request.method == 'POST':
    get = request.POST.get
    name = get('name')
    alter_ego = get('alter_ego')
    primary_ability = get('primary_ability')
    secondary_ability = get('secondary_ability')
    catchphrase = get('catchphrase')
    new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary_ability, secondary_ability=secondary_ability,catchphrase=catchphrase)
    new_hero.save()
    return HttpResponseRedirect(reverse('superheroes:index'))
  else:
    return render(request, 'superheroes/create.html')