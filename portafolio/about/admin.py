from django.contrib import admin

# Register your models here.
from .models import Training,Skill

class TrainingAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class SkillAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

# Register your models here.
admin.site.register(Training,TrainingAdmin)
admin.site.register(Skill,SkillAdmin)