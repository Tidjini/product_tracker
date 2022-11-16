from django.db import models


class Encaissement(models.Model):

    reference = models.CharField(max_length=10, primary_key=True)
    label = models.CharField(max_length=100)
    date_range = models.CharField(max_length=50, null=True)
    value = models.DecimalField(max_digits=30, decimal_places=3)
    previous_value = models.DecimalField(max_digits=30, decimal_places=3)

    @property
    def growth_loss(self):
        if self.previous_value == 0:
            return 100

        diff = self.value - self.previous_value
        percent = diff * 100 / self.previous_value
        return percent
