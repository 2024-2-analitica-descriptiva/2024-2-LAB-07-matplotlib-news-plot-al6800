"""
Escriba el código que ejecute la acción solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la gráfica final está ubicado en la raíz de
    este repositorio.

    El gráfico debe salvarse al archivo `files/plots/news.png`.
    """
    # Ruta del archivo CSV
    ruta_archivo = 'files/input/news.csv'

    # Crear la carpeta `files/plots` si no existe
    ruta_salida = "files/plots/news.png"
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)

    # Crear la figura del gráfico
    plt.figure(figsize=(10, 6))

    # Configuración de colores, orden y grosor de línea
    colors = {"Television": "dimgray", "Newspaper": "grey", "Internet": "tab:blue", "Radio": "lightgrey"}
    zorder = {"Television": 1, "Newspaper": 1, "Internet": 2, "Radio": 1}
    linewidths = {"Television": 2, "Newspaper": 2, "Internet": 4, "Radio": 2}

    # Leer el archivo CSV
    df = pd.read_csv(ruta_archivo, index_col=0)

    # Graficar cada columna con su configuración
    for col in df.columns:
        plt.plot(df[col], color=colors[col], label=col, zorder=zorder[col], linewidth=linewidths[col])

        # Agregar anotaciones en los datos iniciales
        first_year = df.index[0]
        plt.scatter(x=first_year, y=df[col][first_year], color=colors[col], zorder=zorder[col])
        plt.text(
            first_year - 0.2,
            df[col][first_year],
            col + " " + str(df[col][first_year]) + "%",
            ha="right",
            va="center",
            color=colors[col],
        )

        # Agregar anotaciones en los datos finales
        last_year = df.index[-1]
        plt.scatter(x=last_year, y=df[col][last_year], color=colors[col], zorder=zorder[col])
        plt.text(
            last_year + 0.2,
            df[col][last_year],
            str(df[col][last_year]) + "%",
            ha="left",
            va="center",
            color=colors[col],
        )

    # Ajustes de diseño
    plt.title("How people get their news", fontsize=16)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    # Guardar la gráfica
    plt.savefig(ruta_salida)
    print(f"Gráfica guardada en: {ruta_salida}")

    # # Mostrar la gráfica
    # plt.show()

# Llamar a la función
pregunta_01()
