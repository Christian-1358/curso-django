class Churrasco:
    def __init__(self, pessoas, carne_por_pessoa_kg=0.4, preco_kg=50.0):
        self.pessoas = pessoas
        self.carne_por_pessoa_kg = carne_por_pessoa_kg
        self.preco_kg = preco_kg
        
    def calcular_carne(self):
        return self.pessoas * self.carne_por_pessoa_kg
    
    def calcular_custo(self):
        return self.calcular_carne() * self.preco_kg
    
    def calcular_precopor_pessoa(self):
        if self.pessoas == 0:
            return 0
        else:
            
            return self.calcular_custo() / self.pessoas
        
    def exitbir_relatorios(self):
        total_carne = self.calcular_carne()
        custo_total = self.calcular_custo()
        preso_pessoa = self.calcular_precopor_pessoa()
        
        print(f"--- Relatório do Churrasco ---")
        print(f"Participantes: {self.pessoas} pessoas")
        print(f"Quantidade de carne necessária: {total_carne:.2f} kg")
        print(f"Custo total do churrasco: R$ {custo_total:.2f}")
        print(f"Preço por pessoa: R$ {preso_pessoa:.2f}")
        
meu_churrasco = Churrasco(pessoas=3)
meu_churrasco.exitbir_relatorios()