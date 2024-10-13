from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from .forms import UserCreateForm, UserAuthenticationForm
from .models import Cheatsheet, Genre, Section, Author
import os
from django.utils.encoding import smart_str

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = UserAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def library(request):
    files = Cheatsheet.objects.all()
    genres = Genre.objects.all()
    sections = Section.objects.all()
    authors = Author.objects.all()

    # Применение фильтров
    genre_id = request.GET.get('genre')
    section_id = request.GET.get('section')
    author_id = request.GET.get('author')
    year = request.GET.get('year')

    if genre_id:
        files = files.filter(genre__id=genre_id)
    if section_id:
        files = files.filter(section__id=section_id)
    if author_id:
        files = files.filter(author__id=author_id)
    if year:
        files = files.filter(year=year)

    context = {
        'files': files,
        'genres': genres,
        'sections': sections,
        'authors': authors,
    }
    return render(request, 'library.html', context)


# Скачивание файла - НОВЫЙ ФУНКЦИОНАЛ

def download_cheatsheet(request, cheatsheet_id):
    cheatsheet = get_object_or_404(Cheatsheet, pk=cheatsheet_id)
    file_path = cheatsheet.file.path
    if os.path.exists(file_path):
        filename = os.path.basename(cheatsheet.file.name)
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
        return response
    raise Http404

@login_required
def profile(request):
    return render(request, 'profile.html')
