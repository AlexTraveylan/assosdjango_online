"# AssosDjango"

git remote add origin https://github.com/AlexTraveylan/AssosDjango.git
git branch -M main
git push -u origin main

---

#Ne pas oublié de creer la base de donnée avec python manage.py migrate

#Il y a un dossier .env à rajouter dans le dossier /assos dans lequel se trouve settings.py
#Il contient :
#- SECRET_KEY='****\*\*\*\*****\*\*****\*\*\*\*****\*\*\*****\*\*\*\*****\*\*****\*\*\*\*****' (secret ?)

#- DEBUG= True (or False)

#- ALLOWED_HOSTS= '127.0.0.1' (ou le nom de domaine en ligne)
