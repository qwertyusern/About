from django.db import models

class Maqola(models.Model):
    sarlavha=models.CharField(max_length=30)
    sana=models.DateField(auto_now_add=True)
    matn=models.TextField()
    rasm=models.FileField(blank=True, upload_to="maqola_rasm")

    def __str__(self):
        return self.sarlavha
class Intervyu(models.Model):
    link=models.URLField()
    sana=models.DateField(auto_now_add=True)
    sarlavha=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.sarlavha} {self.sana}"



