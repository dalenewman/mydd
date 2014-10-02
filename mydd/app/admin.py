from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from models import *

class StepInline(admin.TabularInline):
    model = Step
    extra = 1

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [StepInline, IngredientInline]
    list_display = ('name', 'description', 'servings')
    list_filter = ['difficulty', 'tags' ]
    search_fields = ['name','description']
    filter_horizontal = ('products','tags')
    list_per_page = 25

class ClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ['tags']
    search_fields = ['title','description']
    filter_horizontal = ('products','recipes','tags')
    list_per_page = 25

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name','quantity','uom', 'recipe',)
    list_filter = ['quantity','uom','recipe']
    search_fields = ['name']

admin.site.register(Person)
admin.site.register(Location)
admin.site.register(MainIngredient)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Product)
admin.site.register(TypeOfCuisine)
admin.site.register(Tag)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Class, ClassAdmin)
