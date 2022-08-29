from django.http import HttpResponse
from django.shortcuts import render

data = {
  'movies': [
    {
      'id': 5,
      'title': 'Jawz',
      'year': 1696,
    },
    {
      'id': 6,
      'title': 'Sharknado',
      'year': 2001,
    },
    {
      'id': 7,
      'title': 'The Land Before Time',
      'year': 1999,
    }
  ]
}

def movies(req): 
  return render(req, 'movies/movies.html', data)

def home(req): 
  return HttpResponse("HOME")