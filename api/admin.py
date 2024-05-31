from django.contrib import admin
from api.models import User,FriendRequest


class adminUser(admin.ModelAdmin):
    pass
    # list_display= '__all__'

admin.site.register(User)
# Register your models here.
