from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass 

    def __str__(self): #reserved python method - if there is an object, we are dictating how to display the string version of the user.
        return self.username
