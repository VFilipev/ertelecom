from django.db import models

class City(models.Model):
    label = models.CharField(max_length=255, verbose_name=u'город',)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name=u'Город'
        verbose_name_plural=u'Города'

class District(models.Model):
    label = models.CharField(max_length=255, verbose_name=u'Район',)
    city = models.ForeignKey(City, null = True,on_delete = models.CASCADE,
                              blank = True,
                              related_name='nodes')
    def __str__(self):
        return self.label
    class Meta:
        verbose_name=u'Район'
        verbose_name_plural=u'Районы'

class Street(models.Model):
    label = models.CharField(max_length=255, verbose_name=u'Улица',)
    district = models.ForeignKey(District, null = True,
                              blank = True,on_delete = models.CASCADE,
                              related_name='nodes')
    def __str__(self):
        return self.label

    class Meta:
        verbose_name=u'Улица'
        verbose_name_plural=u'Улицы'

class House(models.Model):
    label = models.CharField(max_length=255, verbose_name=u'Дом',)
    street = models.ForeignKey(Street, null = True,
                              blank = True,on_delete = models.CASCADE,
                              related_name='nodes')
    def __str__(self):
        return self.label

    class Meta:
        verbose_name=u'Улица'
        verbose_name_plural=u'Улицы'

class Entrance(models.Model):
    label = models.CharField(max_length=255, verbose_name=u'Подъезд',)
    house = models.ForeignKey(House, null = True,
                              blank = True,on_delete = models.CASCADE,
                              related_name='nodes')
    def __str__(self):
        return self.label

    class Meta:
        verbose_name=u'Подъезд'
        verbose_name_plural=u'Подъезды'
