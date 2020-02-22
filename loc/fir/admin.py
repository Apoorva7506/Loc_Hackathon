from django.contrib import admin
from .models import User,missing_obj,murder,miss_person,Assault

admin.site.register(User)
admin.site.register(missing_obj)
admin.site.register(murder)
admin.site.register(miss_person)
admin.site.register(Assault)