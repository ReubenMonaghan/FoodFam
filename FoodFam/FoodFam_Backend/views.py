from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, generics, viewsets
from .serializers import *

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    https://www.django-rest-framework.org/api-guide/viewsets/
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    https://www.django-rest-framework.org/api-guide/viewsets/

    you can write stuff in here as a note in views.py
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# this is an example of how to add extra functionality to a DRF view from the DRF tutorial
#    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
#    def highlight(self, request, *args, **kwargs):
#        snippet = self.get_object()
#        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    https://www.django-rest-framework.org/api-guide/viewsets/

    you can write stuff in here as a note in views.py
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]