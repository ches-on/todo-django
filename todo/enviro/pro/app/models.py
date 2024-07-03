from django.db import models

class Task(models.Model):
    taskname= models.CharField(max_length=250)
    datecreated = models.DateTimeField(auto_now_add=True, null=True)
    starttime= models.TimeField()
    endtime = models.TimeField()
    description = models.TextField(null= True, blank=True)

    
class Meta:
    odering = ["complete)"]