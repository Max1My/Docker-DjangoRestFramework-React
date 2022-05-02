from rest_framework.serializers import ModelSerializer,StringRelatedField
from .models import User_test,Project,ToDo_list

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User_test
        fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User_test
#         fields = ('username','email')

class UserAdminSerializer(ModelSerializer):
    class Meta:
        model = User_test
        fields = '__all__'

class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ToDolistModelSerializer(ModelSerializer):

    class Meta:
        model = ToDo_list
        fields = ['project_name','text','user']
