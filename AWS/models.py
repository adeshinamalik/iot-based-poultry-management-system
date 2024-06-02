from django.db import models


# Create your models here.
class EggCollection(models.Model):
    # LastEggDate = models.DateField()
    # LastEggTime = models.TimeField()
    StartEggDateTime = models.DateTimeField(blank=True)
    StopEggDateTime = models.DateTimeField(blank=True)
    EggDuration = models.IntegerField(default=0, blank=True)
    NextEggDateTime = models.DateTimeField(blank=True)
    EggQuantity = models.IntegerField(default=0)
    EggWeight = models.IntegerField(default=0)
    EggStatus = models.BooleanField(default=False)
    EggSystemFault = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.StartEggDateTime = self.StopEggDateTime.replace(tzinfo=None)
        self.StopEggDateTime = self.StopEggDateTime.replace(tzinfo=None)
        self.NextEggDateTime = self.NextEggDateTime.replace(tzinfo=None)
        super(EggCollection, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.StopEggDateTime.replace(tzinfo=None))


class WasteCollection(models.Model):
    # LastWasteDate = models.DateField()
    # LastWasteTime = models.TimeField()
    StartWasteDateTime = models.DateTimeField(blank=True)
    StopWasteDateTime = models.DateTimeField(blank=True)
    NextWasteDateTime = models.DateTimeField(blank=True)
    #CurrentDuration = models.IntegerField(default=0)
    WasteDuration = models.IntegerField(default=0)
    WasteStatus = models.BooleanField(default=False)
    WasteSystemFault = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.StartWasteDateTime = self.StartWasteDateTime.replace(tzinfo=None)
        self.StopWasteDateTime = self.StopWasteDateTime.replace(tzinfo=None)
        self.StopRefillDateTime = self.NextWasteDateTime.replace(tzinfo=None)
        super(WasteCollection, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.StopWasteDateTime.replace(tzinfo=None))


class Feeding(models.Model):
    # LastFeedingDate = models.DateField()
    # LastFeedingTime = models.TimeField()
    StartFeedingDateTime = models.DateTimeField(blank=True)
    StopFeedingDateTime = models.DateTimeField(blank=True)
    FeedWeight = models.IntegerField(default=0)
    FeedingDuration = models.IntegerField(default=0)
    NextFeedingDateTime = models.DateTimeField(blank=True)
    FeedingStatus = models.BooleanField(default=False)
    FeedingSystemFault = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        self.StopFeedingDateTime = self.StopFeedingDateTime.replace(tzinfo=None)
        self.StopFeedingDateTime = self.StopFeedingDateTime.replace(tzinfo=None)
        self.NextFeedingDateTime = self.NextFeedingDateTime.replace(tzinfo=None)
        super(Feeding, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.StartFeedingDateTime.replace(tzinfo=None))


class Water(models.Model):
    # LastRefillDate = models.DateField()
    # LastRefillTime = models.TimeField()
    # StartRefillDateTime = models.DateTimeField(auto_now_add=True, blank=True)
    StartRefillDateTime = models.DateTimeField(blank=True)
    StopRefillDateTime = models.DateTimeField(blank=True)
    RefillDuration = models.IntegerField(default=0)
    RefillStatus = models.BooleanField(default=False)
    WaterSystemFault = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.StartRefillDateTime = self.StartRefillDateTime.replace(tzinfo=None)
        self.StopRefillDateTime = self.StopRefillDateTime.replace(tzinfo=None)
        super(Water, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.StartRefillDateTime.replace(tzinfo=None))

