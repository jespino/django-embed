from django.db import models
from embed.register import register

def EmbededContent(models.Model):
    content_id = models.TextField(null=False, blank=False)
    content_type = models.SlugField(choices=register.get_content_types(),
                                    null=False, blank=False)

    class Meta:
        unique_toguether = (content_id, content_type)
