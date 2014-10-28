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

class Image(models.Model):
    title = models.CharField(_("title"), max_length=512)
    image = models.URLField(_("image"), blank=True, default="")
    credits = models.CharField(_("credits"), max_length=512, blank=True, default="")
    caption = models.CharField(_("caption"), max_length=1024, blank=True, default="")
    description = models.TextField(_("description"), max_length=4096, blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _("image")
        verbose_name_plural = _("images")

class Product(models.Model):
    name = models.CharField(_("name"), max_length=255)
    images = models.ManyToManyField(Image, verbose_name=_("images"), blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("product")

models.DateTimeField(auto_now_add=True).contribute_to_class(Product.images.through, 'created')
models.DateTimeField(auto_now=True).contribute_to_class(Product.images.through, 'modified')

class Person(models.Model):
    first = models.CharField(_("first name"), max_length=128)
    last = models.CharField(_("last name"), max_length=128)
    avatar = models.URLField(_("avatar"), blank=True)
    bio = models.TextField(_("bio"),max_length=1024, blank=True, default="")
    images = models.ManyToManyField(Image, verbose_name=_("images"), blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.first + " " + self.last

    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("person")

models.DateTimeField(auto_now_add=True).contribute_to_class(Person.images.through, 'created')
models.DateTimeField(auto_now=True).contribute_to_class(Person.images.through, 'modified')

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
    description = models.TextField(_("description"), max_length=4096, blank=True, default="")
    website = models.URLField(_("website"), blank=True, default="")
    street = models.CharField(_("street"), max_length=512, blank=True, default="")
    city = models.CharField(_("city"), max_length=255, blank=True, default="")
    state = models.CharField(_("state"),max_length=2, choices=STATES, default=MI)
    zip = models.CharField(_("zip"), max_length=10, blank=True, default="")
    phone = models.CharField(_("phone"), max_length=20, blank=True, default="")
    images = models.ManyToManyField(Image, verbose_name=_("images"), blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("location")

models.DateTimeField(auto_now_add=True).contribute_to_class(Location.images.through, 'created')
models.DateTimeField(auto_now=True).contribute_to_class(Location.images.through, 'modified')

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
    inspiration = models.CharField(_("inspiration"), max_length=512, blank=True, default="")
    servings = models.PositiveIntegerField(_("servings"), default=0)
    prep_time = models.PositiveIntegerField(_("prep time"), default=0, help_text=_("preparation time in minutes."))
    cook_time = models.PositiveIntegerField(_("cook time"), default=0, help_text=_("cook time in minutes."))
    difficulty = models.PositiveSmallIntegerField(_("difficulty"), choices=DIFFICULTY, default=3)
    products = models.ManyToManyField(Product,verbose_name=_("products"), blank=True)
    tags = models.ManyToManyField(Tag,verbose_name=_("tags"), blank=True)
    images = models.ManyToManyField(Image, verbose_name=_("images"), blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("recipe")
        verbose_name_plural = _("recipes")

models.DateTimeField(auto_now_add=True).contribute_to_class(Recipe.images.through, 'created')
models.DateTimeField(auto_now=True).contribute_to_class(Recipe.images.through, 'modified')
models.DateTimeField(auto_now_add=True).contribute_to_class(Recipe.products.through, 'created')
models.DateTimeField(auto_now=True).contribute_to_class(Recipe.products.through, 'modified')
models.DateTimeField(auto_now_add=True).contribute_to_class(Recipe.tags.through, 'created')
models.DateTimeField(auto_now=True).contribute_to_class(Recipe.tags.through, 'modified')

class Class(models.Model):
    title = models.CharField(_("name"), max_length=512)
    description = models.TextField(_("description"), max_length=4096, blank=True, default="")
    cost = models.DecimalField(_("cost"), decimal_places=2,max_digits=6, default=0.0)
    instructor = models.ForeignKey(Person, verbose_name=_("instructor"))
    tags = models.ManyToManyField(Tag,verbose_name=_("tags"), blank=True)
    products = models.ManyToManyField(Product, verbose_name=_("products"), blank=True)
    recipes = models.ManyToManyField(Recipe, verbose_name=_("recipes"), blank=True)
    images = models.ManyToManyField(Image, verbose_name=_("images"), blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _("class")
        verbose_name_plural = _("classes")

models.DateTimeField(auto_now_add=True).contribute_to_class(Class.images.through, 'created')
models.DateTimeField(auto_now=True).contribute_to_class(Class.images.through, 'modified')
models.DateTimeField(auto_now_add=True).contribute_to_class(Class.tags.through, 'created')
models.DateTimeField(auto_now=True).contribute_to_class(Class.tags.through, 'modified')
models.DateTimeField(auto_now_add=True).contribute_to_class(Class.products.through, 'created')
models.DateTimeField(auto_now=True).contribute_to_class(Class.products.through, 'modified')
models.DateTimeField(auto_now_add=True).contribute_to_class(Class.recipes.through, 'created')
models.DateTimeField(auto_now=True).contribute_to_class(Class.recipes.through, 'modified')

class Schedule(models.Model):
    _class = models.ForeignKey(Class, verbose_name=_("class"), db_column="class_id")
    location = models.ForeignKey(Location, verbose_name=_("location"))
    date = models.DateTimeField(_("date"))
    full = models.BooleanField(_("full"),default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self._class.title + " at " + self.location.name

    class Meta:
        verbose_name = _("schedule")
        verbose_name_plural = _("schedule")

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, verbose_name=_("recipe"))
    quantity = models.CharField(_("quantity"), max_length=64, blank=True)
    uom = models.CharField(_("unit of measure"), max_length=128, blank=True)
    name = models.CharField(_("name"), max_length=255)
    images = models.ManyToManyField(Image, verbose_name=_("images"), blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("ingredient")
        verbose_name_plural = _("ingredients")

models.DateTimeField(auto_now_add=True).contribute_to_class(Ingredient.images.through, 'created')
models.DateTimeField(auto_now=True).contribute_to_class(Ingredient.images.through, 'modified')

class Step(models.Model):
    recipe = models.ForeignKey(Recipe, verbose_name=_("recipe"))
    description = models.TextField(_("description"), max_length=1024 )
    sequence = models.SmallIntegerField(_('sequence'))
    images = models.ManyToManyField(Image, verbose_name=_("images"), blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.description[:30] + "..." if len(self.description) > 30 else self.description

    class Meta:
        verbose_name = _("step")
        verbose_name_plural = _("steps")

models.DateTimeField(auto_now_add=True).contribute_to_class(Step.images.through, 'created')
models.DateTimeField(auto_now=True).contribute_to_class(Step.images.through, 'modified')
