# Feedfoward *from scratch*
![Alt text](./assets/feedfoward.png "a graph")

Implementación de un modelo feedfoward para clasificación no lineal. En este caso, se utilizó la red como compuerta xor.


### Función de costo y algoritmo de optimización
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
- Carga el notebook en google colab.

- Si necesitas ejecutarlo localmente, debes tener instalado los siguientes módulos:
```
pip install pandas matplotlib numpy scikit-learn seaborn jupyter
```
### Dataset y preprocesamiento de datos

Para la clasificación, se genera un dataset propio con varias muestras.
