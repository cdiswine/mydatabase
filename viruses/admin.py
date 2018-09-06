from django.contrib import admin

from .models import Virus

@admin.register(Virus)
class VirusAdmin(admin.ModelAdmin):
    list_display = ['order', 'family', 'subfamily', 'genus', 'species', 'genome', 'host']


from .models import Sequence

@admin.register(Sequence)
class SequenceAdmin(admin.ModelAdmin):
    list_display = ['nucleotides', 'submission_date']

