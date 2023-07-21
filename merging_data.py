# Combinar as DataFrames com base nas colunas em comum
merged_data = pd.merge(dataexpo, idhm, left_on=['UF do Produto','Ano'], right_on=['UF','Ano'])
display(merged_data)
