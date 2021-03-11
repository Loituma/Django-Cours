# Cours python-django

Utilisation de docker pour avoir une bdd postgre et lancer l'application django.

## Utilisation

Dans app:
- `source env/bin/activate`
- `django-admin.py startapp appli` -> Create a new app


Pour utiliser manager.py

- `docker-compose exec web python manage.py createsuperuser`
- `docker-compose exec web python manage.py makemigrations`
- `docker-compose exec web python manage.py migrate`

Pour voir la bdd:
- `docker-compose exec db psql --username=user --dbname=mysite`
- `\\l` -> check si la bdd exite
- `\\c mysite` -> Go dans ma bdd
- `\\dt` -> Affiche les tables