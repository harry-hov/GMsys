from django.db import models

# Create your models here.
DEPART=(
    ('Academics','Academics'),
    ('Hostel','Accomodation'),
)
STATUS=(
    ('Solved','Solved'),
    ('Not Solved','Not Solved')
)

class Grievance(models.Model):
    name = models.CharField(max_length=20)
    enroll = models.CharField(max_length=20)
    #depart = models.CharField(max_length=20)
    depart = models.CharField(max_length=6, choices=DEPART, default='Academics')
    msg = models.CharField(max_length=200)
    #status = models.CharField(max_length=20)
    status = models.CharField(max_length=6, choices=STATUS, default='Not Solved')
    
    def __str__(self):
        return self.enroll