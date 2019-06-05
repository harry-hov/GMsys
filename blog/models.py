import datetime
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


def grievance_number():
    last_grievance = Grievance.objects.all().order_by('id').last()
    if not last_grievance:
        return 'GMS' + str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + '0000'
    grievance_id = last_grievance.grievance_id
    grievance_int = int(grievance_id[9:13])
    new_grievance_int = grievance_int + 1
    new_grievance_id = 'GMS' + str(str(datetime.date.today().year)) + str(datetime.date.today().month).zfill(2) + str(new_grievance_int).zfill(4)
    return new_grievance_id

class Grievance(models.Model):
    grievance_id = models.CharField(max_length = 20, editable=False, default=grievance_number)
    name = models.CharField(max_length=20)
    enroll = models.CharField(max_length=20)
    #depart = models.CharField(max_length=20)
    depart = models.CharField(max_length=6, choices=DEPART, default='Academics')
    msg = models.CharField(max_length=200)
    #status = models.CharField(max_length=20)
    status = models.CharField(max_length=6, choices=STATUS, default='Not Solved')
    
    def __str__(self):
        #return self.enroll
        return self.grievance_id
'''
    def __iter__(self):
        return [self.grievance_id, 
                self.name, 
                self.enroll, 
                self.depart, 
                self.msg, 
                self.status,]
'''

    