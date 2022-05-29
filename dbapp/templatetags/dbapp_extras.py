from django import template
from dbapp.models import *
register = template.Library()

@register.simple_tag()
def get_books_limit(sort=None):
    if not sort:
        return Books.objects.all()
    else:
        return Books.objects.order_by(sort)[:10]

@register.simple_tag()
def get_categories():
    return Categories.objects.all()

@register.simple_tag()
def get_books_all(sort=None):
    if not sort:
        return Books.objects.all()
    else:
        return Books.objects.order_by(sort)

@register.simple_tag()
def get_author(filter=None):
    if not filter:
        return Authors.objects.all()
    else:
        return Authors.objects.get(pk=filter)

@register.simple_tag()
def get_members(sort=None):
    if not sort:
        return Members.objects.all()
    else:
        return Members.objects.order_by(sort)
    
@register.simple_tag()
def get_loans(sort=None):
    if not sort:
        return Loan.objects.all()
    else:
        return Loan.objects.order_by(sort)

@register.simple_tag()
def get_reservations(sort=None):
    if not sort:
        return Reservations.objects.all()
    else:
        return Reservations.objects.order_by(sort)

@register.simple_tag()
def get_transactions(sort=None):
    if not sort:
        return Transactions.objects.all()
    else:
        return Transactions.objects.order_by(sort)
    