from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birth_date = models.DateField(null=True, blank=True)
    about_me = models.CharField(max_length=140, null=True, blank=True)
    url_list = models.URLField(max_length=140, null=True, blank=True)
    photo = models.ImageField(upload_to='uploads/',  null=True, blank=True)
    friends = models.ManyToManyField('UserProfile', through='friends', related_name='folowwed_by')

    def __str__(self):
        return self.user.username


class Friends(models.Model):
    followed = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='followed')
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='follower')
    start_following = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('followed', 'follower')


    def save(self, *args, **kwargs):
        if self.followed != self.follower:
            super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.follower} followed {self.followed} at {self.start_following}'

