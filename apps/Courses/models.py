# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models
from django.contrib.messages import error

#Controller/Manager for validations
class CourseManager(models.Manager):
    def validate(self, post_data):
        errors = {}

        # check all fields for emptyness
        for field, value in post_data.iteritems():
            if len(value) < 1:
                errors[field] = "{} field is reqired".format(field.replace('_', ' '))

            # check name fields for min length
            if field == "name":
                if not field in errors and len(value) < 5:
                    errors[field] = "{} field must bet at least 5 characters".format(field.replace('_', ' '))
            
            # check name fields for min length
            if field == "desc":
                if not field in errors and len(value) < 15:
                    errors[field] = "{} field must bet at least 15 characters".format(field.replace('_', ' '))
            
        return errors
# Class for your models
class Course (models.Model):
    name = models.CharField (max_length=50)
    desc = models.CharField (max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

