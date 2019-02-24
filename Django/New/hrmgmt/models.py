from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

from faker import Faker

# Create your models here.
class Employee(MPTTModel):
    STANDARD = 'STD'
    UPPER = 'UPP'
    MANAGER = 'MGR'
    SR_MANAGER = 'SRMGR'
    PRESIDENT = 'CEO'

    EMPLOYEE_TYPES = (
        (STANDARD, 'base employee'),
        (UPPER, 'upper employee'),
        (MANAGER, 'manager'),
        (SR_MANAGER, 'senior manager'),
        (PRESIDENT, 'president')
    )

    EMPLOYEE_PAYS = (
        (STANDARD, 500),
        (UPPER, 700),
        (MANAGER, 1000),
        (SR_MANAGER, 1200),
        (PRESIDENT, 1500)
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
