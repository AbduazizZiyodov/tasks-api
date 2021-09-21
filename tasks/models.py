from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=50)
    description = models.TextField(blank=False)

    created_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        null=True,
        to=get_user_model(),
        on_delete=models.SET_NULL
    )

    def __str__(self) -> str:
        return "Task({},{})".format(self.id, self.user.username)
