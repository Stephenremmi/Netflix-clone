from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Film
from .forms import NetflixFilmForm, NetflixLetterForm
# Create your views here.
def index(request):
    return render(request, "netflix/index.html")

@login_required(login_url='/accounts/login/')
def film(request,film_id):
    try:
        film = Film.objects.get(id = film_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"film":film})

@login_required(login_url='/accounts/login/')
def new_film(request):
    current_user = request.user
    if request.method == 'POST':
        form = NetfilxFormForm(request.POST, request.FILES)
        if form.is_valid():
            film = form.save(commit=False)
            film.editor = current_user
            film.save()
        return redirect('newsToday')

    else:
        form = NetlixFilmForm()
    return render(request, 'new_article.html', {"form": form})