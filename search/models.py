from django.db import models
from datetime import datetime

class Company(models.Model):
  name = models.CharField(max_length=140)
  email = models.CharField(max_length=140)
  password = models.CharField(max_length=20)
  industry = models.CharField(max_length=20)
  picture = models.CharField(max_length=400)
  created_at = models.DateField(default=datetime.now())

  def __unicode__(self):
    return "id=%s, name='%s', email='%s', password='%s', industry='%s', picture='%s', created_at='%s'" % (
      self.id, self.name, self.email, self.password, self.industry, self.picture, self.created_at
    )

class Task(models.Model):
  description = models.CharField(max_length=140)
  company_id = models.ForeignKey(Company)
  created_at = models.DateField(default=datetime.now())

  def __unicode__(self):
    return "id=%s, description='%s', company_id=%s, created_at='%s'" % (self.id, self.description,
      self.company_id, self.created_at
    )
