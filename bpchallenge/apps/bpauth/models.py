import uuid
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, Permission, Group)
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone

__author__ = "Sidon"
__date__ = "Created by 23/03/2020"
__email__ = "sidoncd@gmail.com"


class AccountsPermission(Permission):
    class Meta:
        proxy = True
        verbose_name = 'Permission'
        verbose_name_plural = 'Permissons'


class AccountsGroup(Group):
    class Meta:
        proxy = True
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


class UserManager(BaseUserManager):
    def create_user(self, email, name=None, password=None):
        if not email:
            raise ValueError('Users must have an email.')

        user = self.model(
            email=email,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if not password:
            password = 123456
        user = self.create_user(
            email=email,
            password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        # user.email_user('Cadastros Realizado com sucesso!',
        #                 'Login: %s | Senha: %s' % (email, password))
        return user

    def create_user_api(self, email, password=None):
        user = self.model(
            email=email,
            is_active=False,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name='E-mail', unique=True,
                              help_text='The email will be used to access the system and send information',
                              validators=[validators.EmailValidator()],
                              error_messages={
                                  'unique': "This email already exists.",
                              })
    name = models.CharField(max_length=200, verbose_name='Name',
                            help_text="Enter the user's full name.", null=True)
    is_active = models.BooleanField(default=True, verbose_name='Active?',
                                    help_text='.')
    is_staff = models.BooleanField(default=False, verbose_name='Only active users can access the system',
                                   help_text='Determines whether the user can access the administrative environment.')
    date_joined = models.DateTimeField(
        'Registration date', default=timezone.now)

    groups = models.ManyToManyField(
        AccountsGroup,
        verbose_name='Grupos',
        blank=True,
        help_text='The groups this user belongs to. '
                  'A user will get all the permissions granted to each of their groups.',
        related_name="users",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        AccountsPermission,
        verbose_name='Permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="user_permissions",
        related_query_name="user",
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        if self.name:
            return self.name
        else:
            return self.email

    get_full_name.short_description = 'Full Name'

    def get_short_name(self):
        return self.name

    get_short_name.short_description = 'Name'

    # Retorna a lista de grupos em um objeto do tipo str
    def get_groups_list(self):
        return ", ".join(p.name for p in self.groups.all())

    # Retorna a lista dos nomes dos grupos em um objeto do tipo Lista
    def get_list_groups(self):
        return [g.name for g in self.groups.all()]

    # # Retorna a lista de ids e nomes dos grupos em um objeto do tipo json
    # def get_json_groups(self):
    #     return [DictJson([['id', g.id], ['name', g.name]]) for g in self.groups.all()]

    get_groups_list.short_description = 'Grupos'

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.email

    def clean(self):
        super(User, self).clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
