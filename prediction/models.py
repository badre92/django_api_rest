

# Create your models here.


"""
- CRIM     per capita crime rate by town
- ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
- INDUS    proportion of non-retail business acres per town
- CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
- NOX      nitric oxides concentration (parts per 10 million)
- RM       average number of rooms per dwelling
- AGE      proportion of owner-occupied units built prior to 1940
- DIS      weighted distances to five Boston employment centres
- RAD      index of accessibility to radial highways
- TAX      full-value property-tax rate per $10,000
- PTRATIO  pupil-teacher ratio by town
- B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
- LSTAT    % lower status of the population
- MEDV     Median value of owner-occupied homes in $1000's
"""
from django.db       import models
class House(models.Model):
    CRIM    = models.FloatField()
    ZN      = models.FloatField()
    INDUS   = models.FloatField()
    CHAS    = models.FloatField()
    NOX     = models.FloatField()
    RM      = models.FloatField()
    AGE     = models.FloatField()
    DIS     = models.FloatField()
    RAD     = models.FloatField()
    TAX     = models.FloatField()
    PTRATIO = models.FloatField()
    B       = models.FloatField()
    LSTAT   = models.FloatField()
    MEDV    = models.FloatField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']



