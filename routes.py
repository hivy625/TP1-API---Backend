from flask import Blueprint, jsonify,request
from extensions import db
from models import Article
from datetime import datetime

articles_bp = Blueprint('articles', __name__)

#route pour creer des articles

@articles_bp.route('/api/articles', methods=['POST'])
def creer_articles():
    data = request.get_json()

    #validation des champs
    if not data.get('titre') or not data.get('contenu') or not data.get('auteur'):
        return jsonify({'message': 'le titre, le contenu et l\'auteur sont obligatoires'}),400

    a = Article(
        titre=data['titre'],
        contenu=data['contenu'],
        auteur=data['auteur'],
        date=datetime.now()
    )
    db.session.add(a)
    db.session.commit()
    return jsonify({'message': 'article cree avec success','article':a.mise_dictionnaire()}),201

#route pour recuperer tous les articles

@articles_bp.route('/api/articles',methods=['GET'])
def recuperer_articles():
    auteur = request.args.get('auteur')
    date = request.args.get('date')

    query = Article.query
    if auteur:
        query = query.filter_by(auteur=auteur)
    if date:
        query = query.filter_by(date=date)

    articles = query.all()
    return jsonify({'articles': [a.mise_dictionnaire() for a in articles]}), 200

#recuperer les articles par id
@articles_bp.route('/api/articles/<int:id>',methods=['GET'])
def recuperer_article(id):
    a = Article.query.get_or_404(id)
    if not a:
        return jsonify({'messsage': 'article non trouve'}), 404
    return jsonify({'article': a.mise_dictionnaire()}), 200

#route pour modifier un article

@articles_bp.route('/api/articles/<int:id>',methods=['PUT'])
def modifier_articles(id):
    a = Article.query.get(id)

    if not a:
        return jsonify({'message' : 'article non trouve'}), 404
    data = request.get_json()
    if not data.get('titre') or not data.get('contenu') or not data.get('auteur'):
        return jsonify({'message': 'le titre, le contenu et l\'auteur sont obligatoires'}), 400

    a.titre = data['titre']
    a.contenu = data['contenu']
    a.auteur = data['auteur']
    db.session.commit()
    return jsonify({'message': 'article modifie avec succes','article': a.mise_dictionnaire()}), 200

#route pour supprimer un article

@articles_bp.route('/api/articles/<int:id>',methods=['DELETE'])
def supprimer_article(id):
    a = Article.query.get_or_404(id)
    if not a :
        return jsonify({'message': 'article non trouve'}), 404
    db.session.delete(a)
    db.session.commit()
    return jsonify({'message': 'article supprime avec succes'}), 200

#rechercher artciles

@articles_bp.route('/api/articles/search',methods=['GET'])
def rechercher_article():
    titre = request.args.get('titre')
    if not titre:
        return jsonify({'message': 'parametre de la requete obligatoire'}), 400

    articles = Article.query.filter(Article.titre.contains(titre)).all()
    return jsonify({'articles': [a.mise_dictionnaire() for a in articles]}), 200