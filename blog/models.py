from django.db import models


class Blog(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=70,
        help_text='Написать заголовок',
        unique=True
    )
    slug = models.SlugField('URL', max_length=40, default='')
    content = models.TextField('Текст статьи', help_text='Напишите текст статьи', blank=True)
    photo = models.ImageField('Фото', upload_to='images/%Y/%m/%d/')
    time_create = models.DateTimeField('Время создания', auto_now_add=True)
    time_update = models.DateTimeField('Время изменения', auto_now=True)
    is_published = models.BooleanField('Публикация', default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create', 'title']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Gallery(models.Model):
    title = models.CharField('Название фото', max_length=50)
    image = models.ImageField('Изображение', upload_to='images/gallery')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Comment(models.Model):
    post = models.ForeignKey('Blog',  on_delete=models.NOT_PROVIDED, null=True, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(help_text='Введите email:')
    body = models.TextField(help_text='Напишите комментарий:')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)

