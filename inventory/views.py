from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article

def home_view(request, *args, **kwargs):
    article_obj = Article.objects.get(id=1)
    articles_queryset = Article.objects.all()
    context = {
        "id": article_obj.id,
        "title": article_obj.title,
        "content": article_obj.content,
        "object_list": articles_queryset
    }

    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)