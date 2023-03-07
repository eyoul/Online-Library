from django.contrib import admin
from .models import *


# Registration of Text Book models 
admin.site.register(Tbook),

# Registration of Reference Book models 
admin.site.register(Rbook)

# Registration of Quiz models 
admin.site.register(Quiz)