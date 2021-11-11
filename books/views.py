from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Book, User 
from .forms import BookForm

# Create your views here.


def homepage(request):
    if request.user.is_authenticated:
        return redirect("list_books")
    return render(request, "books/homepage.html")


def list_books(request):
    book = Book.objects.all().order_by("created_at")
    return render(request, "books/list_books.html")

@login_required
def add_book(request):
    if request.method == "POST":
        form = BookForm(data=request.POST)
        if form.is_Valid():
            book = form.save(commit=False)
            book.save()
            return redirect("show_book", pk=book.pk)
    else:
        form = BookForm()

    return render(request, "books/add_book.html", {"form": form})


@login_required
def show_book(request):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/show_book.html", {"book": book})

@login_required
def edit_book(request):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "GET":
        form = BookForm(instance=book)
    else:
        form = BookForm(data=request.POST, instance=book)
        if form.is_Valid():
            book.save()
            return redirect("list_books")
    
    return render(request, "books/edit_book.html", {"form": form, "book": book})

@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method =="POST":
        book.delete()
        messages.success(request, "Book deleted.")
        return redirect("list_books")

    return render(request, "books/delete_book.html", {"book", book})

