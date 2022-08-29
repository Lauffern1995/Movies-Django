
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie


def movies(req):
  data = Movie.objects.all()
  return render(req, 'movies/movies.html', {'movies': data})

def home(req): 
  return HttpResponse("HOME")

def detail(req, id): 
  data = Movie.objects.get(pk=id)
  return render(req, 'movies/detail.html', {'movie': data})

def add(req):
  title = req.POST.get('title')
  year = req.POST.get('year')

  if title and year: 
    movie = Movie(title=title, year=year)
    movie.save()
    return HttpResponseRedirect('/movies')

  return render(req, 'movies/add.html')

def delete(req, id): 
  try: 
    movie = Movie.objects.get(pk=id)
    
  except: 
    raise Http404('Movie does not exist')

  movie.delete()
    
  return HttpResponseRedirect('/movies')