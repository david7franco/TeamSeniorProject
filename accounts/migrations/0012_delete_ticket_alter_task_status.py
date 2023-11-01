# Generated by Django 4.2.4 on 2023-11-01 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_ticket'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ticket',
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(1, 'To Do'), (2, 'In Progress'), (3, 'On Hold'), (4, 'Done')], default=1),
        ),
    ]
