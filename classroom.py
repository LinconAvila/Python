class Turma:
    def __init__(self):
        self.matriculas = []
        self.notas = []

    def leitura_dados(self, quantidade_alunos):
        for i in range(quantidade_alunos):
            matricula = input(f"Digite a matrícula do aluno {i + 1}: ")
            nota = float(input(f"Digite a nota do aluno {i + 1}: "))
            self.matriculas.append(matricula)
            self.notas.append(nota)

    def cadastrar_alunos_preexistentes(self, matriculas_preexistentes, notas_preexistentes):
        self.matriculas.extend(matriculas_preexistentes)
        self.notas.extend(notas_preexistentes)

    def calcular_media(self):
        total_notas = sum(self.notas)
        quantidade_alunos = len(self.notas)
        if quantidade_alunos > 0:
            return total_notas / quantidade_alunos
        else:
            return 0

    def mostrar_abaixo_da_media(self, media):
        print("Alunos com nota abaixo da média:")
        for i in range(len(self.matriculas)):
            if self.notas[i] < media:
                print(f"Matrícula: {self.matriculas[i]}")

    def verificar_e_editar_nota(self):
        matricula_aluno = input("Digite a matrícula do aluno para verificar/editar a nota: ")
        index = self.matriculas.index(matricula_aluno) if matricula_aluno in self.matriculas else -1

        if index != -1:
            print(f"Nota atual do aluno {matricula_aluno}: {self.notas[index]}")
            nova_nota = float(input("Digite a nova nota: "))
            self.notas[index] = nova_nota
            print(f"Nota do aluno {matricula_aluno} atualizada para: {nova_nota}")
        else:
            print("Matrícula não encontrada.")

if __name__ == "__main__":
    turma = Turma()

    # Adicionar os 30 alunos pré-existentes
    matriculas_preexistentes = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010',
                                '011', '012', '013', '014', '015', '016', '017', '018', '019', '020',
                                '021', '022', '023', '024', '025', '026', '027', '028', '029', '030']

    notas_preexistentes = [8.5, 7.2, 6.9, 9.0, 5.5, 6.8, 7.5, 8.0, 6.0, 7.7,
                           6.5, 7.8, 9.5, 5.0, 8.3, 7.1, 6.7, 8.9, 7.4, 6.2,
                           7.3, 8.2, 9.2, 6.6, 7.9, 6.4, 7.6, 8.1, 6.3, 7.0]

    turma.cadastrar_alunos_preexistentes(matriculas_preexistentes, notas_preexistentes)

    quantidade_alunos = int(input("Digite a quantidade de alunos adicionais na turma: "))
    turma.leitura_dados(quantidade_alunos)

    media = turma.calcular_media()
    print(f"Média aritmética das notas: {media}")

    turma.mostrar_abaixo_da_media(media)

    opcao = input("Deseja verificar/editar a nota de algum aluno pré-existente? (S/N): ")
    if opcao.upper() == "S":
        turma.verificar_e_editar_nota()

   
