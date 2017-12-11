# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.six import python_2_unicode_compatible



# Create your models here.

# @python_2_unicode_compatible 装饰器用于兼容python 2
# 如果使用python2 的环境可以使用__unicode__代替__str__


@python_2_unicode_compatible
class Category(models.Model):
	name = models.CharField(max_length = 100)
	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Tag(models.Model):
	name = models.CharField(max_length = 100)
	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Post(models.Model):
	# 文章标题
	title = models.CharField(max_length = 70)
	# 文章正文
	body = models.TextField()
	# 创建时间 最后修改时间
	created_time = models.DateField()
	modified_time = models.DateField()
	# 文章摘要 允许为空
	excerpt = models.CharField(max_length = 200,blank = True)
	# 分类与标签
	category = models.ForeignKey(Category)
	tag = models.ManyToManyField(Tag,blank = True)
	# 作者
	author = models.ForeignKey(User)
	def __str__(self):
		return self.title

	# 通过Meta类来指定一些属性 
	# 如果created_time相同就通过title排序 -:表示逆序
	class Meta():
		ordering = ['-created_time','title']


	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk':self.pk})

		
		
		