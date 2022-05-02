from django.core.management.base import BaseCommand
from django.contrib.auth.models import User,Group,Permission
from users.models import User_test,Project,ToDo_list


class Command(BaseCommand):

    def handle(self, *args, **options):
        User_test.objects.all()
        Project.objects.all()
        ToDo_list.objects.all()

        users = [
            {'username':'maximy_test354','first_name': 'Maksim','last_name': 'Lyapko','birthday_year': 1996,'email': 'maximy_test354.pro@gmail.com'},
            {'username':'john_cena11','first_name': 'John','last_name': 'Cena','birthday_year': 1977,'email': 'john11_cena@gmail.com'}
        ]

        projects = [
            {'name': 'Android','links_repo':'github.com','user': 'maximy_test354'},
            {'name': 'Web-Site','links_repo':'github.com','user': 'maximy_test354'},
            {'name': 'Twitter','links_repo':'github.com','user': 'john_cena11'},
            {'name': 'Facebook','links_repo':'github.com','user': 'john_cena11'}
        ]

        for item in users:
            User_test.objects.create(**item)

        for item in projects:
            item['user'] = User_test.objects.get(username=item['user'])
            Project.objects.create(**item)

        User.objects.all().delete()
        Group.objects.all().delete()

        User.objects.create_superuser('admin','admin@test.com','sync1234')

        add_project = Permission.objects.get(codename='add_project')
        change_project = Permission.objects.get(codename='change_project')
        delete_project = Permission.objects.get(codename='delete_project')

        add_user = Permission.objects.get(codename='add_user')
        change_user = Permission.objects.get(codename='change_user')
        delete_user = Permission.objects.get(codename='delete_user')

        little_staff = Group.objects.create(name='Младшие сотрудники')

        little_staff.permissions.add(add_project)
        little_staff.permissions.add(change_project)
        little_staff.permissions.add(delete_project)


        big_staff = Group.objects.create(name='Старшие сотрудники')

        big_staff.permissions.add(add_project)
        big_staff.permissions.add(change_project)
        big_staff.permissions.add(delete_project)

        big_staff.permissions.add(add_user)
        big_staff.permissions.add(change_user)
        big_staff.permissions.add(delete_user)

        little = User.objects.create_user('little','little@little.com','little12345')
        little.groups.add(little_staff)
        little.save()

        big = User.objects.create_user('big','big@big.com','big123456')
        big.groups.add(big_staff)
        big.save()

        print('done')