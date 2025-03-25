# admin.py
from django.contrib import admin
from .models import Agent, Property, GeneralData,UserData

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'estate_name', 'phone_number', 'rating', 'verifications')
    search_fields = ('name', 'estate_name')

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('address', 'district_name', 'tehsil_name', 'acre', 'available')
    search_fields = ('address', 'district_name')
    list_filter = ('available', 'land_category')

@admin.register(GeneralData)
class GeneralDataAdmin(admin.ModelAdmin):
    list_display = ('id',)
    filter_horizontal = ('top_rate', 'featured', 'recommendation')

@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name', 'phone')  # Allow searching by name & phone