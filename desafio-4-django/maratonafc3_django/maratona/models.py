from django.db import models
#sempre que alterar algum model no django, tem que rodar o comando makemigrations (algo assim), e depois o comando migrate
#python manage.py makemigrations
#python manage.py migrate

class Aula(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.TextField('image url')
    video_url = models.TextField('video url', default=None, blank=True, null=True)
    live_date = models.DateTimeField('live date')

    def __str__(self):
        return self.title