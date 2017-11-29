from rest_framework import serializers
from sample.models import Person
from django.contrib.auth.models import User


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Person
        fields = ('id', 'name', 'age', 'fav_game', 'owner')



class UserSerializer(serializers.HyperlinkedModelSerializer):
    persons = serializers.HyperlinkedRelatedField(many=True, view_name="person-detail", read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'persons')