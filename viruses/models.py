from django.db import models

class Virus(models.Model): 
    order = models.CharField(max_length=500, blank=True, null=True)
    family = models.CharField(max_length=500, blank=True, null=True)
    subfamily = models.CharField(max_length=500, blank=True, null=True)
    genus = models.CharField(max_length=500, blank=True, null=True)
    species = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.species

    genome = models.CharField(max_length=500, blank=True, null=True)
    host = models.CharField(max_length=500, blank=True, null=True)
    #sequence_name = models.CharField(max_length=500, blank=True, null=True)
    #submission_date = models.DateTimeField()
    

    #sequence_name = models.TextField()
    #submission_date = models.DateTimeField()
   

class Sequence(models.Model):
    nucleotides = models.TextField()

    def __str__(self):
        return self.nucleotides

    submission_date = models.DateTimeField()
    species = models.ForeignKey(
        Virus,
        on_delete=models.CASCADE,
    )


   

    