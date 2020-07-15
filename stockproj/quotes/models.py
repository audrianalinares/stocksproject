from django.db import models

class Stock(models.Model):
    ticker = models.Charfield(max_length=10)

    def __str__(self):
        return self.ticker