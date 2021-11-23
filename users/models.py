from django.db import models

USER_TYPE_CHOICES = (
    ('1' , 'Transporter'),
    ('2' , 'Operator'),
)
# Create your models here.
class Users(models.Model):
    code = models.AutoField(primary_key=True, blank=False, null=False, unique=True)
    nif = models.CharField(max_length=60)
    type = models.CharField(max_length=60, choices=USER_TYPE_CHOICES, default = '1')
    def __str__(self):
        return self.nif
    class Meta:
        managed = True
        db_table = 'users'
