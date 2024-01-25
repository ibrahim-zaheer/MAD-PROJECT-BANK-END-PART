from django.contrib import admin
from .models import Notes,MyModel,ProperProfileCreation,UserProfileBeforeLogin,InvestorProject,Project
# Register your models here.
admin.site.register(Notes)
admin.site.register(MyModel)
admin.site.register(ProperProfileCreation)
admin.site.register(UserProfileBeforeLogin)
admin.site.register(Project)
admin.site.register(InvestorProject)