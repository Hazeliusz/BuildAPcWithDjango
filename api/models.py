from django.db import models

class PcComponent(models.Model):
    name = models.CharField(max_length=100, null=False)
    max_fps = models.IntegerField(null=False)
    img_source = models.CharField(max_length=100)
    price = models.IntegerField(null=False)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Case(PcComponent):
    pass

class Cpu(PcComponent):
    pass

class Gpu(PcComponent):
    pass

class Motherboard(PcComponent):
    pass

class Psu(PcComponent):
    pass

class Ssd(PcComponent):
    pass

class Game(models.Model):
    title = models.CharField(max_length=100, null=False)
    demand_value = models.FloatField(null=False)

    def __str__(self):
        return self.title
