<<<<<<< HEAD
# Generated by Django 4.2.6 on 2023-11-08 14:14
=======
# Generated by Django 4.2.7 on 2023-11-08 01:58
>>>>>>> Added Open Ticket button to resident dashboard

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('floor', models.PositiveIntegerField(default=0)),
                ('assingor', models.CharField(default='Null', max_length=200)),
                ('description', models.TextField()),
                ('status', models.IntegerField(choices=[(1, 'To Do'), (2, 'In Progress'), (3, 'On Hold'), (4, 'Done')], default=1)),
                ('priority', models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=1)),
                ('date_posted', models.DateTimeField(default=datetime.datetime.now)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='TextEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResidentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('residentName', models.CharField(max_length=200)),
                ('floor', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='resident_creates_ticket',
            fields=[
                ('resident_creates_ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('FK_resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('FK_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.task')),
            ],
        ),
        migrations.CreateModel(
            name='RaUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.PositiveIntegerField()),
                ('ra_name', models.CharField(max_length=200)),
                ('room_number', models.PositiveIntegerField()),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('date_posted', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('fk_task_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='accounts.task')),
            ],
        ),
        migrations.CreateModel(
            name='Annotations',
            fields=[
                ('annotate_id', models.AutoField(primary_key=True, serialize=False)),
                ('annotations', models.TextField()),
                ('date_posted', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('fk_task_annotations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annotations', to='accounts.task')),
            ],
        ),
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
