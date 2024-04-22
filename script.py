# Analisis de Datos
import pandas as pd
# Deteccion de codificación del archivo
import chardet

# ----- Carga de archivo ----- #

#Detectando codificacíon del archivo
with open('Capacity-02.csv', 'rb') as archivo:
    result = chardet.detect(archivo.read())

print(result['encoding'])

# Columnas en las que nos debemos enfocar para obtener un catalogo de proyectos
selec_columnas = ['Nombre', 'Proyecto(s)', 'Tipo Requerimiento']

# Carga archivo CSV con un DataFrame
dataF = pd.read_csv('C:\\Users\\bc.jnevarez\\Codigo\\Capacity-02.csv', index_col=0, encoding='latin-1', usecols=selec_columnas)

# ----- Limpieza de datos ----- #

# Eliminar columnas completamente vacías
dataF_limpio = dataF.dropna(axis=1, how="all")

# Eliminar filas con valores nulos en cualquier columna
dataF_limpio = dataF.dropna()

# Carga datos limpios a un archivo
dataF_limpio.to_csv("Capacity-03(clean).csv", index=False)

# ----- Analisis de datos ----- #

# Agrupa por nombre y cuenta las aparaciciones
projects = dataF_limpio.groupby("Nombre").count()

# Carga el resultado en un archivo
projects.to_csv("Asignación de proyectos.csv")

# Selecciona la columna con los nombres de proyectos
#col_proyectos = dataF_limpio['Proyecto(s)']

# Obtener una lista de nombres unicos
#nombres_proyectos = col_proyectos.unique().tolist()

# Creando un catálogo de proyectos
catalogo_proyectos = dataF_limpio['Proyecto(s)'].drop_duplicates()

# Guardar el catalogo en un archivo .csv
catalogo_proyectos.to_csv('Catalogo Proyectos.csv', index=False)

# Buscar ocurrencias de un proyecto

busca_proyecto = input("Inserta el nombre del proyecto que buscas: ")

filtro = dataF_limpio['Tipo Requerimiento'].str.contains(busca_proyecto, case=False)

print(filtro)

p_encontrados = dataF_limpio.loc[filtro, 'Proyecto(s)'].tolist()

#print(p_encontrados)
print('Proyectos relacionados a ' + busca_proyecto)
for p in p_encontrados:
    print(p)
