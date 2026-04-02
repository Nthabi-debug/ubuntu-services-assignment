from django.db import models

class Report(models.Model):
    CATEGORY_CHOICES = [
        ('pothole', 'Pothole'),
        ('water', 'Water Leak'),
        ('electricity', 'Electricity Fault'),
        ('waste', 'Waste Collection'),
    ]

    STATUS_CHOICES = [
        ('received', 'Received - We have your report'),
        ('in_progress', 'In Progress - A team is working on it'),
        ('resolved', 'Resolved - Issue has been fixed'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='report_photos/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='received')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_category_display()} - {self.created_at}"