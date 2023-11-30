# Sistema Simples de Controle de Notas e Falta
import os

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = []
        self.faltas = []

    def add_nota(self, nota, disciplina):
        self.notas.append((nota, disciplina))

    def add_falta(self, falta):
        self.faltas.append(falta)

    def calcula_media(self):
        soma = 0
        for nota, disciplina in self.notas:
            soma += nota
        return soma / len(self.notas)

    def aprovado(self):
        return self.calcula_media() >= 7.0

class SistemaGestaoAlunos:
    def __init__(self):
        self.alunos = []

    def cadastra_aluno(self, nome, matricula, curso):
        aluno = Aluno(nome, matricula, curso)
        self.alunos.append(aluno)

    def registra_nota(self, matricula, nota, disciplina):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                aluno.add_nota(nota, disciplina)
                break

    def registra_falta(self, matricula, falta):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                aluno.add_falta(falta)
                break

    def calcula_medias(self):
        for aluno in self.alunos:
            aluno.calcula_media()

    def verifica_aprovacao(self):
        for aluno in self.alunos:
            aluno.aprovado()

    def gera_relatorio(self):
        relatorio = ""
        for aluno in self.alunos:
            relatorio += "Aluno: " + aluno.nome + "\n"
            relatorio += "Matrícula: " + aluno.matricula + "\n"
            relatorio += "Curso: " + aluno.curso + "\n"
            relatorio += "Notas:\n"
            for nota, disciplina in aluno.notas:
                relatorio += "  " + str(nota) + " - " + disciplina + "\n"
            relatorio += "Faltas: " + str(aluno.faltas) + "\n"
            relatorio += "Aprovado: " + str(aluno.aprovado()) + "\n\n"
        return relatorio

sistema = SistemaGestaoAlunos()
sistema.cadastra_aluno("João da Silva", "1234567890", "Engenharia de Software")
sistema.cadastra_aluno("Maria da Costa", "9876543210", "Administração")
sistema.registra_nota("1234567890", 8.0, "Programação")
sistema.registra_nota("1234567890", 9.0, "Matemática")
sistema.registra_nota("9876543210", 7.0, "Economia")
sistema.registra_nota("9876543210", 8.0, "Contabilidade")
sistema.registra_falta("1234567890", 2)
sistema.registra_falta("9876543210", 1)
sistema.calcula_medias()
sistema.verifica_aprovacao()
relatorio = sistema.gera_relatorio()
print(relatorio)