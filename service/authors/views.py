from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer, AdminRenderer

from .models import Author,Book,Article,Biography
from .serializers import AuthorModelSerializer,BookModelSerializer,BiographyModelSerializer,ArticleModelSerializer

class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

class BookModelViewSet(ModelViewSet):
    # author = MAuthor('Грин', 1880)
    # serializer = AuthorSerializer(author)
    # print(serializer.data)

    # render = JSONRenderer()
    # json_data = render.render(serializer.data)
    # print(json_data)

    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer

class BiographyModelViewSet(ModelViewSet):
    renderer_classes = [AdminRenderer]
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer