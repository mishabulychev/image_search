# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
import os

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')


class Document(models.Model):
    docfile = models.ImageField(validators=[validate_file_extension])
    name = models.CharField(verbose_name=u"Имя",max_length=255,blank=True,)
    features = models.BinaryField(blank=True,)
    weight = 0
