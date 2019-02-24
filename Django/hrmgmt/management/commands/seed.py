from django.core.management.base import BaseCommand
from hrmgmt.models import Employee
# import UserFactory here
from faker import Faker

import time


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--users',
            default=200,
            type=int,
            help='The number of fake users to create.')

    def handle(self, *args, **options):
        ti = time.time()
        dct = {
            1:Employee.SR_MANAGER,
            2:Employee.MANAGER,
            3:Employee.UPPER,
            4:Employee.STANDARD,
        }
        ceo = Employee.objects.create(
        name = Faker().name(),
        date=Faker().date_between(start_date='-10y', end_date='today'),
        role=Employee.PRESIDENT,
        salary=Employee.PRESIDENT,)
        for i in range(int(options['users']/66)):
            ti = time.time()
            sr =  Employee.objects.create(
            name = Faker().name(),
            date=Faker().date_between(start_date='-10y', end_date='today'),
            role=dct[1],
            salary=dct[1],
            parent=ceo)
            man = []
            for i in range(5):
                man.append(Employee.objects.create(
                name = Faker().name(),
                date=Faker().date_between(start_date='-10y', end_date='today'),
                role=dct[2],
                salary=dct[2],
                parent=sr))
            for i in man:
                up = []
                for j in range(6):
                    up.append(Employee.objects.create(
                    name = Faker().name(),
                    date=Faker().date_between(start_date='-10y', end_date='today'),
                    role=dct[3],
                    salary=dct[3],
                    parent=i))
                for j in up:
                    Employee.objects.create(
                    name = Faker().name(),
                    date=Faker().date_between(start_date='-10y', end_date='today'),
                    role=dct[4],
                    salary=dct[4],
                    parent=j)
            print(time.time()-ti)

                #int(0.5*options['users'])
