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
        num = Employee.objects.all().count()
        Employee.objects.all().delete()
        print(f"All {num} employee droped")
        ti = time.time()
        dct = {
            1:Employee.SR_MANAGER,
            2:Employee.MANAGER,
            3:Employee.UPPER,
            4:Employee.STANDARD,
            5:Employee.JUNIOR
        }
        fk = Faker()
        ceo = Employee.objects.create(
        name = fk.name(),
        date=fk.date_between(start_date='-10y', end_date='today'),
        role=Employee.PRESIDENT,
        salary=Employee.PRESIDENT,)
        count = 0
        for s in range(10):
            count += 1
            sr =  Employee.objects.create(
            name = fk.name(),
            date=fk.date_between(start_date='-10y', end_date='today'),
            role=dct[1],
            salary=dct[1],
            parent=ceo)
            for m in range(5):
                count += 1
                man = Employee.objects.create(
                name = fk.name(),
                date=fk.date_between(start_date='-8y', end_date='today'),
                role=dct[2],
                salary=dct[2],
                parent=sr)
                for u in range(5):
                    count += 1
                    up = Employee.objects.create(
                    name = fk.name(),
                    date=fk.date_between(start_date='-6y', end_date='today'),
                    role=dct[3],
                    salary=dct[3],
                    parent=man)
                    for st in range(7):
                        count += 1
                        std = Employee.objects.create(
                        name = fk.name(),
                        date=fk.date_between(start_date='-4y', end_date='today'),
                        role=dct[4],
                        salary=dct[4],
                        parent=up)
                        for j in range(2):
                            count += 1
                            jun = Employee.objects.create(
                            name = fk.name(),
                            date=fk.date_between(start_date='-2y', end_date='today'),
                            role=dct[5],
                            salary=dct[5],
                            parent=std)
                            print(jun, std, up, man, sr, count)


        # for i in range(int(options['users']/66)):
        #     ti = time.time()
        #     sr =  Employee.objects.create(
        #     name = Faker().name(),
        #     date=Faker().date_between(start_date='-10y', end_date='today'),
        #     role=dct[1],
        #     salary=dct[1],
        #     parent=ceo)
        #     man = []
        #     for i in range(5):
        #         man.append(Employee.objects.create(
        #         name = Faker().name(),
        #         date=Faker().date_between(start_date='-10y', end_date='today'),
        #         role=dct[2],
        #         salary=dct[2],
        #         parent=sr))
        #     for i in man:
        #         up = []
        #         for j in range(6):
        #             up.append(Employee.objects.create(
        #             name = Faker().name(),
        #             date=Faker().date_between(start_date='-10y', end_date='today'),
        #             role=dct[3],
        #             salary=dct[3],
        #             parent=i))
        #         for j in up:
        #             Employee.objects.create(
        #             name = Faker().name(),
        #             date=Faker().date_between(start_date='-10y', end_date='today'),
        #             role=dct[4],
        #             salary=dct[4],
        #             parent=j)
        #     print(time.time()-ti)

                #int(0.5*options['users'])
