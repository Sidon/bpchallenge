# Generated by Django 3.0.4 on 2020-03-24 21:47

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountsGroup',
            fields=[
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='AccountsPermission',
            fields=[
            ],
            options={
                'verbose_name': 'Permission',
                'verbose_name_plural': 'Permissons',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.permission',),
            managers=[
                ('objects', django.contrib.auth.models.PermissionManager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(error_messages={'unique': 'This email already exists.'}, help_text='The email will be used to access the system and send information', max_length=254, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='E-mail')),
                ('name', models.CharField(help_text="Enter the user's full name.", max_length=200, null=True, verbose_name='Name')),
                ('is_active', models.BooleanField(default=True, help_text='.', verbose_name='Active?')),
                ('is_staff', models.BooleanField(default=False, help_text='Determines whether the user can access the administrative environment.', verbose_name='Only active users can access the system')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Registration date')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all the permissions granted to each of their groups.', related_name='users', related_query_name='user', to='bpauth.AccountsGroup', verbose_name='Grupos')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_permissions', related_query_name='user', to='bpauth.AccountsPermission', verbose_name='Permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
