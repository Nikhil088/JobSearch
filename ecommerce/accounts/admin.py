from django.contrib import admin

from .models import GuestEmail
from .models import Profile

admin.site.register(Profile)

admin.site.register(GuestEmail)