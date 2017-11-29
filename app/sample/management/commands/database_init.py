from django.core.management.base import BaseCommand
from sample.models import Person
from django.contrib.auth.models import User


class Command(BaseCommand):
    def _create_persons(self):
        user = User.objects.get(pk=1)
        user.save()

        person = Person(name="Steven",
                        age=26,
                        fav_game="Super Mario 64",
                        owner=user)
        person.save()

        person = Person(name="Lisa",
                        age=26,
                        fav_game="Final Fantasy 9",
                        owner=user)
        person.save()

        person = Person(name="Bob",
                        age=36,
                        fav_game="Super Mario World",
                        owner=user)
        person.save()

        person = Person(name="Tim",
                        age=14,
                        fav_game="Minecraft",
                        owner=user)
        person.save()

        person = Person(name="Stephanie",
                        age=21,
                        fav_game="Street Fighter 5",
                        owner=user)
        person.save()


    def handle(self, *args, **kwargs):
        self._create_persons()