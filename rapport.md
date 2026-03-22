# **TAF 1 INF222 – EC1 : Développement Backend**

## **Nom :** TON NOM

## **Prénom :** TON PRÉNOM

## **Filière :** TA FILIÈRE

## **Matricule :** TON MATRICULE

## **UE :** INF222

---

# **INTRODUCTION**

Dans le cadre du cours INF222 portant sur le développement backend, ce travail pratique (TAF 1) a pour objectif de structurer notre apprentissage à l’aide de la plateforme CleeRoute, tout en développant une première API backend fonctionnelle.

Ce travail vise également à développer notre esprit critique vis-à-vis des outils d’apprentissage numériques, ainsi qu’à produire une application concrète sous forme d’une API de gestion d’articles de blog.

---

# **PARTIE 1 : UTILISATION DE CLEEROUTE**

## **Étape 1 : Création du compte**

J’ai créé un compte sur la plateforme CleeRoute en fournissant mes informations personnelles et en validant mon adresse email. Cette étape permet d’accéder aux fonctionnalités de la plateforme.

*(Insérer capture d’écran)*

---

## **Étape 2 : Définition du niveau et de l’objectif**

J’ai sélectionné mon niveau en développement web ainsi que mes objectifs d’apprentissage. Cela permet à la plateforme de proposer un parcours adapté.

*(Insérer capture d’écran)*

---

## **Étape 3 : Paramétrage du profil**

J’ai configuré mon profil en précisant mes centres d’intérêt et mes objectifs. Cela améliore la personnalisation du contenu proposé.

*(Insérer capture d’écran)*

---

## **Étape 4 : Génération du parcours**

La plateforme a généré automatiquement un parcours d’apprentissage structuré en modules.

*(Insérer capture d’écran)*

---

## **Étape 5 : Suivi des modules**

J’ai suivi plusieurs modules proposés, ce qui m’a permis de renforcer mes connaissances en développement backend.

*(Insérer capture d’écran)*

---

## **Étape 6 : Prise de notes**

J’ai utilisé la fonctionnalité de prise de notes pour résumer les concepts importants.

*(Insérer capture d’écran)*

---

## **Étape 7 : Ajout de sources et utilisation du chat**

J’ai ajouté des sources et utilisé l’assistant pour poser des questions et approfondir ma compréhension.

*(Insérer capture d’écran)*

---

## **Étape 8 : Quiz d’évaluation**

J’ai participé aux quiz pour évaluer ma compréhension des concepts appris.

*(Insérer capture d’écran)*

---

# **PARTIE 2 : DÉVELOPPEMENT DE L’API BACKEND**

## **Présentation du projet**

J’ai développé une API backend permettant de gérer un blog simple. Cette API permet de créer, lire, modifier, supprimer et rechercher des articles.

---

## **Technologies utilisées**

* Python
* Django
* Django REST Framework
* SQLite
* Swagger (drf-yasg)

---

## **Structure du projet**

Le projet est organisé comme suit :

* **models.py** : définit la structure des données (Article)
* **serializers.py** : gère la validation et la transformation des données
* **views.py** : contient la logique métier et les endpoints
* **urls.py** : définit les routes de l’API

Cette séparation respecte les bonnes pratiques de développement backend.

---

## **Fonctionnalités implémentées**

### ✔️ Création d’un article

Permet d’ajouter un nouvel article avec les champs : titre, contenu, auteur, catégorie et tags.

### ✔️ Lecture des articles

Permet de récupérer tous les articles ou un article spécifique via son ID.

### ✔️ Modification d’un article

Permet de modifier les informations d’un article existant.

### ✔️ Suppression d’un article

Permet de supprimer un article via son ID.

### ✔️ Recherche d’articles

Permet de rechercher des articles par mots-clés dans le titre ou le contenu.

### ✔️ Filtrage

Permet de filtrer les articles par catégorie, auteur ou date.

---

## **Documentation de l’API**

L’API est documentée avec Swagger, accessible via :

http://127.0.0.1:8000/swagger/

Cette interface permet de tester les endpoints directement.

*(Insérer capture d’écran Swagger)*

---

## **Bonnes pratiques appliquées**

* Validation des données via les serializers
* Utilisation des codes HTTP standards
* Organisation claire du projet
* Utilisation de Django REST Framework pour simplifier le développement

---

## **Lien du projet GitHub**

(Insérer ici le lien de ton dépôt GitHub)

---

# **PARTIE 3 : ANALYSE CRITIQUE DE CLEEROUTE**

## **Points forts**

* Parcours d’apprentissage structuré
* Interface intuitive et facile à utiliser
* Personnalisation du contenu
* Présence de quiz pour évaluer les connaissances

---

## **Points faibles**

* Manque de projets pratiques avancés
* Interface parfois lente
* Peu d’intégration avec des outils externes comme GitHub

---

## **Améliorations possibles**

* Ajouter des projets réels guidés
* Intégrer GitHub pour suivre les progrès
* Améliorer la performance de la plateforme

---

## **Utilité pour un étudiant**

CleeRoute est un outil utile pour structurer l’apprentissage et progresser de manière autonome en informatique, notamment pour les débutants.

---

# **CONCLUSION**

Ce travail m’a permis de découvrir et de maîtriser les bases du développement backend avec Django REST Framework. J’ai également appris à utiliser une plateforme d’apprentissage structurée comme CleeRoute.

La réalisation de cette API m’a permis de comprendre les concepts essentiels tels que les endpoints, la gestion des données et la documentation d’une API.

Ce TAF constitue une étape importante dans mon apprentissage du développement web backend.
