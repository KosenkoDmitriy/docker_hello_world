from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class API(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='api', on_delete=models.CASCADE)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    classes = models.CharField(max_length=100, blank=True, default='')
    methods = models.CharField(max_length=100, blank=True, default='')
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    example = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        options = self.title and {'title': self.title} or {}
        super(API, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)

