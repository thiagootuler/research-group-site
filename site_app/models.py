import json
from django.db import models


class Apresentacao(models.Model):
    texto = models.TextField(max_length=500)


class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    _autores = models.CharField(max_length=250)
    capa = models.CharField(max_length=100)
    miniatura = models.CharField(max_length=100)
    resumo = models.TextField(max_length=500)
    citacoes = models.CharField(max_length=250)
    qualis = models.FloatField()
    doi = models.CharField(max_length=100)

    @property
    def autores(self):
        return json.loads(self._autores)


class Membro(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.CharField(max_length=50)
    lattes = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)
    resumo = models.TextField(max_length=250)


class Localizacao(models.Model):
    _logradouro = models.CharField(max_length=100)
    _numero = models.CharField(max_length=10)
    _bairro = models.CharField(max_length=50)
    _cidade = models.CharField(max_length=100)
    _uf = models.CharField(max_length=2)

    def __str__(self):
        return "{}, {} - {}, {}/{}".format(
            self._logradouro,
            self._numero,
            self._bairro,
            self._cidade,
            self._uf
        )


class Coordenada(models.Model):
    _logitude = models.FloatField()
    _latitude = models.FloatField()
    _altitude = models.IntegerField()

    def __str__(self):
        return ','.join([str(self._logitude), str(self._latitude), str(self._altitude)])


class Endereco(models.Model):
    grupo = models.TextField(max_length=50)
    instituicao = models.TextField(max_length=100)
    departamento = models.TextField(max_length=100)
    _localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    _cep = models.CharField(max_length=8)
    _coordenada = models.ForeignKey(Coordenada, on_delete=models.CASCADE)

    @property
    def localizacao(self):
        return str(self._localizacao)

    @property
    def cep(self):
        cep = self._cep
        return "%s.%s-%s" % (cep[0:2], cep[2:5], cep[5:8])

    @property
    def coordenada(self):
        return str(self._coordenada)


class Contato(models.Model):
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    _telefone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    mapa = models.TextField(max_length=250)

    @property
    def telefone(self):
        tel = self._telefone
        return "(%s) %s - %s" % (tel[0:2], tel[2:6], tel[6:10])
