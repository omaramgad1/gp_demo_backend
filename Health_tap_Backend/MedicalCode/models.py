from django.db import models
from Patient.models import Patient
from django.utils import timezone
from Appointment.models import Appointment


class MedicalEditCode(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.RESTRICT, related_name='medical_edit_codes')
    code = models.CharField(max_length=10, unique=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()
    appointment = models.OneToOneField(
        Appointment, on_delete=models.RESTRICT)

    STATUS_CHOICES = (
        ('V', 'Valid'),
        ('E', 'Expired'),
    )
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default='V')

    class Meta:
        verbose_name_plural = 'Medical Edit Codes'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
            self.expired_at = self.created_at + timezone.timedelta(hours=1)
            self.status = 'V'
            print(f'Saving new instance with status {self.status}')
        if timezone.now() >= self.expired_at:
            self.status = 'E'
        return super().save(*args, **kwargs)

    def is_valid(self):
        return timezone.now() <= self.expired_at and self.status == 'V'

    def __str__(self):
        return self.code
