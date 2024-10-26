import csv

def processar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    dados = []
    for linha in linhas:
        linha = linha.strip()
        tipo_registro = linha[:2]

        if tipo_registro == "00":
            registro = {
                "tipo_registro": linha[:2],
                "nome_arquivo": linha[2:15].strip(),
                "codigo_origem": linha[15:23].strip(),
                "data_geracao": linha[23:31].strip(),
                "reserva": linha[31:].strip()
            }

        elif tipo_registro == "01":
            registro = {
                "tipo_registro": linha[:2],
                "data_pregao": linha[2:10].strip(),
                "cod_bdi": linha[10:12].strip(),
                "cod_neg": linha[12:24].strip(),
                "tp_merc": linha[24:27].strip(),
                "nom_res": linha[27:39].strip(),
                "espec": linha[39:49].strip(),
                "prazot": linha[49:52].strip(),
                "modref": linha[52:56].strip(),
                "preabe": formatar_numero(linha[56:69].strip()),
                "premax": formatar_numero(linha[69:82].strip()),
                "premin": formatar_numero(linha[82:95].strip()),
                "premed": formatar_numero(linha[95:108].strip()),
                "preult": formatar_numero(linha[108:121].strip()),
                "preofc": formatar_numero(linha[121:134].strip()),
                "preofv": formatar_numero(linha[134:147].strip()),
                "totneg": linha[147:152].strip(),
                "quatot": linha[152:170].strip(),
                "voltot": formatar_numero(linha[170:188].strip()),
                "preexe": formatar_numero(linha[188:201].strip()),
                "indopc": linha[201:202].strip(),
                "datven": linha[202:210].strip(),
                "fatcot": linha[210:217].strip(),
                "proexe": linha[217:230].strip(),
                "codisi": linha[230:242].strip(),
                "desmes": linha[242:245].strip(),
            }

        elif tipo_registro=="99":
            registro = {
                "tipo_registro": linha[:2],
                "reserva": linha[2:].strip(),
            }

        else:
            continue

        dados.append(registro)    

    return dados

def formatar_numero(numero_str):
    if not numero_str:
        return ""
    
    try:
        numero = float(f"{numero_str[:2]}.{numero_str[-2:]}")
        return f"{numero:,.2f}".replace('.',',')
    except ValueError:
        return ""
    
def salvar_em_csv(dados, nome_arqivo_csv):
    if not dados:
        print("Nenhum dado encontrado")
        return
    
    campos = set()
    for registro in dados:
        campos.update(registro.keys())

    campos = sorted(campos)

    with open(nome_arqivo_csv, 'w', newline = '', encoding = 'utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = campos, delimiter = ";", lineterminator = '\n')
        writer.writeheader()
        writer.writerows(dados)

# nome_arquivo_txt= "C:\\Users\\vitor\\Downloads\\COTAHIST_D11102024\\COTAHIST_D11102024.TXT"
nome_arquivo_txt= "C:\\Users\\vitor\\Downloads\\COTAHIST_D18102024\\COTAHIST_D18102024.TXT"
dados = processar_arquivo(nome_arquivo_txt)

# nome_arquivo_csv = "D:\\CEDERJ\\2024.2\\tcc\\IVOptionPredictor\\projeto\\data\\b3data_2024.10.11.csv"
nome_arquivo_csv = "D:\\CEDERJ\\2024.2\\tcc\\IVOptionPredictor\\projeto\\data\\b3data_2024.10.18.csv"
salvar_em_csv(dados, nome_arquivo_csv)

print("dados salvos")
