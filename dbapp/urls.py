from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('category/<int:c_id>', views.books_category),
    path('all_books/', views.all_books, name = 'all_books'),
    path('book/<int:book_id>', views.book),
    path('members/', views.member, name='members'),
    path('loans/', views.loan, name = 'loans'),
    path('reservations/', views.reservation, name = 'reservations'),
    path('transactions/', views.transaction, name = 'transactions'),
    path('popular_books/', views.popular_book, name = 'popular_books'),
    path('active_members/', views.active_member, name = 'active_members'),
    path('most_categories/', views.sort_category, name = 'sort_categories'),
    path('members_fine/', views.member_fine, name= 'members_fine'),
]