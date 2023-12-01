from django.urls import path,re_path
from .views import WorkListCreateView,UserRegisterView,ArtistWorkListView,DelArtist
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Artist API",
      default_version='v1',
      description="Artist API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[]
)

urlpatterns = [
    path('api/works/',WorkListCreateView.as_view(),name="work-list-create"),
    path('api/works',ArtistWorkListView.as_view(),name="artist-work-list"),
    path('api/register/',UserRegisterView.as_view(),name="user-register"),
    path('api/api-token-auth/',obtain_auth_token,name='api_token'),
    path('api/remove-artist/<str:username>',DelArtist.as_view(),name="Delete-Artist"),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]