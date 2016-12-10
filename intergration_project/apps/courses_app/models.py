from __future__ import unicode_literals

from django.db import models

from ..login_reg_app.models import User

class CourseManager(models.Manager):
    def add_user_to_course(self, form_data):
        # First find the course
        course = self.get(id=form_data['course'])
        # Then grab the user
        user = User.objects.get(id=form_data['user'])
        # Add the user to the course
        course.users.add(user)
        #And finally save the course
        course.save()

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()
    # Adds many-to-many relationship w/ users
    users = models.ManyToManyField('login_reg_app.User', related_name='courses')