from django.db import models
from django.urls import reverse


class Library(models.Model):
    name = models.CharField('название',max_length = 150 )
    text = models.TextField('описание', max_length = 5000)
    map = models.CharField('местоположение', max_length = 150)
    slug = models.SlugField(unique=True, max_length=150)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'библиотека'
        verbose_name_plural = 'библиотеки'

    def get_absolute_url(self):
        return reverse('library_detail', kwargs ={'slug':self.slug })




class Author(models.Model):
    name = models.CharField('имя автора', max_length = 150)
    description = models.TextField('описание автора', max_length = 7000)
    year = models.SmallIntegerField('возраст', default = 0)
    libraries = models.ManyToManyField(Library, verbose_name= 'Библиотеки', related_name= 'author_library')
    image = models.ImageField(upload_to = 'authors/')
    slug = models.SlugField(unique = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'


    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'slug': self.slug})




class Book(models.Model):
    title = models.CharField('название книжки', max_length=150)
    description = models.TextField('описание')
    author = models.ForeignKey(Author, verbose_name='Автор книги',  on_delete= models.CASCADE)
    age = models.SmallIntegerField('рекомендуемый возраст')
    price = models.SmallIntegerField('цена книги')

    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'Книжка'
        verbose_name_plural = 'книги'

    def get_absolute_url(self):
        return reverse('book_detail', kwargs = {'pk_id': self.pk})
