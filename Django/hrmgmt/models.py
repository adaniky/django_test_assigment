from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Employee(MPTTModel):
    STANDARD = 'STD'
    MANAGER = 'MGR'
    SR_MANAGER = 'SRMGR'
    PRESIDENT = 'PRES'

    EMPLOYEE_TYPES = (
        (STANDARD, 'base employee'),
        (MANAGER, 'manager'),
        (SR_MANAGER, 'senior manager'),
        (PRESIDENT, 'president')
    )

    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', null=True, related_name='employee', on_delete=models.CASCADE)

    def __str__(self):
        return "<EmployeeMptt: {} {}".format(self.first_name, self.last_name)

    def __repr__(self):
        return self.__str__()
