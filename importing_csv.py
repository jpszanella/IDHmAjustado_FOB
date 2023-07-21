#carregar dados exportações
dataexpo=pd.read_excel("expo3.xlsx")
# Visualizar os nomes das colunas separadas
display(dataexpo)
# Datacleaning 
colunas_para_manter=['Ano','UF do Produto','Valor FOB (US$)']
dataexpo=dataexpo[colunas_para_manter]
display(dataexpo)

#carregar dados IDHM
idhm=pd.read_excel("IDHMajustado2012_2021.xlsx")
#limpar colunas em branco
colunas_para_manter = ['UF', 'Range', 'Ano']
idhm = idhm[colunas_para_manter]
display(idhm)
