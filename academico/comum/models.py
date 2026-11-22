from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal

# Create your models here.

class Aluno(models.Model):
    
    sexo_opcoes = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Outro', 'Outro'),
    )
    
    # nome = models.CharField(verbose_name='Nomes', max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(verbose_name='E-mail', max_length=200)
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', null=True)
    sexo = models.CharField(choices=sexo_opcoes, max_length=30, null=True)
    telefone = models.CharField(verbose_name='Telefone', max_length=15, null=True)
    
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ('user__first_name', )
        
    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)
    
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
        
        codigo = models.CharField(verbose_name='Código do curso', help_text='Código usado para composição de turmas e matrículas', unique=True, max_length=10)
        
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
    
        def __str__(self):
            codigo = self.codigo.replace('-','')
            
            return '{} - {}'.format(codigo, self.descricao)
        
        