# ==============================================================================
# SECCIÓN 1: IMPORTACIÓN DE MÓDULOS Y LIBRERÍAS
# ==============================================================================

import sqlite3

# CONCEPTO: 'sqlite3' es un módulo nativo de Python (no requiere 'pip install').
# Otorga un motor de base de datos relacional ligero basado en archivos locales,
# sin necesidad de instalar o configurar un servidor de base de datos independiente.
import pandas as pd

# CONCEPTO: 'pandas' es la librería principal en Python para manipulación y análisis de datos.
# Utiliza estructuras de datos llamadas DataFrames (tablas bidimensionales) que facilitan
# la limpieza, transformación y consulta de información. Se importa convencionalmente como 'pd'.
from bokeh.models import ColumnDataSource

# CONCEPTO: 'bokeh' es una librería para crear visualizaciones interactivas en navegadores web.
# SUBMÓDULO: 'bokeh.models' contiene los objetos de bajo nivel que definen la estructura del gráfico.
# CLASE: 'ColumnDataSource' es el contenedor de datos fundamental de Bokeh. Actúa como puente
# entre las estructuras de datos de Python (como diccionarios o DataFrames) y el renderizado web (JavaScript).
from bokeh.palettes import Category10

# SUBMÓDULO: 'bokeh.palettes' contiene colecciones de paletas de colores predefinidas.
# OBJETO: 'Category10' es una paleta de colores categóricos cualitativos (ideal para diferenciar barras o grupos).
from bokeh.plotting import figure, output_file, show

# SUBMÓDULO: 'bokeh.plotting' es la interfaz de alto nivel de Bokeh para construir gráficos rápidamente.
# FUNCIONES:
# - 'figure': Crea y configura el lienzo principal donde se dibujarán las formas geométricas (líneas, barras, etc.).
# - 'output_file': Define el nombre y la ruta del archivo HTML donde se guardará el gráfico generado.
# - 'show': Abre el archivo HTML en el navegador predeterminado para visualizar la interfaz gráfica.
from bokeh.transform import factor_cmap

# SUBMÓDULO: 'bokeh.transform' proporciona funciones para mapear o transformar datos directamente en propiedades visuales.
# FUNCIÓN: 'factor_cmap' (Factor Color Mapper) asigna colores de una paleta a factores o categorías específicas
# (en este caso, asigna un color distinto a cada mes de forma automática).


# ==============================================================================
# SECCIÓN 2: LÓGICA DE BASE DE DATOS (PERSISTENCIA DE DATOS)
# ==============================================================================


def preparar_base_datos():
    """
    Crea la base de datos local SQLite y llena la tabla 'ventas' con información inicial.

    NOTAS CONCEPTUALES:
    - Conexión: Representa la sesión de trabajo con el archivo físico '.db'.
    - Cursor: Objeto que permite enviar comandos SQL y recorrer los resultados devueltos.
    - Commit: Operación que guarda los cambios de forma permanente en el disco.
    """
    # Establecer conexión con la base de datos (se crea el archivo 'empresa.db' si no existe)
    conexion = sqlite3.connect("empresa.db")
    cursor = conexion.cursor()

    # Creación de la estructura de la tabla mediante DDL (Data Definition Language)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mes TEXT NOT NULL,
            monto INTEGER NOT NULL
        )
    """
    )

    # Verificación de registros para evitar duplicidad de datos al reejecutar el script
    cursor.execute("SELECT COUNT(*) FROM ventas")
    if cursor.fetchone()[0] == 0:
        # Estructura de datos en memoria (Lista de Tuplas)
        datos_iniciales = [
            ("Enero", 1200),
            ("Febrero", 1900),
            ("Marzo", 1500),
            ("Abril", 2400),
            ("Mayo", 2100),
            ("Junio", 2800),
        ]
        # Inserción parametrizada para prevenir vulnerabilidades de Inyección SQL
        cursor.executemany(
            "INSERT INTO ventas (mes, monto) VALUES (?, ?)", datos_iniciales
        )
        conexion.commit()

    # Cierre de conexión para liberar recursos de memoria e hilos en el SO
    conexion.close()


# ==============================================================================
# SECCIÓN 3: PROCESAMIENTO Y VISUALIZACIÓN DE DATOS (DASHBOARD)
# ==============================================================================


def graficar_desde_bd():
    """
    Consulta la base de datos SQLite y genera una gráfica de barras interactiva con Bokeh.

    NOTAS CONCEPTUALES:
    - ETL (Extract, Transform, Load): Extraemos de SQL, transformamos con Pandas y cargamos en Bokeh.
    - ColumnDataSource (CDS): Al vincular el CDS a la figura, cualquier interacción en el gráfico
      puede sincronizarse con los datos origen.
    """
    # --------------------------------------------------------------------------
    # PASO 1: Extracción de datos (SQL a Pandas)
    # --------------------------------------------------------------------------
    conexion = sqlite3.connect("empresa.db")
    # pd.read_sql_query ejecuta la consulta SQL y convierte el resultado en un DataFrame
    df = pd.read_sql_query("SELECT mes, monto FROM ventas", conexion)
    conexion.close()

    # Asegurar el casting explícito de datos a tipo String para el eje categórico
    df["mes"] = df["mes"].astype(str)

    # --------------------------------------------------------------------------
    # PASO 2: Mapeo de datos para Bokeh
    # --------------------------------------------------------------------------
    # Vinculación del DataFrame de Pandas con el conector nativo de Bokeh
    source = ColumnDataSource(data=df)

    # Configuración del documento de salida web
    output_file("reporte_ventas_bd.html")
    meses = list(df["mes"])

    # --------------------------------------------------------------------------
    # PASO 3: Construcción de la figura y elementos visuales
    # --------------------------------------------------------------------------
    fig = figure(
        x_range=meses,  # Define el eje X como categórico pasando la lista de meses
        height=400,  # Altura del lienzo en píxeles
        width=700,  # Ancho del lienzo en píxeles
        title="Reporte de Ventas desde SQLite",  # Título del gráfico
        toolbar_location="above",  # Ubicación de la barra de herramientas interactivas
    )

    # Renderizado de la figura geométrica 'vbar' (Vertical Bars)
    fig.vbar(
        x="mes",  # Columna del ColumnDataSource para el eje X
        top="monto",  # Columna del ColumnDataSource para determinar la altura
        width=0.5,  # Grosor de las barras
        source=source,  # Origen de datos ligado
        line_color="white",  # Borde de las barras
        fill_color=factor_cmap(
            "mes", palette=Category10[6], factors=meses
        ),  # Color por categoría
    )

    # --------------------------------------------------------------------------
    # PASO 4: Estilizado del gráfico
    # --------------------------------------------------------------------------
    fig.y_range.start = 0  # Fuerza a que el eje Y comience estrictamente en 0
    fig.xgrid.grid_line_color = (
        None  # Remueve las líneas de la cuadrícula vertical para mayor claridad
    )
    fig.yaxis.axis_label = "Monto ($)"
    fig.xaxis.axis_label = "Mes"

    # Despliegue en navegador
    show(fig)


# ==============================================================================
# SECCIÓN 4: PUNTO DE ENTRADA PRINCIPAL (MAIN)
# ==============================================================================

if __name__ == "__main__":
    # CONCEPTO: Esta validación asegura que el código solo se ejecute cuando
    # el archivo es llamado directamente, y no cuando es importado como módulo en otro script.
    preparar_base_datos()
    graficar_desde_bd()
