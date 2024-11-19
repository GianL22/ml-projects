# Kernel Ridge Regression *from scratch* para la predicción de manchas solares

Implementación de regresion polinomial con regularización L2 usando el truco de kernel. El modelo fue entrenado con el número de manchas solares anuales, mensuales y diarias. Para este último caso se implementó el algoritmo de descenso de gradiente con el truco de kernel.

La función kernel utilizada fue la polinomial

$$
K(X, Y) = (\gamma \langle X, Y \rangle + \text{coef0})^{\text{d}}
$$

En este caso, se dejó el parámetro del coeficinete por defecto. En el caso del parámetro del grado de la dimensión, permite que las predicciones se ajusten mejor al comportamiento de la grafica, pero al ser muy alto, puede traer sobreajuste.

### Descenso de gradiente
Fue utilizado el **error cuadrático medio** como **función de costo** 
$$
MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

se escogió el algoritmo de **descenso de gradiente** para la optimización. 

$$
\frac{\partial E}{\partial w_{ij}} = \frac{\partial E}{\partial \hat{y}} \frac{\partial \hat{y}}{\partial z_i} \frac{\partial z_i}{\partial w_{ij}}
$$

$$
w_{ij}^{nueva} = w_{ij}^{antigua} - \alpha \frac{\partial E}{\partial w_{ij}}
$$
### Cómo ejecutarlo
- Carga el notebook en google colab y [descarga el dataset](https://www.sidc.be/SILSO/datafiles)

- Si necesitas ejecutarlo localmente, debes tener instalado los siguientes módulos:
```
pip install pandas matplotlib numpy scikit-learn jupyter
```
### Dataset y preprocesamiento de datos
Se trata de un dataset con tipos de datos secuenciales en donde la predicción depende de N datos previos. Para este caso, se escogió el número de manchas solares anterior para predecir el siguiente.

El [dataset](https://www.sidc.be/SILSO/datafiles) fue normalizado y se eliminaron los registros sin observaciones. 
