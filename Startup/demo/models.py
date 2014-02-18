from django.db import models
from django.contrib.auth.models import User



#Dabase Configuration

class Todo(models.Model):
    user = models.ForeignKey(User)
    todo = models.CharField(max_length=200)
    flag = models.CharField(max_length=2, default='1')
    priority = models.CharField(max_length=2, default='0')
    pubtime = models.DateTimeField(auto_now_add=True)

	#The __unicode__() method is called whenever you call unicode() on an object. 
	#Since Django's database backends will return Unicode strings in your model's attributes, 
	#you would normally want to write a __unicode__() method for your model.

    def __unicode__(self):
        return u'%d %s %s' % (self.id, self.todo, self.flag)
                                                                                                         
    class Meta:
        ordering = ['priority', 'pubtime']