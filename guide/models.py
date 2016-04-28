from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Location(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField()
    updated_at      = models.DateTimeField()
    deleted_at      = models.DateTimeField()
    name            = models.CharField(max_length=255)

class Category(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField()
    updated_at      = models.DateTimeField()
    deleted_at      = models.DateTimeField()
    title           = models.CharField(max_length=255)

class Exhibition(models.Model):
    uuid                    = models.UUIDField(primary_key=True)
    created_at              = models.DateTimeField()
    updated_at              = models.DateTimeField()
    deleted_at              = models.DateTimeField()
    title                   = models.CharField(max_length=255)
    subtitle                = models.CharField(max_length=255)
    is_live                 = models.BooleanField()
    position                = models.IntegerField()
    sponsor                 = models.CharField(max_length=255)
    bg_iphone_updated_at    = models.DateTimeField()
    bg_ipad_updated_at      = models.DateTimeField()
    bg_iphone_file_size     = models.IntegerField()
    bg_ipad_file_size       = models.IntegerField()
    bg_iphone_normal        = models.URLField()
    bg_iphone_retina        = models.URLField()
    bg_ipad_normal          = models.URLField()
    bg_ipad_retina          = models.URLField()

class Tour(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField()
    updated_at      = models.DateTimeField()
    deleted_at      = models.DateTimeField()
    title           = models.CharField(max_length=255)
    subtitle        = models.CharField(max_length=255)
    body            = models.TextField()
    exhibition      = models.ForeignKey('Exhibition', on_delete=models.CASCADE, db_column='exhibition_uuid')
    artwork         = models.ManyToManyField('Artwork', through='tourArtwork')

class Artist(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField()
    updated_at      = models.DateTimeField()
    deleted_at      = models.DateTimeField()
    first_name      = models.CharField(max_length=255)
    last_name       = models.CharField(max_length=255)
    country         = models.CharField(max_length=20)
    bio             = models.TextField()
    code            = models.CharField(max_length=40)
    exhibition      = models.ForeignKey('Exhibition', on_delete=models.CASCADE, db_column='exhibition_uuid')
    artwork         = models.ManyToManyField('Artwork', through='artistArtwork')

class Link(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField()
    updated_at      = models.DateTimeField()
    deleted_at      = models.DateTimeField()
    title           = models.CharField(max_length=255)
    url             = models.URLField()
    exhibition      = models.ForeignKey('Exhibition', on_delete=models.CASCADE, db_column='exhibition_uuid')
    artist          = models.ForeignKey('Artist', on_delete=models.CASCADE, db_column='artist_uuid')

class Artwork(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField()
    updated_at      = models.DateTimeField()
    deleted_at      = models.DateTimeField()
    title           = models.CharField(max_length=255)
    code            = models.CharField(max_length=40)
    body            = models.TextField()
    share_url       = models.URLField()
    exhibition      = models.ForeignKey('Exhibition', on_delete=models.CASCADE, db_column='exhibition_uuid')
    location        = models.ForeignKey('Location', on_delete=models.CASCADE, db_column='location_uuid')
    category        = models.ForeignKey('Category', on_delete=models.CASCADE, db_column='category_uuid')
    artist          = models.ManyToManyField('Artist', through='artistArtwork')

class Media(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField()
    updated_at      = models.DateTimeField()
    deleted_at      = models.DateTimeField()
    title           = models.CharField(max_length=255)
    kind            = models.CharField(max_length=255)
    width           = models.IntegerField()
    height          = models.IntegerField()
    position        = models.IntegerField()
    alt             = models.CharField(max_length=255)
    exhibition      = models.ForeignKey('Exhibition', on_delete=models.CASCADE, db_column='exhibition_uuid')
    artwork         = models.ForeignKey('Artwork', on_delete=models.CASCADE, db_column='artwork_uuid')
    urlThumb        = models.URLField()
    urlSmall        = models.URLField()
    urlMedium       = models.URLField()
    urlLarge        = models.URLField()
    urlFull         = models.URLField()

class artistArtwork(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField()
    updated_at      = models.DateTimeField()
    deleted_at      = models.DateTimeField()
    exhibition      = models.ForeignKey('Exhibition', on_delete=models.CASCADE, db_column='exhibition_uuid')
    artist          = models.ForeignKey('Artist', on_delete=models.CASCADE, db_column='artist_uuid')
    artwork         = models.ForeignKey('Artwork', on_delete=models.CASCADE, db_column='artwork_uuid')

class tourArtwork(models.Model):
    uuid            = models.UUIDField(primary_key=True)
    created_at      = models.DateTimeField()
    updated_at      = models.DateTimeField()
    deleted_at      = models.DateTimeField()
    position        = models.IntegerField()
    exhibition      = models.ForeignKey('Exhibition', on_delete=models.CASCADE, db_column='exhibition_uuid')
    tour            = models.ForeignKey('Tour', on_delete=models.CASCADE, db_column='tour_uuid')
    artwork         = models.ForeignKey('Artwork', on_delete=models.CASCADE, db_column='artwork_uuid')
