from django.db import models
from django.urls import reverse
from model_utils import Choices


class GroupInformation(models.Model):
    PI_name = models.CharField(default='PI Name', max_length=200)
    PI_position = models.CharField(default='PI Position', max_length=200)
    group_name = models.CharField(default='e.g., Soft Matter', max_length=200)
    group_def = models.CharField(
        default='e.g., Lab, Group, etc.', max_length=200)
    group_short_description = models.CharField(
        default='e.g., Soft Matter at Interfaces', max_length=200)
    group_long_description = models.TextField(
        default='We do research on...')

    def __str__(self):
        return self.group_name


class ResearchField(models.Model):
    topic = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()
    main_image = models.ImageField(
        upload_to='research_field_images', blank=True)

    def __str__(self):
        return self.topic


class ContactRequest(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    contact_info = models.CharField(max_length=200)

    def __str__(self):
        return self.text[:50]

    def get_absolute_url(self):
        return reverse('contact_request_acknowledged')


class Publications(models.Model):
    authors = models.TextField()
    year = models.IntegerField()
    title = models.TextField()
    journal = models.CharField(max_length=200)
    volume = models.IntegerField()
    initialPage = models.IntegerField()
    PUBLICATION_TYPE = Choices('Paper', 'Review', 'Chapter', 'Proceeding')
    publication_type = models.CharField(
        choices=PUBLICATION_TYPE,
        default=PUBLICATION_TYPE.Paper,
        max_length=20)

    def __str__(self):
        return '%s %s' % (self.journal, str(self.year))

    class Meta:
        verbose_name_plural = "Publications"
        

class Member(models.Model):
    name = models.CharField(max_length=200)
    POSITION = Choices('PI', 'Postdoc', 'PhD', 'Technician', 'MSc', 'Guest_PhD', 'Guest_Student')
    position = models.CharField(choices=POSITION, default=POSITION.PhD, max_length=20)
    initial_year = models.IntegerField()
    final_year = models.IntegerField()
    main_image = models.ImageField(
        upload_to='members_images', blank=True)
    email = models.EmailField(max_length=70, blank=True)

    def __str__(self):
        return '%s %s' % (self.name, str(self.initial_year))
