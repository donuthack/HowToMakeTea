from django.db import models
from .tea.Tea import Adds


class Add(models.Model):
    mame = models.CharField(max_length=255)


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
    TYPE_OF_TEA=[
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

    # additions = models.CharField()
    #
    # def is_upperclass(self):
    #     return self.additions in {self.FLOWER_TEA, self.WHITE_TEA}


class MakeTea(models.Model):
    water = models.IntegerField("Amount of water") #TODO positive integer field
    temp = models.IntegerField("Temperature") #TODO positive integer field
    typeoftea = models.CharField("Preference type of tea", max_length=255,  choices=TeaType.TYPE_OF_TEA, default=TeaType.BLACK_TEA,)
    adds = models.ManyToManyField(Add, related_name='adds_tea') #TODO __str__  повернення імя

    def __str__(self):
        return self.typeoftea
