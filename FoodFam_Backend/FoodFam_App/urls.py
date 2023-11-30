from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from django.urls import path

from FoodFam_App import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'recipes', views.RecipeViewSet,basename="recipe")
router.register(r'users', views.UserViewSet,basename="user")
router.register(r'groups', views.GroupViewSet,basename="group")

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    #path('users/', views.UserList.as_view()),
    #path('users/<int:pk>/', views.UserDetail.as_view()),
    #path('recipes/', views.RecipeList.as_view()),
    #path('recipes/<int:pk>/', views.RecipeDetail.as_view()),
    #path(r'^', include(router.urls))
]