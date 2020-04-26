from django.shortcuts import render, redirect
from .models import book
from .forms import bookCreate
from django.http import HttpResponse

#DataFlair
def index(request):
	shelf = book.objects.all()
	return render(request, 'book/library.html', {'shelf': shelf})

def upload(request):
	upload =          bookCreate()
	if request.method == 'POST':
		upload = bookCreate(request.POST, request.FILES)
		if upload.is_valid():
			upload.save()
			return redirect('index')
		else:
			return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
	else:
		return render(request, 'book/upload_form.html', {'upload_form':upload})

def update_book(request, book_id):
	book_id = int(book_id)
	try:
		book_sel = book.objects.get(id = book_id)
	except book.DoesNotExist:
		return redirect('index')
	book_form = bookCreate(request.POST or None, instance = book_sel)
	if book_form.is_valid():
		book_form.save()
		return redirect('index')
	return render(request, 'book/upload_form.html', {'upload_form':book_form})

def delete_book(request, book_id):
	book_id = int(book_id)
	try:
		book_sel = book.objects.get(id = book_id)
	except book.DoesNotExist:
		return redirect('index')
	book_sel.delete()
	return redirect('index')
