# -*- coding: UTF-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

from gym_app.models import Task, MailBox
from django.contrib.auth.models import Permission, Group, User
from django.contrib.contenttypes.models import ContentType



def populate():
    Task.objects.all().delete()
    add_Task(name = "Esteira")
    add_Task(name = "Elíptico")
    add_Task(name = "Bicicleta")
    add_Task(name = "Rosca Inversa")
    add_Task(name = "Rosca Concentrada")
    add_Task(name = "Rosca Martelo")
    add_Task(name = "Rosca Direta")
    add_Task(name = "Rosca Alternada")
    add_Task(name = "Remada Unilateral")
    add_Task(name = "Puxada na Frente com Triângulo e Polia Alta")
    add_Task(name = "Puxada na Frente com Polia Alta")
    add_Task(name = "Puxada Alta com Braços Estendidos")
    add_Task(name = "Chest fly")
    add_Task(name = "Crucifixo")
    add_Task(name = "Crossover")
    add_Task(name = "Supino Inclinado")
    add_Task(name = "Supino Reto")
    add_Task(name = "Glúteos Quatro Apoios e Perna Estendida")
    add_Task(name = "Abdução de Quadril")
    add_Task(name = "Mesa Flexora")
    add_Task(name = "Cadeira Extensora")
    add_Task(name = "Cadeira Abdutora")
    add_Task(name = "Leg Press Inclinado")
    add_Task(name = "Remada Alta")
    add_Task(name = "Desenvolvimento com Halteres")
    add_Task(name = "Elevação Frontal")
    add_Task(name = "Elevação Lateral")
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

def add_Task(name):
    a = Task.objects.get_or_create(name = name)[0]
    a.save()
    return a

def add_group(name):
    g = Group.objects.get_or_create(name = name)[0]
    g.save()

def add_permission(codename, name):
    content_type = ContentType.objects.get_for_model(Permission)
    p = Permission.objects.get_or_create(codename = codename, content_type = content_type)[0]
    p.name = name
    p.save()

def add_mail_box(owner):
    g = MailBox.objects.get_or_create(owner = owner)[0]
    g.save()


# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()