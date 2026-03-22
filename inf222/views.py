from django.shortcuts import render, redirect, get_object_or_404
from blog.models  import Article
from django.contrib import messages 

def home(request):
    # Gestion du formulaire POST pour ajouter un article
    if request.method == 'POST':
        title = request.POST.get('title')
        contenu = request.POST.get('contenu')
        autor = request.POST.get('autor')
        category = request.POST.get('category', '')
        tags = request.POST.get('tags', '')

        # Crée un article en base
        Article.objects.create(
            title=title,
            contenu=contenu,
            autor=autor,
            category=category,
            tags=tags
        )
        messages.success(request, f"L'article '{title}' a été ajouté !")  # <-- message de succès
        return redirect('home')  # Recharge la page pour afficher la liste

    # GET → récupère tous les articles depuis la base
    articles = Article.objects.all()
    return render(request, 'page/home.html', {'articles': articles})


def delete_article(request, id):
    # Supprime l'article s'il existe
    Article.objects.filter(pk=id).delete()
    return redirect('home')