from django.db import models
import uuid

# Create your models here.


class Product(models.Model):

	prod_name = models.CharField(max_length=200, null=True,blank=False)
	prod_tags = models.ManyToManyField('Tag',blank=True)
	prod_description = models.TextField(null=True,blank=True)
	prod_amount = models.IntegerField(default=0,null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	prod_expires = models.DateField(null=True,blank=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

	def __str__(self):
		return self.prod_name


class Tag(models.Model):
	name = models.CharField(max_length=200,null=True,blank=False)
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

	def __str__(self):
		return self.name
