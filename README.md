"# AssosDjango"

---

Ne pas oublier de creer la base de donnée avec python manage.py migrate

Ne pas oublié d'installer avec pip install le contenu du fichier requirements.txt (pip install -r requirements.txt)

Il y a un dossier .env à rajouter dans le dossier /assos/assos/ dans lequel se trouve settings.py

Il contient :

- SECRET_KEY='\***\*\*\*\*\*\*\***\*\*\***\*\*\*\*\*\*\***\*\*\*\***\*\*\*\*\*\*\***\*\*\***\*\*\*\*\*\*\***' (secret ?)
- DEBUG= True (or False)
- ALLOWED_HOSTS= '127.0.0.1' (ou le nom de domaine en ligne)
