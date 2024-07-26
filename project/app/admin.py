from django.contrib import admin
from .models import CustomeUser,transaction
# Register your models here.






class CustomeUserAdmin(admin.ModelAdmin):
    list_display = ('id','username','first_name','email','Phonenumber','Address','DOB','Initialamount','Accountnumber')
    fieldsets = ((None, {'fields': ('username','Image', 'password', 'usertype')}),)
    search_fields = ('username', 'email')


class transactionAdmin(admin.ModelAdmin):
    list_display = ('user_id','details','amount','balance','dateandtime')
    readonly_fields = ('dateandtime',)
    fieldsets = ((None, {'fields': ('user_id','details','amount','balance','dateandtime')}),)

    

admin.site.register(CustomeUser, CustomeUserAdmin)
admin.site.register(transaction,transactionAdmin)

admin.site.site_header= 'E-BANK'