import rich


class Temp:
        def __init__(self,temp = 20.0, minimo = 16, max = 30, ):
            self.minimo = minimo
            self.max = max
            self._temp = temp
        @property
        def temp(self):
            return self._temp
                

        @temp.setter
        def temp(self, novo_valor):
            if novo_valor < self.minimo:
                raise ValueError(f"ERRO: A temperatura mínima é de {self.minimo}°C!")
            if novo_valor > self.maximo:
                raise ValueError(f"ERRO: O ar suporta até {self.maximo}°C!")
            self._temp = novo_valor

        def incremetacao(self):
            self.temp += 0.5 
        def descrementar(self):
            self.temp -= 0.5
try:
    rich.print("[red]Digite '0' para sair (ou uma temperatura válida)[/red]")
    escolha_temp = float(input("Digite a temperatura do termostato: "))

    if escolha_temp != 0:
        termostato = Temp(escolha_temp)
        print(f"Temperatura configurada com sucesso: {termostato.temp}°C")
    else:
        print("Saindo...")

except ValueError as e:
    print(e)