from webbrowser import get
from .models import Superhero

def get_hero_context(hero_id):
  hero = Superhero.objects.get(pk=hero_id)
  return { 'hero': hero}

def save_hero_details(request, hero_id=None):
  hero = Superhero.objects.get(pk=hero_id) if hero_id else Superhero()
  hero.set(request)
  hero.save()

def delete_hero(hero_id):
  hero = Superhero.objects.get(pk=hero_id)
  hero.delete()