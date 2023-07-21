import sys
!{sys.executable} -m pip install mlxtend
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions

# Definir as variáveis independentes (features) e a variável dependente (target)
X = merged_data[['Valor FOB (US$)', 'Ano']].values
y = merged_data['Range'].values

# Instanciar o modelo de regressão logística
logreg = LogisticRegression()

# Treinar o modelo
logreg.fit(X, y)

# Plotar a regressão logística
plot_decision_regions(X, y, clf=logreg)

# Definir os limites dos eixos X e Y
plt.xlim(X[:, 0].min() - 2.0, X[:, 0].max() + 2.0)
plt.ylim(X[:, 1].min() - 2.0, X[:, 1].max() + 2.0)

# Adicionar rótulos aos eixos X e Y
plt.xlabel('Valor FOB (US$)')
plt.ylabel('Ano')

# Mostrar o gráfico
plt.show(logreg)
