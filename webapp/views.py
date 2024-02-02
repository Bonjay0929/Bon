from django.shortcuts import render, redirect
from .models import *
from .forms import AuthorForm


def homePage(request):
    author = Author.objects.all()
    genre =  Genre.objects.all()
    books =  Author.objects.all()
    contract_status =  AuthorContractStatus.objects.all()

    total_authors =  author.count()
    total_books = books.count()
    accepted = contract_status.filter(status='A').count()
    pending = contract_status.filter(status='P').count()

    context = {
        'author': author,
        'total_books': total_books,
        'total_authors': total_authors,
        'accepted': accepted,
        'pending': pending,

    }
    return render(request, 'pages/home.html', context)


def aboutPage(request):
    return render(request, 'pages/about.html')


def profilePage(request, pk):
    author = Author.objects.get(id=pk)
    books = author.books_set.all()
  

    context = {
        'author':author,
        'books':books,
    
    }
    return render(request, 'pages/profile.html', context)


def genrePage(request, pk):
    author = Author.objects.get(id=pk)
    books = author.books_set.all()
    

    context = {
        'author': author,
        'books': books,
        
    }
    return render(request, 'pages/genre.html', context)


def createAuthorPage(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homePage')

    context = {'form': form}
    return render(request, 'pages/author_form.html', context)


def updateAuthor(request, pk):
    author = Author.objects.get(id=pk)
    form = AuthorForm(instance= author)

    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('homePage')

    context = {'form': form}
    return render(request, 'pages/author_form.html', context)


def deleteAuthor(request, pk):
    author = Author.objects.get(id=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('homePage')

    return render(request, 'pages/delete_author.html')