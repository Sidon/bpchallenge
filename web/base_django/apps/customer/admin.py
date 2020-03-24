from django.contrib import admin
from .models import Customer

__author__ = "Sidon Duarte"
__date__ = "Created by 23/03/20"
__copyright__ = "Copyright 2019"
__email__ = "sidoncd@gmail.com"



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('full_name', 'phones', 'email')
    search_fields = ('full_name', 'email',)

    list_display_links = list_display
    fieldsets = (
        (None, {'fields': ('email', 'full_name', 'password',)}),
        # ('Permissões', {'fields': ('groups',)}),
        # ('Datas importantes', {'fields': ('date_joined', 'last_login')}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'nome', 'password1', 'password2',)}),
    )
    search_fields = ('email', 'full_name')
    ordering = ('full_name',)
    list_per_page = 30

    def save_model(self, request, obj, form, change):
        # print('====>',dir(obj))
        obj.set_password(form.clean()['password'])
        super(CustomerAdmin, self).save_model(request, obj, form, change)
