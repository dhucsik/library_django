from dataclasses import field
from django import forms
from .models import Loan, Reservations 

class LoanCreate(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ('member',)

class ReservationCreate(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ('member', 'reservation_date',)