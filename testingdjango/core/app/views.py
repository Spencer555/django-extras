from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from app.models import Book 
from django.views.generic import CreateView 
from django.utils.text import slugify
from app.forms import BookForm
import json 

# Create your views here.


def book_list(request):
    book_list = Book.objects.all()
    #templates not created 
    return render(request, 'bookList.html', {'book_list':book_list})


def book_detail(request, pk):
    book = get_object_or_404(Book, id=pk)


    if request.method == 'GET':
        return render(request, 'bookDetail.html', {'book_detail':book})


    elif request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data('title')
            cost = form.cleaned_data('cost')
            price = form.cleaned_data('price')
            Book.objects.create(
                title=title,
                cost=cost,
                price=price
            ).save()


    elif request.method == 'DELETE':
        id = json.loads(request.body)['id']
        book = Book.objects.get(id=id)
        book.delete()

        return HttpResponse(stauts=204)

    return redirect(book)



class BookCreateView(CreateView):
    model = Book 
    template_name = 'bookCreate.html'
    fields = ('title', 'cost', 'price')


    def form_valid(self, form):
        self.object = form.save()

        return redirect(self.object)