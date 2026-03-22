# INF222_Backend_Blog_Ec1
depot des devoirs d'info 222 Ec1 


 #  API Blog - Django REST Framework

    ##   Description
    Cette API permet de gérer un blog simple avec les fonctionnalités suivantes :
    - Création d’articles
    - Lecture (liste et détail)
    - Modification
    - Suppression
    - Recherche d’articles
    - Filtrage par catégorie, auteur et date
    
    Cette API a été développée dans le cadre du cours INF222 – Développement Backend.

---

## ⚙️ Technologies utilisées
    - Python
    - Django
    - Django REST Framework
    - SQLite
    - Swagger (drf-yasg)
    
    ---

##  Installation

### 1. Cloner le projet
```bash
git clone https://github.com/ton-username/INF222_Backend_Blog.git
cd INF222_Backend_Blog
```
### 2. Créer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate  # Linux
```
### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```
### 4. Appliquer les migrations
```bash
python manage.py migrate
```

### 5. Lancer le serveur, Accès : http://127.0.0.1:8000/
```bash
python manage.py runserver
```
### 6.Documentation API (Swagger)
   http://127.0.0.1:8000/swagger/

### endpoints 
      
    Méthode	Endpoint	Description	Codes HTTP
    POST	/api/articles/	Créer un article	201 Created, 400 Bad Request
    GET	/api/articles/	Lister tous les articles	200 OK
    GET	/api/articles/{id}/	Récupérer un article	200 OK, 404 Not Found
    PUT	/api/articles/{id}/	Modifier un article	200 OK, 400, 404
    DELETE	/api/articles/{id}/	Supprimer un article	204 No Content, 404
    GET	/api/articles/search/?query=texte	Rechercher dans titre/contenu	200 OK
    GET	/api/articles/?categorie=Tech	Filtrer par catégorie	200 OK
    GET	/api/articles/?auteur=Pierre	Filtrer par auteur	200 OK

### Modèle de données

    Article
    Champ	Type	Description	Validation
    id	AutoField	Identifiant unique	Généré automatiquement
    titre	CharField(255)	Titre de l'article	Obligatoire, non vide nomee title 
    contenu	TextField	Contenu de l'article	Min. 10 caractères 
    auteur	CharField(100)	Nom de l'auteur	Obligatoire nomee autor 
    date	DateTimeField	Date de création	Générée automatiquement nomee date 
    categorie	CharField(100)	Catégorie	Optionnel nomee category
    tags	CharField(255)	Tags	Optionnel

 ### Exemples de requêtes
     
    Créer un article (POST /api/articles/)

Requête :
     json
     
     {
       "titre": "Mon premier article",
       "contenu": "Ceci est le contenu de mon article",
       "auteur": "Pierre",
       "categorie": "Tech",
       "tags": "django,api"
     }

# Réponse (201 Created) :
     json
     
     {
       "id": 1,
       "titre": "Mon premier article",
       "contenu": "Ceci est le contenu de mon article",
       "auteur": "Pierre",
       "date": "2026-03-22T10:30:00Z",
       "categorie": "Tech",
       "tags": "django,api"
     }

Rechercher des articles (GET /api/articles/search/?query=django)

Réponse (200 OK) :
json
    
    [
      {
        "id": 1,
        "titre": "Mon premier article",
        "contenu": "Ceci est le contenu de mon article",
        "auteur": "Pierre",
        "date": "2026-03-22T10:30:00Z",
        "categorie": "Tech",
        "tags": "django,api"
      }
    ]

### Bonnes pratiques implémentées
    
    Bonne pratique	Implémentation
    Validation des entrées	Dans serializers.py (titre et auteur obligatoires, contenu min. 10 caractères)
    Codes HTTP appropriés	200, 201, 400, 404, 204, 500
    Séparation des responsabilités	Modèles (models.py), vues (views.py), sérialiseurs (serializers.py)
    Documentation API	Swagger (/swagger/)
    Recherche multi-champs	Utilisation des Q objects de Django
    Filtrage dynamique	Surcharge de get_queryset()

#### Dépendances
  
     Django==6.0.1
     djangorestframework==3.15.2
     drf-yasg==1.21.7
     requests==2.32.3

 ### Liens utiles

    Dépôt GitHub : https://github.com/votre-utilisateur/blog-api

    Documentation Swagger : http://127.0.0.1:8000/swagger/

### Auteur

    Nom	:Pierre Landry Nkoa 
    Filière	:Informatique 
    UE	:INF222

 ### Licence
    
    Ce projet est réalisé dans le cadre pédagogique de l'UE INF222.

Date de soumission : 23/03/2026


  

 
 












