 API Backend
 
 - Gestion de Blog (TAF 1)Ce projet consiste en une API RESTful développée avec Python et Flask pour la gestion des articles d'un blog. Il a été réalisé dans le cadre de l'UE INF222 Programmation Web.
 
 -  Technologies utiliséesLangage :
        Python 3Framework
        FlaskBase de données
        SQLite (via Flask-SQLAlchemy)Architecture
        Blueprints pour la séparation des routes Installation et lancement extraction/Clonage du projet
 Placez-vous dans le dossier racine du projet.

Installation des dépendances 
Assurez-vous d'avoir Python installé, puis exécutez :Bashpip install flask flask-sqlalchemy

Initialisation de la base de données :Le code est configuré pour créer automatiquement le fichier blog.db au premier lancement.Lancement du serveur :Bashpython app.py

L'API sera disponible sur http://127.0.0.1:5000. 
Documentation des Endpoints1. 
ArticlesMéthodeEndpointDescriptionPOST/api/articlesCréer un nouvel articleGET/api/articles Lister tous les articles (Filtres possibles : auteur, date)GET/api/articles/<id> Récupérer un article spécifique via son 
IDPUT/api/articles/<id> Modifier un article existant
DELETE/api/articles/<id> Supprimer un article
GET/api/articles/searchRechercher par titre (Paramètre titre requis)🧪 Exemples d'utilisation (JSON)Création d'un article 

(POST /api/articles)Payload :JSON{
    "titre": "Mon premier article",
    "contenu": "Ceci est le contenu de mon article de test.",
    "auteur": "Wansi"
}
Modification d'un article (PUT /api/articles/2)Payload :JSON{
    "titre": "Titre Modifié",
    "contenu": "Contenu mis à jour.",
    "auteur": "Wansi"
}
Recherche d'un article (GET /api/articles/search?titre=premier) Renvoie la liste des articles dont le titre contient "premier".
Codes de réponse HTTP gérés
200 OK : Requête réussie.
201 Created : Article créé avec succès.
400 Bad Request : Paramètres manquants (titre, contenu ou auteur).
404 Not Found : L'article demandé n'existe pas dans la base de données.
Structure du projetapp.py : Point d'entrée et configuration de l'application.extensions.py
Initialisation de l'instance SQLAlchemy.
models.py : Modèle de données Article et méthode de sérialisation.routes.py 
Logique des points de terminaison (Blueprints).
