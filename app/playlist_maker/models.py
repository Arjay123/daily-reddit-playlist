# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Credential(models.Model):
    """
    A model that contains credentials for an api service

    Fields:
        access_token     - if the service requires authorization, this is used
                           to authorize the server
        refresh_token    - Used to retrieve a new access_token if it has
                           expired
        client_id        - client id for the api service
        client_secret    - client secret for the api service
        account_username - username of the account registered for the api
                           service
        account_password - password of the account registered for the api
                           service
        service          - name of the api service
    """
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)
    account_username = models.CharField(max_length=255)
    account_password = models.CharField(max_length=255)
    account_id = models.CharField(max_length=255)
    service = models.CharField(max_length=30)
