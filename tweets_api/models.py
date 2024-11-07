from django.db import models


class UserModel(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True, blank=False, null=False)
    senha = models.CharField(max_length=255, blank=False, null=False)
    profile = models.URLField(
        default='https://via.placeholder.com/500x500'
    )
    logged_in = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class TweetModel(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(UserModel, related_name='tweets',
                              on_delete=models.CASCADE)
    post = models.TextField(blank=False, null=False)
    image = models.URLField()

    def save(self, *args, **kwargs):
        if not self.image:
            self.image = self.owner.profile
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Tweet by {self.owner.nome}'
