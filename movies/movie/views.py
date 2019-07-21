from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import connection
try:
    client = connection.Connection('root', 'root', '192.168.43.109', 6543)
except:
    pass


# Create your views here.


def index(request):
    global client
    client.use_database('movie')
    movie_table = client.table('movie')
    movies = movie_table.get_item()

    country_table = client.table('country')
    countries = country_table.get_item()

    director_table = client.table('director')
    directors = director_table.get_item()

    for i in range(0, len(movies)):
        for country in countries:
            if int(country['id']) == int(movies[i]['country_id']):
                movies[i]['country_name'] = country['name']
        for director in directors:
            if int(director['id']) == int(movies[i]['director_id']):
                movies[i]['director_name'] = director['first_name'] + " " + director['last_name']
    return render(request, 'movie/index.html', {'movies': movies})


def create_database(request):
    global client
    client.create_database('movie')
    client.use_database('movie')
    client.create_table('country', {'id': 'int', 'name': 'text'}, ['id'])
    client.create_table('director', {'id': 'int', 'first_name': 'text', 'last_name': 'text', 'date_of_birth': 'text'}, ['id'])
    client.create_table('movie', {'id': 'int', 'name': 'text', 'director_id': 'int', 'country_id': 'int', 'year': 'text', 'description': 'text'}, ['id'])
    return HttpResponse('Done')


def country(request):
    global client
    client.use_database('movie')
    table = client.table('country')
    rows = table.get_item()
    return render(request, 'movie/country.html', {'rows': rows})


def add_country(request):
    global client
    client.use_database('movie')
    table = client.table('country')
    id = request.POST['id']
    name = request.POST['name']
    table.put_item({'id': int(id), 'name': name})
    return HttpResponseRedirect(reverse('movie:country'))


def update_country(request):
    global client
    client.use_database('movie')
    table = client.table('country')
    id = request.POST['id']
    name = request.POST['name']
    table.update_item({'name': name}, {'id': int(id)})
    return HttpResponseRedirect(reverse('movie:country'))


def delete_country(request):
    global client
    client.use_database('movie')
    table = client.table('country')
    id = request.GET['id']
    table.delete_item({'id': int(id)})
    return HttpResponseRedirect(reverse('movie:country'))


def director(request):
    global client
    client.use_database('movie')
    table = client.table('director')
    rows = table.get_item()
    return render(request, 'movie/director.html', {'rows': rows})


def add_director(request):
    global client
    client.use_database('movie')
    table = client.table('director')
    id = request.POST['id']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    date_of_birth = request.POST['date_of_birth']
    table.put_item({'id': int(id), 'first_name': first_name, 'last_name': last_name, 'date_of_birth': date_of_birth})
    return HttpResponseRedirect(reverse('movie:director'))


def delete_director(request):
    global client
    client.use_database('movie')
    table = client.table('director')
    id = request.GET['id']
    table.delete_item({'id': int(id)})
    return HttpResponseRedirect(reverse('movie:director'))


def movie(request):
    global client
    client.use_database('movie')
    table1 = client.table('movie')
    rows = table1.get_item()

    table2 = client.table('director')
    directors = table2.get_item()

    table3 = client.table('country')
    countries = table3.get_item()
    return render(request, 'movie/movie.html', {'rows': rows, 'directors': directors, 'countries': countries})


def add_movie(request):
    global client
    client.use_database('movie')
    table = client.table('movie')
    id = int(request.POST['id'])
    name = request.POST['name']
    director_id = int(request.POST['director_id'])
    country_id = int(request.POST['country_id'])
    year = request.POST['year']
    description = request.POST['description']
    table.put_item({'id': id, 'name': name, 'director_id': director_id, 'country_id': country_id, 'year': year, 'description': description})
    return HttpResponseRedirect(reverse('movie:movie'))


def delete_movie(request):
    global client
    client.use_database('movie')
    table = client.table('movie')
    id = request.GET['id']
    table.delete_item({'id': int(id)})
    return HttpResponseRedirect(reverse('movie:movie'))
