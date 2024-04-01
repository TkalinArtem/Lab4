from django.shortcuts import render, redirect, get_object_or_404

from .forms import BookForm
from .models import Books, Author


def index(request):
    return render(request, 'crud/base.html', {'block_name': 'crud/template_menu.html'})

def read(request):
    books = Books.objects.all()  # Отримуємо всі книги з бази даних
    search_query = request.GET.get('q', '')  # Отримуємо пошуковий запит з GET-параметра 'q'

    if search_query:
        # Якщо є пошуковий запит, фільтруємо книги за назвою
        books = books.filter(title__icontains=search_query)

    context = {
        'books': books,
        'block_name': 'crud/template_read.html',
    }
    return render(request, 'crud/base.html', context)

def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('read_books')
        else:
            print("Помилка")
    else:
        form = BookForm()

        # Фільтрація авторів за введеним ім'ям
    author_name = request.GET.get('author_name', '')
    authors = Author.objects.filter(name__icontains=author_name)

    context = {
        'form': form,
        'block_name': 'crud/template_create.html',
        'authors': authors
    }

    return render(request, 'crud/base.html', context)

def delete(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('read_books')

    context = {
        'book': book,
        'block_name': 'crud/template_delete.html',
        'book_id': book_id,
    }
    return render(request, 'crud/base.html', context)


def update(request, book_id):
    book = get_object_or_404(Books, pk=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('read_books')
        else:
            print('Form is not valid')
    else:
        form = BookForm(instance=book)

    authors = Author.objects.all()  # Отримуємо всіх авторів

    context = {
        'book': book,
        'form': form,
        'authors': authors,  # Передаємо авторів у контекст
        'block_name': 'crud/template_update.html',
    }
    return render(request, 'crud/base.html', context)