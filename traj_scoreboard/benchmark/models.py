# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Challenges(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, blank=True, null=True)
    docker_container = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000, blank=True, null=True)
    data_path = models.CharField(max_length=1000, blank=True, null=True)
    data_size = models.CharField(max_length=1000, blank=True, null=True)
    color = models.CharField(max_length=1000, blank=True, null=True)
    about = models.CharField(max_length=1000, blank=True, null=True)
    example_file = models.CharField(max_length=1000, blank=True, null=True)
    submission_header = models.TextField(blank=True, null=True)  # This field type is a guess.
    submission_separator = models.CharField(max_length=1000, blank=True, null=True)
    scores = models.TextField(blank=True, null=True)  # This field type is a guess.
    subscores = models.TextField(blank=True, null=True)  # This field type is a guess.
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    is_open = models.BooleanField()
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'challenges'


class Datasets(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, blank=True, null=True)
    tree = models.TextField(blank=True, null=True)  # This field type is a guess.
    challenge = models.ForeignKey(Challenges, models.DO_NOTHING)
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'datasets'


class Results(models.Model):
    submission = models.ForeignKey('Submissions', models.DO_NOTHING)
    results_path = models.CharField(max_length=1000)
    score_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_current = models.BooleanField()
    submission_date = models.DateTimeField()
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'results'


class Submissions(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    challenge = models.ForeignKey(Challenges, models.DO_NOTHING)
    name = models.CharField(max_length=1000)
    repository = models.CharField(max_length=1000)
    is_private = models.BooleanField()
    institution = models.CharField(max_length=1000, blank=True, null=True)
    publication = models.CharField(max_length=1000, blank=True, null=True)
    is_accepted = models.BooleanField()
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'submissions'


class Users(models.Model):
    github_username = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000, blank=True, null=True)
    email = models.CharField(max_length=1000, blank=True, null=True)
    is_admin = models.BooleanField()
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'
