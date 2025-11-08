from django.db import models


class GuestBookReview(models.Model):
    status_choices = [
        ('active', 'active'),
        ('blocked', 'blocked'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=status_choices, default='active')

    def _str_(self):
        return f'{self.name} ({self.email})'