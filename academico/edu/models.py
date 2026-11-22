from django.db import models,IntegrityError
import secrets
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal

# Create your models here.

class Matricula(models.Model):
    matricula = models.IntegerField()
    # nome_aluno = models.CharField(max_length=200)
    aluno = models.ForeignKey('comum.aluno', verbose_name='Aluno', on_delete=models.CASCADE)
    curso = models.ForeignKey('curso', verbose_name='Curso', on_delete=models.CASCADE)
    # curso = models.CharField(max_length=100)
    observacao = models.TextField()
    data_matricula =  models.DateTimeField(verbose_name="Data da matrícula", blank = True, auto_now_add=True)
    
    class Meta:
        verbose_name = "Matrícula do aluno"
        verbose_name_plural = "Matrículas dos alunos"
        ordering = ["id"]
        
def gerar_codigo_curso_10_digitos():
    # Garante sempre exatamente 10 dígitos numéricos (de 1000000000 a 9999999999)
    return str(secrets.randbelow(9_000_000_000) + 1_000_000_000)
    
class Curso(models.Model):
    PERIODICIDADE_CHOICES = [
        [1, 'Anual'],
        [2, 'Semestral'],
        [3, 'Livre'],
    ]
    
    TIPO_HORA_AULA_CHOICES = [
        [45, '45 min'],
        [60, '60 min']
    ]
    
    codigo = models.CharField(verbose_name='Código do curso', help_text='Código usado para composição de turmas e matrículas', unique=True, max_length=10, editable=False)
    
    descricao = models.CharField(verbose_name='Descrição', max_length=500, null=True, blank=True)
    
    ativo = models.BooleanField('Ativo', default=True)
    
    ppc = models.FileField(upload_to='static/', null=True, blank=True, verbose_name='PPC', default=None)
    
    ch_total = models.PositiveIntegerField('Carga horária total do curso', blank=True, null=True, default=None)
    
    tipo_hora_aula = models.PositiveIntegerField('Tipo hora aula', blank=True, null=True, choices=TIPO_HORA_AULA_CHOICES)
    
    periodicidade = models.PositiveIntegerField('Periodicidade', choices=PERIODICIDADE_CHOICES, null=True)
    
    media_aprovacao = models.DecimalField('Média para aprovação', null=True, blank=True, help_text='Valor entre 0 e 10.', decimal_places=2, max_digits=5, validators=[MinValueValidator(Decimal(0)), MaxValueValidator(Decimal(10))])
    
    conteudo = models.TextField(verbose_name='Conteúdo')

    class Meta:    
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ('id', 'ativo',)
        
    def _gerar_codigo_unico(self):
        while True:
            novo_codigo = gerar_codigo_curso_10_digitos()
            if not Curso.objects.filter(codigo=novo_codigo).exists():
                return novo_codigo

    def save(self, *args, **kwargs):
        # Gera apenas na criação (quando ainda não tem pk e código vazio)
        if self._state.adding and not self.codigo:
            for _ in range(10):
                self.codigo = self._gerar_codigo_unico()
                try:
                    return super().save(*args, **kwargs)
                except IntegrityError:
                    # Caso extremo de colisão simultânea entre duas requisições
                    self.codigo = ''
            raise IntegrityError('Não foi possível gerar um código único para o curso.')

        return super().save(*args, **kwargs)

    def __str__(self):
        codigo = self.codigo.replace('-','')
        
        return '{} - {}'.format(self.descricao, codigo)
    
    