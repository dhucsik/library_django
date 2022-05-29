from django.db import models

# Create your models here.

class Categories(models.Model):
    id = models.FloatField(primary_key=True)
    category_name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'categories'

class Books(models.Model):
    id = models.FloatField(primary_key=True)
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Categories, models.DO_NOTHING)
    publication_date = models.DateField()
    copies_owned = models.FloatField()

    class Meta:
        managed = True
        db_table = 'books'
    
    @property
    def get_category(self):
        return self.category.category_name

class Authors(models.Model):
    id = models.FloatField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'authors'


class BookAuthor(models.Model):
    id = models.FloatField(primary_key=True)
    book = models.ForeignKey('Books', models.DO_NOTHING)
    author = models.ForeignKey(Authors, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'book_author'


class MemberStatus(models.Model):
    id = models.FloatField(primary_key=True)
    status_value = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'member_status'

class Members(models.Model):
    id = models.FloatField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    joined_date = models.DateField()
    active_status = models.ForeignKey(MemberStatus, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'members'

    @property
    def get_status(self):
        return self.active_status.status_value


class ReservationStatus(models.Model):
    id = models.FloatField(primary_key=True)
    status_value = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'reservation_status'

class Reservations(models.Model):
    id = models.FloatField(primary_key=True)
    book = models.ForeignKey(Books, models.DO_NOTHING)
    member = models.ForeignKey(Members, models.DO_NOTHING)
    reservation_date = models.DateField()
    reservation_status = models.ForeignKey(ReservationStatus, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'reservations'

    @property
    def get_book(self):
        return self.book.title

    @property
    def get_member(self):
        return self.member

    @property
    def get_status(self):
        return self.reservation_status.status_value

class Loan(models.Model):
    id = models.FloatField(primary_key=True)
    book = models.ForeignKey(Books, models.DO_NOTHING)
    member = models.ForeignKey(Members, models.DO_NOTHING)
    loan_date = models.DateField()
    return_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'loan'

    @property
    def get_book(self):
        return self.book.title

    @property
    def get_member(self):
        return self.member

class FinePayment(models.Model):
    id = models.FloatField(primary_key=True)
    member_id = models.FloatField()
    payment_date = models.DateField()
    payment_amount = models.FloatField()

    class Meta:
        managed = True
        db_table = 'fine_payment'

class Fine(models.Model):
    id = models.FloatField(primary_key=True)
    member = models.ForeignKey(Members, models.DO_NOTHING)
    loan = models.ForeignKey(Loan, models.DO_NOTHING)
    fine_date = models.DateField()
    fine_amount = models.FloatField()

    class Meta:
        managed = True
        db_table = 'fine'

class Transactions(models.Model):
    id = models.FloatField(primary_key=True)
    member = models.ForeignKey(Members, models.DO_NOTHING)
    book = models.ForeignKey(Books, models.DO_NOTHING)
    tr_date = models.DateField()
    action = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'transactions'

    @property
    def get_book(self):
        return self.book.title

    @property
    def get_member(self):
        return self.member