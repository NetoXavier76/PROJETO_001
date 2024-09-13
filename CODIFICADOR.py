import hashlib

def criar_hash(arquivo, algoritmo):
    try:
        with open(arquivo, 'rb') as file:
            conteudo = file.read()

        if algoritmo.lower() == 'md5':
            hash_obj = hashlib.md5()
        elif algoritmo.lower() == 'sha1':
            hash_obj = hashlib.sha1()
        elif algoritmo.lower() == 'sha256':
            hash_obj = hashlib.sha256()
        elif algoritmo.lower() == 'sha512':
            hash_obj = hashlib.sha512()
        else:
            return None

        hash_obj.update(conteudo)
        return hash_obj.hexdigest()

    except Exception as e:
        return f"ERROR! {e}"

def mostrar_conteudo_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as f:
            conteudo = f.read()
            print("TEXTO DESCRIPTOGRAFADO:")
            print(conteudo)
    except FileNotFoundError:
        print(f"ARQUIVO {arquivo} NÃO EXISTE.")
    except Exception as e:
        print(f"ERROR!: {e}")

nome_arquivo = "text.txt"

while True:
    algoritmo_escolhido = input(
        "DIGITE O ALGORITMO HASH QUE QUER UTILIZAR (MD5, SHA1, SHA256, SHA512): ")
    resultado_hash = criar_hash(nome_arquivo, algoritmo_escolhido)

    if resultado_hash:
        print(f'O TEXTO FOI CODIFICADO EM HASH {
              algoritmo_escolhido.upper()}: {resultado_hash}')

        resposta = input(
            "GOSTARIA DE SABER O TEXTO DESCRIPTOGRAFADO? (SIM/NÃO): ").strip().lower()
        if resposta in ['sim', 's', 'ism', 'yes']:
            mostrar_conteudo_arquivo(nome_arquivo)
        else:
            print("ENCERRANDO...")
        break
    else:
        print("POR FAVOR, ESCOLHA NOVAMENTE ENTRE AS OPÇÕES: (MD5, SHA1, SHA256, SHA512).")
