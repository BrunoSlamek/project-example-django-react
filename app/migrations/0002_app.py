# Generated by Django 3.2.5 on 2021-07-29 02:33

from django.db import migrations

def create_data(apps, schema_editor):
        Customer = apps.get_model('app', 'Customer')
        Customer(first_name="Customer 001", last_name="Customer 001", email="customer001@email.com", phone="00000000",
                 address="Customer 000 Address", description= "Customer 001 description").save()


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
