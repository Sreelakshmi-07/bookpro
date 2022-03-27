from django.shortcuts import render, redirect
from book_form.forms import BookForm
from django.views.generic import View
from book_form.models import Books


# Create your views here.
class BookView(View):
    def get(self, request):
        form = BookForm()
        return render(request, "book_add.html", {"form": form})

    def post(self, request):
        form = BookForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data.get("book_name"))
            # print(form.cleaned_data.get("author"))
            # print(form.cleaned_data.get("price"))
            # print(form.cleaned_data.get("copies"))
            # qs = Books(
            #     book_name=form.cleaned_data.get("book_name"),
            #     author=form.cleaned_data.get("author"),
            #     amount=form.cleaned_data.get("price"),
            #     copies=form.cleaned_data.get("copies")
            #
            # )
            # qs.save()

            return redirect("listbook")
        else:
            return render(request, "book_add.html", {"form": form})


class BookListView(View):
    def get(self, request):
        qs = Books.objects.all()
        return render(request, 'book_list.html', {'books': qs})


class BookUpdate(View):
    def get(self, request, *args, **kwargs):
        qs = Books.objects.get(id=kwargs.get("id"))
        form = BookForm(instance=qs)
        return render(request, "book_edit.html", {'form': form})

    def post(self, request, *args, **kwargs):
        qs = Books.objects.get(id=kwargs.get("id"))
        form = BookForm(request.POST, instance=qs,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listbook")


class BookDetails(View):
    def get(self, request, **kwargs):
        # pass
        # kwargs = {'id':3}
        qs = Books.objects.get(id=kwargs.get("id"))
        return render(request, "book_details.html", {'book': qs})


class BookDelete(View):
    def get(self, request, **kwargs):
        qs = Books.objects.get(id=kwargs.get("id"))
        qs.delete()
        return redirect("listbook")
