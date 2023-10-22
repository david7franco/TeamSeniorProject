# Generated by Django 4.2.6 on 2023-10-22 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(1, 'To Do'), (2, 'In Progress'), (3, 'On Hold'), (4, 'Done')]),
        ),
    ]
