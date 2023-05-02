from django.db import models


class LoadFiles(models.Model):
    inputFile = models.FileField(upload_to='')
    file_ext = models.CharField(max_length=10, null=True)
    file_link = models.CharField(max_length=250, null=True)
    file_name = models.CharField(max_length=100, null=True)
    newfolder = models.CharField(max_length=15, null=True)
    clean = models.CharField(max_length=15, null=True)
    divide = models.CharField(max_length=15, null=True)
    convert = models.CharField(max_length=15, null=True)
    json = models.CharField(max_length=15, null=True)
    compress = models.CharField(max_length=15, null=True)
    loadtosql = models.CharField(max_length=15, null=True)
    convert = models.CharField(max_length=15, null=True)
    downloads = models.IntegerField(null=True,)
    views = models.IntegerField(null=True,)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    clasify_at = models.DateTimeField(null=True)
    published_at = models.DateTimeField(null=True)
    updated = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return str(self.file_name)
