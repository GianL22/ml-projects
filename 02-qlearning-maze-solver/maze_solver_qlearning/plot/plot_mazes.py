import numpy as np
import matplotlib as plt


def plot_mazes(mazes : np.ndarray, plot_shape = 7):
    n_subplots = mazes.shape[0]
    
    plt.figure(figsize=(plot_shape,plot_shape)) # La imagen del conjunto de ropas se hace mas grande

    for i, maze in enumerate(mazes):
        # image = image.numpy().reshape((28,28))
        # se dibuja la primera figura
        plt.subplot(5,5,i+1) # creamos subplots para cada ropa
        plt.xticks([]) # Esto hace que quite los valores de los ejes, mas limpio
        plt.yticks([])
        plt.grid(False)
        # TODO Mostrar inicio y fin con otros colores
        plt.imshow(maze, cmap=plt.cm.binary)
        
    plt.show() # no es necesaria