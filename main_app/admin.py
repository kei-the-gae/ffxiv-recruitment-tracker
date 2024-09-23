from django.contrib import admin
from .models import Player, Job
from image_cropping import ImageCroppingMixin

class PlayerAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Player, PlayerAdmin)
admin.site.register(Job)
