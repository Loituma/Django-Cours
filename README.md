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
- `\l` -> check si la bdd exite
- `\c mysite` -> Go dans ma bdd
- `\dt` -> Affiche les tables


Si problème avec la table appli_contact faire ces commandes dans la bdd
- `DROP TABLE appli_contact;`
- `CREATE TABLE appli_contact(id SERIAL PRIMARY KEY,nom VARCHAR(150),prenom VARCHAR(150),mail VARCHAR(50),titre VARCHAR(50),contenu VARCHAR(200),competence VARCHAR(250),date timestamp);`
