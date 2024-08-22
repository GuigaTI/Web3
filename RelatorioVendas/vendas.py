def lerDados(arquivo):
    vendas = []
    
    with open(arquivo,'r',encoding='utf-8') as arquivos:
        venda = arquivos.readlines()
        for linha in venda:
            linha = linha.strip()
            campos = linha.split(',')
            if len(campos) != 4:
                print(f"Formato inválido na linha: {linha}")
                continue
            data,produto,quantidade,valor = campos
            quantidade = int(quantidade)
            valorUnidade = float(valor)
            vendas.append((data,produto,quantidade,valorUnidade))
    return vendas

def calcular_totais(vendas):
    total_por_produto = {}
    total_por_dia = {}
    total_geral = 0.0

    for data,produto,quantidade,valorUnidade in vendas:
        total_venda = quantidade * valorUnidade
        if produto in total_por_produto:
            total_por_produto[produto] += total_venda
        else:
            total_por_produto[produto] = total_venda
        if data in total_por_dia:
            total_por_dia[data] += total_venda
        else:
            total_por_dia[data] = total_venda
        total_geral += total_venda
    
    return total_por_produto,total_por_dia,total_geral

def relatorio(total_por_produto,total_por_dia,total_geral):
    relatorio = []

    relatorio.append("Relatório de Vendas")
    relatorio.append("--------------------")
    
    relatorio.append("\nTotal de Vendas por Produto:")
    for produto, total in total_por_produto.items():
        relatorio.append(f"{produto}: R$ {total:.2f}")
    
    relatorio.append("\nTotal de Vendas por Dia:")
    for data, total in total_por_dia.items():
        relatorio.append(f"{data}: R$ {total:.2f}")
    
    relatorio.append(f"\nTotal Geral de Vendas: R$ {total_geral:.2f}")
    
    "\n".join(relatorio)

    with open("relatorio.txt",'a',encoding='utf-8') as arquivos:
        for item in relatorio:
            arquivos.write(f'\n{item}')

def main():

    arquivo = 'vendas.txt'
    vendas = lerDados(arquivo)
    totalProduto,totalDia,totalGeral = calcular_totais(vendas)
    relatorio(totalProduto,totalDia,totalGeral)    
    with open('relatorio.txt','r',encoding='utf-8') as arquivo:
        print(arquivo.read())
if __name__ == "__main__":
    main()


