from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

TYPE_OF_USER = (
    ("admin", "Admin"),
    ("member", "Member"),
)


class Manager(UserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields["is_superuser"] = True
        extra_fields["is_staff"] = True
        super(Manager, self).create_superuser(
            username, email, password, **extra_fields
        )


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.URLField(blank=True, null=True)
    mobile = models.CharField(max_length=12)
    is_blocked_user = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    user_type = models.CharField(max_length=32, choices=TYPE_OF_USER)
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_expiry = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.email

    objects = Manager()


class ActiveToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jti = models.CharField(max_length=200, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)


class AbstractModel(models.Model):
    creator = models.ForeignKey(
        "user.User",
        blank=True,
        null=True,
        related_name="creator_%(class)s_objects",
        on_delete=models.SET_NULL,
    )
    updater = models.ForeignKey(
        "user.User",
        blank=True,
        null=True,
        related_name="updater_%(class)s_objects",
        on_delete=models.SET_NULL,
    )
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
