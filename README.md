# Library management system

It is out final project for course 'Database Management Systems 2'.

Built in Python version 3.10.0, Django version 4.0.2.

![alt text](https://github.com/dhucsik/library_django/blob/main/main_page.png?raw=true)

## Our requirements

- Complexity and Completeness.

- Design(UI) and creativity.

- ERD.

- Functions and Procedures(at least 4).

- Cursor (at least 4).

- Triggers (at least 3).

## Installation

1. Clone this repository.

```bash
git clone git@github.com:dhucsik/library_django
```

2. Create virutal environment and install django.

3. All requirements for pip in requirements.txt file.

4. You have to change DATABASES dict in library>settings.py file.

- For 'NAME' you have to write your port and pluggable database which will connect to your app

- For 'USER' you have to write user which will connect to your pluggable database

- For 'PASSWORD' you have to write password by which user is identified.

5. 
``` bash
path> cd library
path\library> python manage.py runserver
```

## ERD

![alt text](https://github.com/dhucsik/library_django/blob/main/erd.png?raw=true)

## Functions and Procedures

```bash
create or replace procedure get_categories(c_id number)
is
    cursor c is 
    select books.id as id, books.title as title, categories.category_name as cat, books.publication_date as data from books 
    join categories on books.category_id = categories.id
    where category_id = c_id
    order by books.id;

    r_cat c%ROWTYPE;
begin
  open c;
  LOOP
    FETCH  c  INTO r_cat;
    EXIT WHEN c%NOTFOUND;

    DBMS_OUTPUT.PUT_LINE(r_cat.id || r_cat.title || r_cat.cat || r_cat.data);
  END LOOP;

  CLOSE c;
END;


create or replace procedure get_for_main_page
is
    cursor c is
    select books.id as id, books.title as title, categories.category_name as cat, books.publication_date as data 
    from books join categories on books.category_id = categories.id
    order by books.id
    FETCH NEXT 10 ROWS ONLY;

    r_cat c%ROWTYPE;
begin
  open c;
  LOOP
    FETCH  c  INTO r_cat;
    EXIT WHEN c%NOTFOUND;

    DBMS_OUTPUT.PUT_LINE(r_cat.id || r_cat.title || r_cat.cat || r_cat.data);
  END LOOP;

  CLOSE c;
END;


create or replace procedure loan_create(member_id in number, book_id in number)
is
    c number;
begin
    select count(*) into c from loan;
    insert into loan values(c+1, book_id, member_id, sysdate, sysdate + 7);
end;


create or replace procedure reservation_create(member_id in number, book_id in number, reservation_date in DATE)
is
    c number;
begin
    select count(*) into c from reservations;
    insert into reservations values(c+1, book_id, member_id, reservation_date, 2);
end;
```

## Cursors

In view.py file

1. def popular_book

2. def active_member

3. def sort_category

4. def member_fine

## Triggers

```bash
create or replace trigger create_tr
after insert or update on loan
for each row
declare
    v_transaction VARCHAR2(50);
    c number;
begin
   v_transaction := CASE 
        when inserting then 'Insert Loan'
         WHEN UPDATING THEN 'Update Loan'
   END;

   select count(*) into c from transactions;
   INSERT INTO transactions values(c+1, :new.member_id, :new.book_id, sysdate, v_transaction);
END;


create or replace trigger create_trrr
after insert or update on reservations
for each row
declare
    v_transaction VARCHAR2(50);
    c number;
begin
   v_transaction := CASE 
        when inserting then 'Insert Reservation'
         WHEN UPDATING THEN 'Update Reservation'
   END;

   select count(*) into c from transactions;
   INSERT INTO transactions values(c+1, :new.member_id, :new.book_id, sysdate, v_transaction);
END;
```