from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField('русское название', max_length=200)
    title_en = models.CharField('английское название',
                                max_length=200, blank=True)
    title_jp = models.CharField('японское название',
                                max_length=200, blank=True)
    image = models.ImageField('картинка',
                              upload_to='images/')
    description = models.TextField('описание', blank=True)
    previous_evolution = models.ForeignKey('self',
                                           verbose_name='из кого эволюционирует',
                                           on_delete=models.SET_NULL,
                                           related_name='next_evolution',
                                           blank=True, null=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon,
                                verbose_name='покемон',
                                on_delete=models.CASCADE,
                                related_name='entities')
    lat = models.FloatField('широта')
    lon = models.FloatField('долгота')
    appeared_at = models.DateTimeField('время появления',
                                       blank=True, null=True)
    disappeared_at = models.DateTimeField('время исчезновения',
                                          blank=True, null=True)
    level = models.IntegerField('уровень', blank=True, null=True)
    health = models.IntegerField('здоровье', blank=True, null=True)
    strength = models.IntegerField('атака', blank=True, null=True)
    defence = models.IntegerField('защита', blank=True, null=True)
    stamina = models.IntegerField('выносливость', blank=True, null=True)

    def __str__(self):
        return f'Сущность покемона {self.id}'
