from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

#from faker import Faker

# Create your models here.
class Employee(MPTTModel):
    JUNIOR = 'JUN'
    STANDARD = 'STD'
    UPPER = 'UPP'
    MANAGER = 'MGR'
    SR_MANAGER = 'SRMGR'
    PRESIDENT = 'CEO'

    EMPLOYEE_TYPES = (
        (JUNIOR, 'junior employee'),
        (STANDARD, 'base employee'),
        (UPPER, 'upper employee'),
        (MANAGER, 'manager'),
        (SR_MANAGER, 'senior manager'),
        (PRESIDENT, 'president')
    )

    EMPLOYEE_PAYS = (
        (JUNIOR, 500),
        (STANDARD, 800),
        (UPPER, 1200),
        (MANAGER, 1500),
        (SR_MANAGER, 2000),
        (PRESIDENT, 3000)
)
# Employee.objects.create(name = Faker().name(), date=Faker().date_between(start_date='-10y', end_date='today'),role=Employee.PRESIDENT, salary=Employee.PRESIDENT)
    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES)
    salary = models.CharField(max_length=25, choices=EMPLOYEE_PAYS, null=True)
    date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True)

    parent = TreeForeignKey('self', null=True, related_name='employee', on_delete=models.CASCADE)

    def __str__(self):
        return "<EmployeeMptt: {}".format(self.name)

    def __repr__(self):
        return self.__str__()
