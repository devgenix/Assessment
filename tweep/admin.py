# Django Imports
from django.contrib import admin

# Own Imports
from tweep.models import Tweet


admin.site.register([Tweet])