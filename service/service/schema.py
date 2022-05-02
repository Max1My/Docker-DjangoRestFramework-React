import graphene
from graphene_django import DjangoObjectType
from users.models import User, Project,ToDo_list


class UserType(DjangoObjectType):

    class Meta:
        model = User
        fields = '__all__'

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'

class ToDoListType(DjangoObjectType):
    class Meta:
        model = ToDo_list
        fields = '__all__'

class UserMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls,root,info,username,id):
        user = User.objects.get(pk=id)
        user.username = username
        user.save()
        return UserMutation(user=user)

class Mutation(graphene.ObjectType):
    update_author = UserMutation.Field()


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)
    all_todolists = graphene.List(ToDoListType)
    user_by_id = graphene.Field(UserType,id=graphene.Int(required=True))
    project_by_name = graphene.Field(ProjectType,name=graphene.String(required=True))
    todolist_by_project_name_id = graphene.Field(ProjectType,project_name=graphene.Int(required=True))

    def resolve_user_by_id(self,info,id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    def resolve_project_by_name(self,info,name):
        try:
            return Project.objects.get(name=name)
        except Project.DoesNotExist:
            return None

    def resolve_todolist_by_project_name_id(self,info,project_name_id):
        try:
            return ToDo_list.objects.get(project_name=project_name_id)
        except ToDo_list.DoesNotExist:
            return None

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_todolists(self,info):
        return ToDo_list.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutation)