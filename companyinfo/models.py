from django.db import models
from django.utils.translation import gettext as _

class Company(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    logo = models.ImageField(_('Logo'), upload_to='companyinfo/logos/', default='companyinfo/logos/logo.png', blank=True, null=True)
    subtitle = models.CharField(_('Subtitle'), max_length=255)
    call_us = models.CharField(_('Call Us'), max_length=20)
    email_us = models.EmailField(_('Email Us'))
    fb_link = models.URLField(_('Facebook Link'), null=True, blank=True)
    twit_link = models.URLField(_('Twitter Link'), null=True, blank=True)
    insta_link = models.URLField(_('Instagram Link'), null=True, blank=True)
    emails = models.TextField(_('Emails'))
    numbers = models.TextField(_('Numbers'))
    address = models.TextField(_('Address'))

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'companyinfo'
        verbose_name = _('Company Info')
        verbose_name_plural = _('Company Info')
