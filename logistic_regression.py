#Definir as variáveis independentes (features) e a variável dependente (target)
X = merged_data[['Valor FOB (US$)', 'Ano']]
y = merged_data['Range']

# Dividir os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instanciar o modelo de regressão logística
logreg = LogisticRegression()

# Treinar o modelo usando os dados de treinamento
logreg.fit(X_train, y_train)

# Fazer previsões usando os dados de teste
y_pred = logreg.predict(X_test)

# Avaliar o desempenho do modelo -> stablish realtion between prediction and accuracy 
print(classification_report(y_test, y_pred))
