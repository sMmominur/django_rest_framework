from django.db import models

# Create your models here.

class EiinTbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    eiin = models.CharField(max_length=15)
    code = models.CharField(max_length=15, null=True, blank=True)
    name = models.CharField(max_length=255)
    district = models.CharField(max_length=100, null=True, blank=True)
    upazila = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        db_table = 'eiin_tbl'
        indexes = [
            models.Index(fields=['eiin']),
            models.Index(fields=['code']),
            models.Index(fields=['name']),
        ]
        ordering = ['id']

    def __str__(self):
        return self.name or 'Unnamed Entry'