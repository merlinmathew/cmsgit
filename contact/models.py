from django.db import models

class ContactModel(models.Model):

    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField( unique=False)
    message = models.TextField()


    def __str__(self):
        return 'Name: %s ,Email : %s' %(self.contact_name,self.contact_email)

