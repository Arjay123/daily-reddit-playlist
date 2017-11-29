from django.contrib.auth.models import User

from sample.models import Person
from sample.permissions import IsOwnerOrReadOnly
from sample.serializers import PersonSerializer
from sample.serializers import UserSerializer

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.shortcuts import render


def index(request):
    return render(request, 'sample/index.html', {})

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "users": reverse('user-list', request=request, format=format),
        "persons": reverse('person-list', request=request, format=format)
    })


