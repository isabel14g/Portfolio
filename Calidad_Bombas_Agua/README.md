# 💧 Predicción de Funcionamiento de Bombas de Agua – Machine Learning

## 📌 Descripción general
Este proyecto aplica modelos de Machine Learning para predecir si una bomba de agua está:
- **Funcional**
- **Funcional pero con reparación necesaria**
- **No funcional**

Se trata de un problema real de clasificación utilizado en competiciones como *Kaggle – Pump it Up: Data Mining the Water Table*. El objetivo es ayudar a priorizar reparaciones y optimizar recursos públicos en zonas rurales.

---

## 🗂️ Estructura del proyecto
Calidad_Bombas_Agua/
│── Data/ # Dataset original
│── 1_Tarea_Machine_Learning_Isabel_Giraldo.ipynb
│── 2_final_submit.csv # Resultado de predicciones
│── README.md # Este archivo
│── .gitignore #

---

## 📊 Análisis y resultados

### ✅ Modelo utilizado
- **Random Forest Classifier (sklearn)**
- Pruebas con modelo normal y modelo con `class_weight='balanced'` para tratar el desbalance de clases.

### ✅ Métricas principales (modelo sin balancear)
| Clase                         | Precisión | Recall | F1-score |
|------------------------------|-----------|--------|----------|
| **Funcional**                | ~0.81     | ~0.88  | ~0.85    |
| **Funcional con reparación** | ~0.57     | ~0.35  | ~0.44    |
| **No funcional**             | ~0.83     | ~0.84  | ~0.84    |
| **Accuracy total**           | **0.80**  |        |          |

### ✅ Modelo con `class_weight='balanced'`
- Accuracy ≈ 0.80  
- Mejora leve en Recall de clases minoritarias  
- Mejor equilibrio en predicción de "funcional con reparación"

---

## 🛠️ Librerías utilizadas
| Librería        | Uso |
|-----------------|-----|
| Pandas / NumPy  | Limpieza y manipulación de datos |
| Matplotlib / Seaborn | Gráficos y visualización |
| Scikit-learn     | Modelado (RandomForest, train_test_split, metrics) |
| Jupyter Notebook | Desarrollo del proyecto |

---

## ✨ Autora
**Isabel Giraldo Álvarez**  
📧 Email: isabelgiraldoal@gmail.com  
🔗 GitHub: https://github.com/isabel14g
