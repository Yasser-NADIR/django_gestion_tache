# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CompanySettings(models.Model):
    setting_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    logo_white = models.CharField(max_length=255)
    logo_icon = models.CharField(max_length=255)
    mainpage_card_text = models.CharField(max_length=500)
    footer_text = models.CharField(max_length=255)
    facebook_link = models.CharField(max_length=255)
    youtube_link = models.CharField(max_length=255)
    instagram_link = models.CharField(max_length=255)
    print_footer = models.TextField()
    company_settings_date_updated = models.DateField()

    class Meta:
        managed = False
        db_table = 'company_settings'


class FUser(models.Model):
    id_f_user = models.AutoField(primary_key=True)
    libelle_famille = models.CharField(max_length=100)
    coefficient = models.IntegerField()
    remarques = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'f_user'


class HDetTache(models.Model):
    id_h_det_tache = models.AutoField(primary_key=True)
    id_h_l_ent_tache = models.IntegerField()
    id_tache = models.IntegerField()
    h_debut = models.TimeField()
    h_fin = models.TimeField()
    temps_diff = models.IntegerField()
    coefficient = models.IntegerField()
    prix_calc = models.IntegerField()
    remarques = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'h_det_tache'


class HEntTache(models.Model):
    id_h_ent_tache = models.AutoField(primary_key=True)
    libelle_journee = models.CharField(max_length=100)
    id_users = models.IntegerField()
    date_operation = models.DateField()
    remarques = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'h_ent_tache'


class Region(models.Model):
    nom_region = models.TextField()

    class Meta:
        managed = False
        db_table = 'region'


class ReqFUser(models.Model):
    nbr_libelle_famille = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_f_user'


class ReqGTache(models.Model):
    libelle_tache = models.CharField(max_length=100, blank=True, null=True)
    somme_tache = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_g_tache'


class ReqGTacheUser(models.Model):
    nom = models.CharField(max_length=100, blank=True, null=True)
    libelle_tache = models.CharField(max_length=100, blank=True, null=True)
    somme_tache = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_g_tache_user'


class ReqHDetTache(models.Model):
    id_h_det_tache = models.IntegerField(blank=True, null=True)
    id_h_l_ent_tache = models.IntegerField(blank=True, null=True)
    id_tache = models.IntegerField(blank=True, null=True)
    h_debut = models.TimeField(blank=True, null=True)
    h_fin = models.TimeField(blank=True, null=True)
    temps_diff = models.IntegerField(blank=True, null=True)
    coefficient = models.IntegerField(blank=True, null=True)
    prix_calc = models.IntegerField(blank=True, null=True)
    remarques = models.CharField(max_length=100, blank=True, null=True)
    libelle_tache = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_h_det_tache'


class ReqHEntTache(models.Model):
    id_h_ent_tache = models.IntegerField(blank=True, null=True)
    libelle_journee = models.CharField(max_length=100, blank=True, null=True)
    id_users = models.IntegerField(blank=True, null=True)
    date_operation = models.DateField(blank=True, null=True)
    remarques = models.CharField(max_length=100, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_h_ent_tache'


class ReqHTache(models.Model):
    id_h_ent_tache = models.IntegerField(blank=True, null=True)
    libelle_journee = models.CharField(max_length=100, blank=True, null=True)
    id_users = models.IntegerField(blank=True, null=True)
    date_operation = models.DateField(blank=True, null=True)
    remarques = models.CharField(max_length=100, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    id_h_det_tache = models.IntegerField(blank=True, null=True)
    id_h_l_ent_tache = models.IntegerField(blank=True, null=True)
    id_tache = models.IntegerField(blank=True, null=True)
    h_debut = models.TimeField(blank=True, null=True)
    h_fin = models.TimeField(blank=True, null=True)
    temps_diff = models.IntegerField(blank=True, null=True)
    coefficient = models.IntegerField(blank=True, null=True)
    prix_calc = models.IntegerField(blank=True, null=True)
    remarques1 = models.CharField(max_length=100, blank=True, null=True)
    libelle_tache = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_h_tache'


class ReqNbrUsersFamille(models.Model):
    libelle_famille = models.CharField(max_length=100, blank=True, null=True)
    nbr_utilisateur = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_nbr_users_famille'


class ReqTaches(models.Model):
    nombre_de_tache = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_taches'


class ReqUsers(models.Model):
    nbr_users = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_users'


class ReqUsersFamille(models.Model):
    id_users = models.IntegerField(blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    libelle_famille = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_users_famille'


class Tache(models.Model):
    id_tache = models.AutoField(primary_key=True)
    libelle_tache = models.CharField(max_length=100)
    coefficient = models.IntegerField()
    remarques = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tache'


class User(models.Model):
    username = models.TextField()
    email = models.TextField()
    password = models.TextField()

    class Meta:
        managed = False
        db_table = 'user'


class Users(models.Model):
    id_users = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=100)
    id_f_user = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'
