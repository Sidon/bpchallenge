from django.contrib import admin
# from .models import Customer, NaturalPerson, LegalPerson, Phone, AddressSede, AddressEntrega
#
# __author__ = "Sidon Duarte"
# __date__ = "Created by 05/03/20"
# __copyright__ = "Copyright 2018"
# __email__ = "sidoncd@gmail.com"
#
#
# class LegalPersonInline(admin.StackedInline):
#     verbose_name = 'Pessoa Jurídica'
#     verbose_name_plural = 'Pessoa Jurídica'
#     model = LegalPerson
#
#
# class NaturalPersonInline(admin.StackedInline):
#     verbose_name = 'Pessoa Física'
#     verbose_name_plural = 'Pessoa Física'
#     model = NaturalPerson
#
#
# class AddressSedeInline(admin.StackedInline):
#     verbose_name = 'Endereço da Sede'
#     verbose_name_plural = 'Endereço da Sede'
#     model = AddressSede
#     exclude = ('additional',)
#     fk_name = 'main'
#     readonly_fields = ('kind',)
#
#
# class AddresEntregaInline(admin.StackedInline):
#     verbose_name = 'Endereço de Entrega'
#     verbose_name_plural = 'Endereço de Entrega'
#     model = AddressEntrega
#     exclude = ('main',)
#     fk_name = 'additional'
#     readonly_fields = ('kind',)
#     max_num = 1
#     extra = 3
#
# class FoneInline(admin.TabularInline):
#     model = Phone
#
#
# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#
#     list_display = ('identification', 'email' )
#     inlines = (LegalPersonInline, NaturalPersonInline, AddressSedeInline, AddresEntregaInline)
#     search_fields = ('identification',)
#
#     list_display_links = list_display
#     # list_filter = ('is_active',)
#     fieldsets = (
#         (None, {'fields': ('email', 'identification', 'password',)}),
#         ('Legado', {'fields': ('legace_code',)}),
#         ('Dados pessoais', {'fields': ('phone',)}),
#         # ('Permissões', {'fields': ('groups',)}),
#         # ('Datas importantes', {'fields': ('date_joined', 'last_login')}),
#     )
#
#     add_fieldsets = (
#         (None, {'fields': ('email', 'nome', 'password1', 'password2',)}),
#     )
#     search_fields = ('email', 'name', 'identification')
#     ordering = ('identification',)
#     # filter_horizontal = ['user_permissions']
#     # autocomplete_fields = ['costumer', 'groups']
#     list_per_page = 30
#
#     def save_model(self, request, obj, form, change):
#         # print('====>',dir(obj))
#         obj.set_password(form.clean()['password'])
#         super(CustomerAdmin, self).save_model(request, obj, form, change)
#

# class ItemVariacaoInline(admin.StackedInline):
#     verbose_name = 'Variações'
#     model = ItemVariation
#     extra = 1
#
# class EmbalagemInline(admin.StackedInline):
#     model = Packing
#
# @admin.register(Packing)
# class EmbalagemAdmin(admin.ModelAdmin):
#     list_display = ('codigo', 'descricao', 'largura', 'altura', 'profundidade', 'container', 'embalagem_contida',
#                     'qt_contida')
#
#
#
# @admin.register(ItemCategory)
# class CatetoriaAdmin(admin.ModelAdmin):
#     list_display = ('codigo', 'titulo',)
#
#
# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
#
#     list_display = ('codigo', 'titulo', 'sku', 'preco_unitario', 'preco_unitario_minimo', 'categoria', 'embalagem')
#     inlines = (ItemVariacaoInline,)
#
#     search_fields = ('titulo', 'sku',)
#     list_filter = ['categoria']
#


    # list_display_links = list_display
    # list_filter = ('is_active',)
    # fieldsets = (
    #     (None, {'fields': ('email', 'nome', 'password',)}),
    #     ('Dados pessoais', {'fields': ('telefone',)}),
    #     ('Permissões', {'fields': ('cliente', 'groups',)}),
    #     ('Datas importantes', {'fields': ('date_joined', 'last_login')}),
    # )
    #
    # add_fieldsets = (
    #     (None, {'fields': ('email', 'nome', 'cliente', 'password1', 'password2',)}),
    # )
    # search_fields = ('email', 'name', 'cliente__identricacao')
    # ordering = ('descricao',)
    # filter_horizontal = ['user_permissions']
    # autocomplete_fields = ['cliente', 'groups']
    # list_per_page = 30
#