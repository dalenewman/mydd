from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.db import models
from django.forms import Textarea
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
    filter_horizontal = ('products','tags','images')
    list_per_page = 25

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ( '_class','location','date','full')
    list_filter = ['_class','location','date','full']

class ClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ['tags']
    search_fields = ['title','description']
    filter_horizontal = ('products','recipes','tags','images')
    list_per_page = 25

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name','quantity','uom', 'recipe',)
    list_filter = ['quantity','uom','recipe']
    search_fields = ['name']
    filter_horizontal = ('images',)

class StepAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2 })},
    }

admin.site.register(Image)
admin.site.register(Person)
admin.site.register(Location)
admin.site.register(MainIngredient)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Product)
admin.site.register(TypeOfCuisine)
admin.site.register(Tag)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Step, StepAdmin)
