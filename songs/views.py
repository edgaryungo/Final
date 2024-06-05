from django.shortcuts import render, redirect
from .models import Category, Song
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.contrib import messages
from .forms import SongForm, AlbumForm

# Create your views here.
@csrf_exempt
def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home-page')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.error(request, "Username OR Password does not exist")  

    context = {'page':page}
    return render(request, 'songs/login_register.html', context)
@csrf_exempt
def logoutPage(request):
    logout(request)
    return redirect('home-page')
    
    context = {}
    return render(request, 'songs/login_register.html', context)
@csrf_exempt
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    songs = Song.objects.filter(
        Q(category__name__icontains=q)|
        Q(album__name__icontains=q)|
        Q(name__icontains=q)|
        Q(body__icontains=q)
    )
    song_count = Song.objects.all().count()
    categories = Category.objects.all()
    
    context = {'songs':songs, 'categories':categories, 'song_count':song_count}
    return render(request, 'songs/home.html', context)

@csrf_exempt
def song(request, pk):
    song_room = Song.objects.get(id=pk)
    context = {'song_room': song_room}
    return render(request, 'songs/song.html', context)
@csrf_exempt
@login_required(login_url='login')
def addAlbum(request):
    move = 'addAlbum'
    album = AlbumForm()

    if request.method == 'POST':
        album = AlbumForm(request.POST)
        if album.is_valid():
            album.save()
            return redirect('add-song')
    context = {'album':album, 'move':move}
    return render(request, 'songs/song_form.html', context) 

# def editAlbum(request, pk):
@csrf_exempt
@login_required(login_url='login')
def addSong(request):
    step = 'add'
    form = SongForm()
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {'form':form, 'step':step}
    return render(request, 'songs/song_form.html', context)

@csrf_exempt
@login_required(login_url='login')
def editSong(request, pk):
    song = Song.objects.get(id=pk)
    form = SongForm(instance=song)
    # check if the its the owner
    if request.user != song.author:
        messages.error(request, "You are not allowed!")
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {'form':form}
    return render(request, 'songs/song_form.html', context)
@csrf_exempt
@login_required(login_url='login')
def deleteSong(request, pk):
    song = Song.objects.get(id=pk)

    # if request.user != room.host:
    #     return HttpResponse('You are not allowed')
    if request.method == 'POST':
        song.delete()
        return redirect('home-page')
    
    context = {'obj':song}
    return render(request, 'songs/delete.html', context)