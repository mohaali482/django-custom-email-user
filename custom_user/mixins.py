from django.db import models
from django.utils.translation import gettext_lazy as _

class TimestampMixin(models.Model):
    created_at = models.DateTimeField(verbose_name=_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Updated At"), auto_now=True)
    deleted_at = models.DateTimeField(verbose_name=_("Deleted At"), blank=True, null=True, editable=False)

    class Meta:
        abstract = True