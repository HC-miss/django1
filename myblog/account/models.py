from django.db import models


class User(models.Model):
    uname = models.CharField(max_length=20, unique=True)
    userpi = models.CharField(max_length=30, null=True, blank=True)
    pwd = models.CharField(max_length=20)
    userinfo = models.CharField(max_length=50, null=True)
    created = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='userimg', null=True)
    email = models.CharField(max_length=30, null=True)


    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.uname
