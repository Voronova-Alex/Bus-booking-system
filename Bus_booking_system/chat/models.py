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
        ordering = ('date_added',)


'''
    ROOM_1 = 'Не могу заргестрироваваться'
    ROOM_2 = 'Нет возможности забронировать автобус на нужнкю дату'
    ROOM_3 = 'Не получаеться авторизоваться'
    ROOM_4 = 'Другие вопросы'

    ROOM_ALL = ((ROOM_1, 'Не могу заргестрироваваться'),
                (ROOM_2, 'Нет возможности забронировать автобус на нужнкю дату'),
                (ROOM_3, 'Не получаеться авторизоваться'),
                (ROOM_4, 'Другие вопросы'))
'''
