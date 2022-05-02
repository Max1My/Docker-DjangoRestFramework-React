from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework import permissions
# from rest_framework.schemas import get_schema_view
# from authors.views import AuthorModelViewSet,BiographyModelViewSet,BookModelViewSet,ArticleModelViewSet
from users.views import UserModelViewSet,ProjectModelViewSet,TodoListModelViewSet
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# schema_view = get_schema_view(
#     openapi.Info(
#         title='service',
#         default_version='1',
#         description='Документация',
#         contact=openapi.Contact(email='maximy@gmail.com'),
#         license=openapi.License(name='MIT License')
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

router = DefaultRouter()
# router.register('authors', AuthorModelViewSet)
# router.register('biographies',BiographyModelViewSet)
# router.register('books', BookModelViewSet)
# router.register('articles', ArticleModelViewSet)
router.register('users', UserModelViewSet)
# router.register('users_project',UserModelViewSet)
router.register('projects',ProjectModelViewSet)
router.register('todolists',TodoListModelViewSet)

# schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/', include(router.urls)),
    # path('api/auth/', include('djoser.urls')),
    # path('api/auth/', include('djoser.urls.authtoken')),
    # path('api/auth/', include('djoser.urls.jwt')),
    # path('schema/',schema_view),
    # path('api/users/',UserListAPIView.as_view()),
    # path('api/users/1', include('users.urls', namespace='1')),
    # path('api/users/2', include('users.urls', namespace='2')),
    # re_path(r'^api/(?P<version>\d)/users/$',UserListAPIView.as_view()),
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),name='schema-redoc'),
    # path('graphql/',GraphQLView.as_view(graphiql=True))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)