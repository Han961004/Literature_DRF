from django.contrib import admin

from .models.user import User
from .models.profile import Profile
from .models.subscribe import Subscription


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Subscription)