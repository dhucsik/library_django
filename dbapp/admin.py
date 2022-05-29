from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Categories)
admin.site.register(Books)
admin.site.register(Authors)
admin.site.register(BookAuthor)
admin.site.register(MemberStatus)
admin.site.register(Members)
admin.site.register(ReservationStatus)
admin.site.register(Reservations)
admin.site.register(Loan)
admin.site.register(Fine)
admin.site.register(FinePayment)