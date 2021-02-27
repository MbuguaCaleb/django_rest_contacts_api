**Create virtual environment**

```
pipenv shell

```

**Installing Django**

```
pipenv install django

```

**Starting a django project**

```
django-admin startproject contacsapi

```

**Running the Project**

```
python manage.py runserver

```

**Installing Django Rest Framework**

```
pipenv install djangorestframework

or

pip3 install djangorestframework

Remmber i am installing every dependency in my virtual enviroment hence the
reason i am running pipenv.

```

**Adding Authentication App**

```
python3 manage.py startapp authentication

```

**Migrations**

```
(a)Run migrations

python manage.py migrate

Serialisers are run directly.
There is no need to create a migration

(b)Making migration when i am using a model

python manage.py makemigrations
```

**Developed by**

```
MbuguaCaleb

```
