
import rich
from classes import Aluno, Professor, Funcionario, Pessoa

def main(): 
    a1 = Aluno("jose", 32, "dev",  "5-123")
    a1.fazer_ainiversario()
    a1.fazer_matricula()
    rich.inspect(a1)
        
    p1 = Professor("Cria", 32, "job", "Mestrado")
    p1.fazer_ainiversario()
    p1.dar_aula()
    rich.inspect(p1, methods=True)
        
    f1 = Funcionario("Claudia", 31, "secretaria", "Secretaria")
    f1.fazer_ainiversario()
    f1.bater_ponto()
    rich.inspect(f1, methods=True)

    

if __name__ == "__main__":
    main()