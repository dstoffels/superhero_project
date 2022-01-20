from django.db import models

# Create your models here.
class Superhero(models.Model):
  name = models.CharField(max_length=50)
  alter_ego = models.CharField(max_length=50)
  primary_ability = models.CharField(max_length=50)
  secondary_ability = models.CharField(max_length=50)
  catchphrase = models.CharField(max_length=50)
  image = models.FileField(upload_to='images/', default='')

  def set(self, request):
    post = request.POST
    files = request.FILES

    self.name = post['name']
    self.alter_ego = post['alter_ego']
    self.primary_ability = post['primary_ability']
    self.secondary_ability = post['secondary_ability']
    self.catchphrase = post['catchphrase']
    self.image = files['image']

  def __str__(self): return self.name
