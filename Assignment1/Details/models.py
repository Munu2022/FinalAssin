from django.db import models
import datetime as dt
from datetime import date
from .validators import validate_lastname, date_of_birth, dept_name
# Create your models here.
class Students(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255, validators=[validate_lastname])
    dob = models.DateField(validators=[date_of_birth])
    roll_number = models.IntegerField()
    department = models.CharField(max_length=255, validators=[dept_name])
    course = models.CharField(max_length=255)
    semester_num = models.IntegerField()
    marks = models.IntegerField()
    age = models.IntegerField(default=0)

    # @property
    # def calc_age(self):
    #     today = date.today()
    #     temp = self.dob
    #     age =  today.year - temp.year - ((today.month, today.day) < (temp.month, temp.day))
    #     return age



    # @property
    # def calc_age(self):
    #     today_date = dt.datetime.today()
    #     temp= str(self.dob)
    #     dob_year = dt.datetime.strptime(temp,"%Y-%m-%d").date().year
    #     age = today_date.year - dob_year
    #     return age

    # def __str__(self):
    #     "in admin site"
    #     return str(self.calc_age)

class Departmant(models.Model):
    department = models.CharField(max_length=255)
    num_course = models.IntegerField()
    num_teachers = models.IntegerField()
    students = models.ForeignKey(Students, on_delete=models.CASCADE, blank=True, null= True)



