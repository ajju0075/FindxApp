from django.db import models

# Create your models here.
class FeedbackModel(models.Model): #model for feedback form 
    name = models.CharField(max_length= 30)
    email = models.EmailField()
    subject = models.CharField(max_length= 20)
    message = models.TextField()
    # is_replaid = models.BooleanField(default= False)
    # status = models.BooleanField(default=False)
    # created_on = models.DateTimeField(auto_now_add=True)
    # updated_on = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.subject



