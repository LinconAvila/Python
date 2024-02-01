class Disciplina:
    def __init__(self, nota_trabalho, nota_prova):
        self.nota_trabalho = nota_trabalho
        self.nota_prova = nota_prova

    def calcular_nota_final(self):
        nota_final = self.nota_trabalho * 0.25 + self.nota_prova * 0.75
        if nota_final < 7.0:
            print("Está em exame.")
        else:
            print(f"Aprovado com a nota {nota_final:.1f}")

nota_trabalho = float(input("Digite a nota do trabalho (0 a 10): "))
nota_prova = float(input("Digite a nota da prova (0 a 10): "))

disciplina = Disciplina(nota_trabalho, nota_prova)
disciplina.calcular_nota_final()

        

    