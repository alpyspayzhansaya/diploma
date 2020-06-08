from django.contrib import admin


from . import models


admin.site.register(models.RequestDetails)
admin.site.register(models.ScoreCard)
