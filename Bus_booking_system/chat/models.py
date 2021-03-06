from django.db import models



class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    room_url = models.URLField(default=None)


    def __str__(self):
        return f'{self.username}-{self.room}'

    class Meta:
        ordering = ('-date_added',)


