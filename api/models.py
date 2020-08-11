from django.db import models
from .tea.Tea import Adds


class Add(models.Model):
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField("Amount")

    def __str__(self):
        return self.name


class TeaType(models.Model):
    BLACK_TEA = "BL"
    GREEN_TEA = "GT"
    OOLONG_TEA = "OO"
    WHITE_TEA = "WH"
    PUER_TEA = "PU"
    EARL_GREY = "EG"
    JASMINE_TEA = "JS"
    MASSALA_TEA = "MS"
    FRUIT_TEA = "FT"
    FLOWER_TEA = "FL"
    LEAF_TEA = "LF"
    TYPE_OF_TEA = [
        (BLACK_TEA, "black"),
        (GREEN_TEA, "green"),
        (OOLONG_TEA, "oolong"),
        (WHITE_TEA, "white"),
        (PUER_TEA, "puer"),
        (EARL_GREY, "earl grey"),
        (JASMINE_TEA, "jasmine"),
        (MASSALA_TEA, "massala"),
        (FRUIT_TEA, "fruit"),
        (FLOWER_TEA, "flower"),
        (LEAF_TEA, "leaf"),
    ]

    # additions = models.CharField(max_length=255)

    # def __str__(self):
    #     return self.additions

    # def is_upperclass(self):
    #     return self.additions in {self.FLOWER_TEA, self.WHITE_TEA}


class MakeTea(models.Model):
    water = models.PositiveIntegerField("Amount of water")
    temp = models.PositiveIntegerField("Temperature")
    typeoftea = models.CharField("Preference type of tea", max_length=255, choices=TeaType.TYPE_OF_TEA,
                                 default=TeaType.BLACK_TEA, )
    adds = models.ManyToManyField(Add, related_name='adds_tea')

    def __str__(self):
        return self.typeoftea


