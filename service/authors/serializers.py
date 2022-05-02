from rest_framework.serializers import ModelSerializer,StringRelatedField
from .models import Author,Article,Book,Biography

class SimpleAuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name','last_name']

class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookModelSerializer(ModelSerializer):
    authors = StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'

class ArticleModelSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class BiographyModelSerializer(ModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Biography
        fields = '__all__'