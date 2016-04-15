# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand

from gym_app.models import Task, MailBox
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        """
        self.populate()

    def populate(self):
        Task.objects.all().delete()
        self.add_task(name="Esteira")
        self.add_task(name="Elíptico")
        self.add_task(name="Bicicleta")
        self.add_task(name="Rosca Inversa")
        self.add_task(name="Rosca Concentrada")
        self.add_task(name="Rosca Martelo")
        self.add_task(name="Rosca Direta")
        self.add_task(name="Rosca Alternada")
        self.add_task(name="Remada Unilateral")
        self.add_task(name="Puxada na Frente com Triângulo e Polia Alta")
        self.add_task(name="Puxada na Frente com Polia Alta")
        self.add_task(name="Puxada Alta com Braços Estendidos")
        self.add_task(name="Chest fly")
        self.add_task(name="Crucifixo")
        self.add_task(name="Crossover")
        self.add_task(name="Supino Inclinado")
        self.add_task(name="Supino Reto")
        self.add_task(name="Glúteos Quatro Apoios e Perna Estendida")
        self.add_task(name="Abdução de Quadril")
        self.add_task(name="Mesa Flexora")
        self.add_task(name="Cadeira Extensora")
        self.add_task(name="Cadeira Abdutora")
        self.add_task(name="Leg Press Inclinado")
        self.add_task(name="Remada Alta")
        self.add_task(name="Desenvolvimento com Halteres")
        self.add_task(name="Elevação Frontal")
        self.add_task(name="Elevação Lateral")
        '''
        add_group('regular')
        add_group('premium')
        add_group('personal_trainer')

        add_mail_box('admin')

        add_permission(codename = 'is_admin', name = 'It is admin')
        add_permission(codename = 'is_regular', name = 'It is regular')
        add_permission(codename = 'is_premium', name = 'It is premium')
        add_permission(codename = 'is_personal', name = 'It is personal_trainer')

        group = Group.objects.get(name='regular')
        permission = Permission.objects.get(codename = 'is_regular')
        group.permissions.add(permission)

        group = Group.objects.get(name='premium')
        permission = Permission.objects.get(codename = 'is_premium')
        group.permissions.add(permission)

        group = Group.objects.get(name='personal_trainer')
        permission = Permission.objects.get(codename = 'is_personal')
        group.permissions.add(permission)

        admin = User.objects.get(username = 'admin')
        permission = Permission.objects.get(codename = 'is_admin')
        admin.user_permissions.add(permission)
        '''
        print Task.objects.all()

    def add_task(self, name):
        a = Task.objects.get_or_create(name=name)[0]
        a.save()
        return a

    def add_group(self, name):
        g = Group.objects.get_or_create(name=name)[0]
        g.save()

    def add_permission(self, codename, name):
        content_type = ContentType.objects.get_for_model(Permission)
        p = Permission.objects.get_or_create(codename=codename,
                                             content_type=content_type)[0]
        p.name = name
        p.save()

    def add_mail_box(self, owner):
        g = MailBox.objects.get_or_create(owner=owner)[0]
        g.save()
