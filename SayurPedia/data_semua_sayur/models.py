from django.db import models

# Create your models here.
class Add_Sayur(models.Model):
	nama_sayur = models.CharField(max_length=200)
	ketinggian_min = models.CharField(max_length=50)
	ketinggian_max = models.CharField(max_length=50)
	deskripsi = models.TextField()
	image = models.ImageField(upload_to='files', blank=True)

	def __str__(self):
		return "{}".format(self.nama_sayur)