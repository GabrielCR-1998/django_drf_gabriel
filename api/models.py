from django.db import models

class Users(models.Model):
    class Meta:
        db_table = 'Users'
        verbose_name_plural = "Users"

    id = models.AutoField(primary_key = True)
    firstName = models.CharField(max_length = 30,blank = False)
    lastName = models.CharField(max_length = 45, blank = False)
    email = models.EmailField(max_length=254, blank = True)
    website = models.URLField(max_length = 200, blank = True)
    image = models.ImageField(upload_to = 'images', blank = True)
    
    def __str__(self) -> str:
        return f'FirsName:{self.firstName} LastName:{self.lastName} Image:{self.image}'
