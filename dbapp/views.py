from datetime import timedelta
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from .forms import LoanCreate, ReservationCreate
from .models import *
import cx_Oracle

# Create your views here.
connection = cx_Oracle.connect('djangousr','pswd','localhost:1521/pdb1')

def index(request):
    return render(request, 'dbapp/index.html')

def books_category(request, c_id):
    c_id = int(c_id)
    try:
        books = Books.objects.filter(category = c_id)
    except Books.DoesNotExist:
        return redirect('home')
    return render(request, 'dbapp/category.html', {'books' : books})

def all_books(request):
    return render(request, 'dbapp/all_books.html')

def book(request, book_id):
    book_id = int(book_id)
    if request.method == 'POST':
        if 'reservation_date' not in request.POST:
            form = LoanCreate(request.POST)
            if form.is_valid():
                loan = form.save(commit=False)
                loan.id = int(Loan.objects.last().id) + 1
                loan.book = Books.objects.get(pk = book_id)
                loan.loan_date = timezone.now()
                loan.return_date = timezone.now() + timedelta(7)
                loan.save()
                return redirect('home')
            else:
                return HttpResponse("""your form is wrong, reload on <a href = "{% url 'home' %}">reload</a>""")
        else:
            form = ReservationCreate(request.POST)
            if form.is_valid():
                reservation = form.save(commit=False)
                reservation.id = int(Reservations.objects.last().id) + 1
                reservation.book = Books.objects.get(pk = book_id)
                reservation.reservation_status = ReservationStatus.objects.get(pk = 2)
                reservation.save()
                return redirect('home')
            else:
                return HttpResponse("""your form is wrong, reload on <a href = "{% url 'home' %}">reload</a>""")
    else:
        form = LoanCreate()
        reform = ReservationCreate()
        try:
            kitap = Books.objects.get(pk = book_id)
        except:
            return redirect('home')
        return render(request, 'dbapp/book.html', {'book' : kitap, 'loan_form' : form, 'reservation_form' : reform})

def member(request):
    return render(request, 'dbapp/members.html')

def loan(request):
    return render(request, 'dbapp/loans.html')

def reservation(request):
    return render(request, 'dbapp/reservations.html')

def transaction(request):
    return render(request, 'dbapp/transactions.html')

def popular_book(request):
    cursor = connection.cursor()
    cursor.execute("""select books.title as book, authors.first_name as author, count(*) as loans from loan
            join books
            on loan.book_id = books.id 
            join authors 
            on books.id = authors.id
            group by books.title, authors.first_name
            order by 3 desc""")
    rows = cursor.fetchall()
    return render(request, "dbapp/popular_book.html", {'data' : rows})

def active_member(request):
    cursor = connection.cursor()
    cursor.execute("""select members.first_name as name, members.last_name as last_name, count(*) as loans from loan
            join members
            on loan.member_id = members.id
            group by members.first_name, members.last_name
            order by 3 desc""")
    rows = cursor.fetchall()
    return render(request, "dbapp/active_members.html", {'data' : rows})

def sort_category(request):
    cursor = connection.cursor()
    cursor.execute("""select categories.category_name as cat_name, count(*) as books_c from books
            join categories
            on categories.id = books.category_id
            group by categories.category_name
            order by 2 desc""")
    rows = cursor.fetchall()
    return render(request, "dbapp/most_categories.html", {'data' : rows})

def member_fine(request):
    cursor = connection.cursor()
    cursor.execute("""select members.first_name as name, members.last_name as last_name, sum(fine.fine_amount) as amount from fine
            join members
            on members.id = fine.member_id
            group by members.first_name, members.last_name
            order by 3 desc""")
    rows = cursor.fetchall()
    return render(request, "dbapp/members_fine.html", {'data' : rows})


def loan_create(request, member_id, book_id):
    cursor = connection.cursor()
    cursor.callproc('loan_create', [member_id, book_id])
    cursor.close()
    return redirect('home')


def reservation_create(request, member_id, book_id, reservation_date):
    cursor = connection.cursor()
    cursor.callproc('reservation_create', [member_id, book_id, reservation_date])
    cursor.close()
    return redirect('home')


def get_categories(request, category_id):
    cursor = connection.cursor()
    rows = cursor.callproc('get_categories', [category_id])
    cursor.close()
    return render(request, "dbapp/category.html", {'data':rows})

def main_page(request):
    cursor = connection.cursor()
    rows = cursor.callproc('get_for_main_page')
    cursor.close()
    return render(request, "dbapp/index.html", {'data':rows})