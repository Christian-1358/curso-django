
import sqlite3

busca = input("Quem você está procurando? ").strip()

try:
    with sqlite3.connect("meubanco.db") as banco:
        banco.row_factory = sqlite3.Row
        cursor = banco.cursor()

        cursor.execute(
            "SELECT * FROM User WHERE nome LIKE ?",
            (f"%{busca}%",)
        )

        amigos = cursor.fetchall()

        if amigos:
            for amigo in amigos:
                print(f"{amigo['nome']} idade {amigo['idade']}")

            print(f"Ao todo encontrei {len(amigos)} amigos com '{busca}'.")
        else:
            print(f"ERRO: Nenhum usuário encontrado com '{busca}'.")

except sqlite3.Error as erro:
    print(f"Falha no banco de dados: {erro}")

except Exception as erro:
    print(f"Algo deu errado: {erro}")
