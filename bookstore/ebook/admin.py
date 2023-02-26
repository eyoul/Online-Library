from django.contrib import admin
from .models import Chat, Tbook, Rbook, Deleterequest, Feedback


# Register your models here.
admin.site.register(Chat),
admin.site.register(Tbook),
admin.site.register(Rbook)
admin.site.register(Deleterequest)
admin.site.register(Feedback)