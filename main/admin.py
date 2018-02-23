from django.contrib import admin
from .models import Location, Machine, Tourney, HighScore, OldiePic, Oldie

class MachineInLine(admin.StackedInline):
    model = Machine
    extra = 0

class OldiePicInLine(admin.StackedInline):
    model = OldiePic
    extra = 0

class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['url']}),
    ]
    inlines = [MachineInLine]

class TourneyAdmin(admin.ModelAdmin):
    list_display = ['name']
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['machine']}),
        (None, {'fields': ['location']}),
        (None, {'fields': ['description']}),
    ]

class HighScoreAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['first']}),
        (None, {'fields': ['second']}),
        (None, {'fields': ['third']}),
        (None, {'fields': ['machine']}),
    ]

class OldieAdmin(admin.ModelAdmin):
    model = Oldie
    fieldsets = [
        (None, {'fields': ['title']}),
    ]
    inlines = [OldiePicInLine]



admin.site.register(Location, LocationAdmin)
admin.site.register(Tourney, TourneyAdmin)
admin.site.register(HighScore, HighScoreAdmin)
admin.site.register(Oldie, OldieAdmin)

# class PhotoAdmin(admin.ModelAdmin):
#     list_display = ["title", "timestamp"]
#
#     class Meta:
#         model = Photo
#
# admin.site.register(Photo, PhotoAdmin)

# Register your models here.
