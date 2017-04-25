from django.db import models

# Create your models here.

class Questao(models.Model):
	pergunta = models.CharField(max_length=100)
	a = models.CharField(max_length=100)
	b = models.CharField(max_length=100)
	c = models.CharField(max_length=100)
	d = models.CharField(max_length=100)
	resposta = models.CharField(max_length=1)

	def __str__(self):
		return "pergunta: %s - resposta: %s" % (self.pergunta, self.resposta)