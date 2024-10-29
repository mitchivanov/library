from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from .forms import UserCreateForm, UserAuthenticationForm, UserPreferenceForm
from .models import Cheatsheet, Genre, Section, Author, UserPreference
import os
from django.utils.encoding import smart_str


def index(request):
    return render(request, 'index.html')
 
def register(request): 
    if request.method == 'POST': 
        form = UserCreateForm(request.POST) 
        if form.is_valid(): 
            password = form.cleaned_data.get('password')
            password_confirm = form.cleaned_data.get('password_confirm')
            if password == password_confirm:
                form.save() 
                messages.success(request, 'Аккаунт успешно создан!') 
                return redirect('login')
            else:
                messages.error(request, 'Пароли не совпадают')
        else:
            messages.error(request, 'Проверьте введённые данные')
    else:
        form = UserCreateForm() 
    context = { 
        'form': form 
    } 
    return render(request, 'register.html', context) 

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
        files = files.filter(authors__id=author_id)  # Изменено с author на authors
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
    user_preference, _ = UserPreference.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        preference_form = UserPreferenceForm(request.POST, instance=user_preference)
        if preference_form.is_valid():
            preference_form.save()
            messages.success(request, 'Предпочтения успешно сохранены!')
            return redirect('profile')
    else:
        preference_form = UserPreferenceForm(instance=user_preference)
    
    context = {
        'preference_form': preference_form
    }
    return render(request, 'profile.html', context)

def user_logout(request):
    auth_logout(request)
    messages.success(request, 'Вы успешно вышли из системы')
    return redirect('index')

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = author.cheatsheets.all()
    
    context = {
        'author': author,
        'books': books
    }
    return render(request, 'author.html', context)

def read_book(request, cheatsheet_id):
    book = get_object_or_404(Cheatsheet, pk=cheatsheet_id)
    file_extension = book.file.name.split('.')[-1].lower()
    
    if file_extension == 'pdf':
        response = FileResponse(book.file, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{book.file.name}"'
        response['X-Frame-Options'] = 'SAMEORIGIN'
        return response
    
    context = {
        'book': book,
        'file_extension': file_extension,
    }
    return render(request, 'read_book.html', context)
