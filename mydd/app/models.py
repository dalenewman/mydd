"""
Definition of models.
"""
from django.utils.translation import ugettext_lazy as _
from django.db import models

class Tag(models.Model):
    name = models.CharField(_("name"), max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")

class TypeOfCuisine(models.Model):
    name = models.CharField(_("name"), max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("type of cuisine")
        verbose_name_plural = _("types of cuisine")

class Product(models.Model):
    name = models.CharField(_("name"), max_length=255)
    image = models.URLField(_("image"), blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("product")

class MainIngredient(models.Model):
    name = models.CharField(_("name"), max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("main ingredient")
        verbose_name_plural = _("main ingredients")

class Person(models.Model):
    first = models.CharField(_("first name"), max_length=128)
    last = models.CharField(_("last name"), max_length=128)
    avatar = models.URLField(_("avatar"), blank=True)
    bio = models.TextField(_("bio"),max_length=1024, blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.first + " " + self.last

    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("person")

class Location(models.Model):
    MI = 'MI'
    IN = 'IN'
    IL = 'IL'
    STATES = (
        (MI, 'MI'),
        (IN, 'IN'),
        (IL, 'IL'),
    )
    name = models.CharField(_("name"), max_length=255)
    contact = models.ForeignKey(Person, verbose_name="contact", blank=True, null=True)
    description = models.TextField(_("description"), max_length=4096, blank=True, default="")
    image = models.URLField(_("image"), blank=True, default="")
    street = models.CharField(_("street"), max_length=512, blank=True, default="")
    city = models.CharField(_("city"), max_length=255, blank=True, default="")
    state = models.CharField(_("state"),max_length=2, choices=STATES, default=MI)
    zip = models.CharField(_("zip"), max_length=10, blank=True, default="")
    phone = models.CharField(_("phone"), max_length=20, blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("location")

class Recipe(models.Model):
    DIFFICULTY = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    author = models.ForeignKey(Person, verbose_name=_("author"))
    name = models.CharField(_("name"), max_length=512)
    description = models.TextField(_("description"), max_length=4096, blank=True, default="")
    servings = models.PositiveIntegerField(_("servings"), default=1)
    active_time = models.PositiveIntegerField(_("active time"), default=0)
    passive_time = models.PositiveIntegerField(_("passive time"), default=0)
    image = models.URLField(_("image"), blank=True, default="")
    type_of_cuisine = models.ForeignKey(TypeOfCuisine, verbose_name=_("type of cuisine"), blank=True, null=True)
    main_ingredient = models.ForeignKey(MainIngredient, verbose_name=_("main ingredient"), blank=True, null=True)
    difficulty = models.PositiveSmallIntegerField(_("difficulty"), choices=DIFFICULTY, default=3)
    products = models.ManyToManyField(Product,verbose_name=_("products"), blank=True)
    tags = models.ManyToManyField(Tag,verbose_name=_("tags"), blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("recipe")
        verbose_name_plural = _("recipes")

class Class(models.Model):
    title = models.CharField(_("name"), max_length=512)
    image = models.CharField(_("image"), max_length=255, blank=True, default="")
    description = models.TextField(_("description"), max_length=4096, blank=True, default="")
    cost = models.DecimalField(_("cost"), decimal_places=2,max_digits=6, default=0.0)
    instructor = models.ForeignKey(Person, verbose_name=_("instructor"))
    tags = models.ManyToManyField(Tag,verbose_name=_("tags"), blank=True)
    products = models.ManyToManyField(Product, verbose_name=_("products"), blank=True)
    recipes = models.ManyToManyField(Recipe, verbose_name=_("recipes"), blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _("class")
        verbose_name_plural = _("classes")

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, verbose_name=_("recipe"))
    name = models.CharField(_("name"), max_length=255)
    quantity = models.CharField(_("quantity"), max_length=64, blank=True)
    uom = models.CharField(_("unit of measure"), max_length=128, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("ingredient")
        verbose_name_plural = _("ingredients")

class Step(models.Model):
    recipe = models.ForeignKey(Recipe, verbose_name=_("recipe"))
    sequence = models.SmallIntegerField(_('sequence'))
    description = models.TextField(_("description"), max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.description[:30] + "..." if len(self.description) > 30 else self.description

    class Meta:
        verbose_name = _("step")
        verbose_name_plural = _("steps")