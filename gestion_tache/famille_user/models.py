from django.db import models

class FUser(models.Model):
    id_f_user = models.AutoField(primary_key=True)
    libelle_famille = models.CharField(max_length=100)
    coefficient = models.IntegerField()
    remarques = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'f_user'