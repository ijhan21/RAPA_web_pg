from django.contrib import admin
from hans.models import VoteChoice, VoteQuestion
# Register your models here.
admin.site.register(VoteQuestion)
admin.site.register(VoteChoice)