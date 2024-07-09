# *Título: Python y los Esquemas ETL: El Pivote Esencial para la Inteligencia Artificial*

## *© Python México 2024*

[Conceptos básicos](batch-release-etl/docs/index.md)


## **Requerimientos para la demo**

[![pypi](https://pypi.org/static/images/logo-small.8998e9d1.svg)](https://pypi.org)
| | |
| --- | --- |
| Pandas | [![Pandas Latest Release](https://img.shields.io/pypi/v/pandas.svg)](https://pypi.org/project/pandas/) [![PyPI Downloads](https://img.shields.io/pypi/dm/pandas.svg?label=PyPI%20downloads)](https://pypi.org/project/pandas/) [![Conda Latest Release](https://anaconda.org/conda-forge/pandas/badges/version.svg)](https://anaconda.org/conda-forge/pandas) [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/pandas.svg?label=Conda%20downloads)](https://anaconda.org/conda-forge/pandas) |
| numpy | [![Numpy Latest Release](https://img.shields.io/pypi/v/numpy.svg)](https://pypi.org/project/numpy/) [![PyPI Downloads](https://img.shields.io/pypi/dm/numpy.svg?label=PyPI%20downloads)](https://pypi.org/project/numpy/) [![Conda Latest Release](https://anaconda.org/conda-forge/numpy/badges/version.svg)](https://anaconda.org/conda-forge/numpy) [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/numpy.svg?label=Conda%20downloads)](https://anaconda.org/conda-forge/numpy) |
| Requests | [![Requests Latest Release](https://img.shields.io/pypi/v/requests.svg)](https://pypi.org/project/requests/) [![PyPI Downloads](https://img.shields.io/pypi/dm/requests.svg?label=PyPI%20downloads)](https://pypi.org/project/requests/) [![Conda Latest Release](https://anaconda.org/conda-forge/requests/badges/version.svg)](https://anaconda.org/conda-forge/requests) [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/requests.svg?label=Conda%20downloads)](https://anaconda.org/conda-forge/requests) |

## **Descripción**

Quiza todos hemos concentrado la mirada en la Inteligencia Artificial (IA), preocupados por temas como Machine Learning, Deep Learning o IA generative pero estos modelos dependen en gran medida de datos de alta calidad y grandes volúmenes de datos. Los datos pueden provenir de diversas fuentes e aqui donde entran en juego los esquemas ETL.

Sí, es entonces un proceso ETL (Extracción, Transformación y Carga) vital para la Inteligencia Artificial (IA) cuales son las razones. A continuación, te explico cómo y por qué:

### **Extracción (E)**

- **Obtención de Datos**: Los modelos de IA y Machine Learning (ML) dependen en gran medida de datos de alta calidad y grandes volúmenes de datos. Los datos pueden provenir de diversas fuentes como bases de datos, archivos, APIs, sensores IoT, redes sociales, etc. La fase de extracción se encarga de recoger estos datos de las múltiples fuentes.
- **Variedad de Datos**: En IA, es común trabajar con datos estructurados (bases de datos relacionales), semi-estructurados (XML, JSON) y no estructurados (texto, imágenes, audio). La extracción debe ser capaz de manejar esta variedad de datos.

### **Transformación (T)**

- **Limpieza de Datos**: Los datos crudos a menudo contienen errores, duplicados o valores faltantes. La transformación incluye la limpieza de datos, lo que mejora la calidad de los datos y, en consecuencia, la precisión de los modelos de IA.
- **Normalización y Formateo**: Los datos provenientes de diferentes fuentes pueden tener diferentes formatos y escalas. La transformación normaliza estos datos para asegurar que sean consistentes y adecuados para el análisis.
- **Enriquecimiento de Datos**: A veces, los datos extraídos necesitan ser enriquecidos con información adicional, como datos geográficos o demográficos, para proporcionar contexto adicional útil para el modelo de IA.
- **Feature Engineering**: En IA, es crucial transformar los datos crudos en características que los modelos puedan entender y usar efectivamente. Este proceso incluye técnicas como la creación de nuevas variables a partir de las existentes, transformación de variables categóricas a numéricas, etc.

### **Carga (L)**

- **Almacenamiento Eficiente**: Los datos transformados deben ser almacenados en un sistema accesible y eficiente, como un data warehouse, data lake, o bases de datos NoSQL. Esto permite que los datos estén disponibles para el entrenamiento y la inferencia de los modelos de IA.
- **Escalabilidad**: Los sistemas de almacenamiento deben ser escalables para manejar grandes volúmenes de datos y permitir consultas rápidas y eficientes.

### **Importancia para la IA**

- **Calidad de Datos**: Los modelos de IA son tan buenos como la calidad de los datos en los que se entrenan. Un proceso ETL bien diseñado asegura que los datos sean precisos, limpios y relevantes.
- **Preprocesamiento**: El ETL se encarga de la mayor parte del preprocesamiento de datos, una etapa crítica en cualquier proyecto de IA.
- **Automatización y Eficiencia**: Los procesos ETL pueden ser automatizados, lo que permite un flujo constante y eficiente de datos para entrenar y actualizar los modelos de IA.

El proceso ETL es fundamental para la IA porque asegura que los datos necesarios estén disponibles, sean de alta calidad y estén en el formato correcto. Sin un proceso ETL robusto, la creación, entrenamiento y despliegue de modelos de IA sería mucho más complicado y menos eficiente. Por lo tanto, ETL es una pieza clave en el pipeline de datos que impulsa la Inteligencia Artificial.

## ¿Cuales son los lenguajes de programacion usados para el desarrollo de ETL?

Para el desarrollo de procesos ETL (Extracción, Transformación y Carga), se utilizan diversos lenguajes de programación y herramientas. Los lenguajes más comúnmente utilizados son:

### **Python**

- **Popularidad**: Python es uno de los lenguajes más populares para ETL debido a su simplicidad, versatilidad y la gran cantidad de bibliotecas y frameworks disponibles.
- **Bibliotecas**: Pandas, NumPy, SQLAlchemy, PySpark, Dask.
- **Frameworks**: Apache Airflow, Luigi, Kedro, Bonobo.

### **SQL**

- **Uso**: SQL es fundamental en ETL para la manipulación de datos almacenados en bases de datos relacionales. Se utiliza para la extracción de datos, transformación (a través de consultas y procedimientos almacenados) y carga en sistemas de destino.
- **Variantes**: Transact-SQL (T-SQL), PL/SQL, MySQL, PostgreSQL.

### **Java**

- **Popularidad**: Java es ampliamente utilizado en ETL por su robustez y escalabilidad, especialmente en entornos empresariales.
- **Frameworks y Herramientas**: Apache NiFi, Talend, Apache Hop, Spring Batch.

### **Scala**

- **Uso en Big Data**: Scala es el lenguaje principal para Apache Spark, una herramienta de procesamiento de datos a gran escala.
- **Popularidad**: Utilizado en ambientes donde el procesamiento de grandes volúmenes de datos es crítico.

### **R**

- **Análisis y Estadísticas**: R es utilizado principalmente para análisis de datos y transformación debido a su potente conjunto de bibliotecas estadísticas.
- **Bibliotecas**: dplyr, data.table, tidyverse.

### **Shell Scripting (Bash, PowerShell)**

- **Automatización**: Se utiliza para la automatización de tareas ETL en sistemas operativos Unix/Linux y Windows.
- **Uso**: Ideal para la integración de diferentes herramientas y el movimiento de archivos.

### **C#**

- **Uso Empresarial**: C# se utiliza en entornos empresariales, especialmente con herramientas de Microsoft como SQL Server Integration Services (SSIS).
- **Herramientas**: SSIS, Azure Data Factory.

### **Go**

- **Eficiencia y Rendimiento**: Go es utilizado por su rendimiento y eficiencia, especialmente en la creación de pipelines ETL distribuidos.
- **Herramientas**: Pachyderm.

### **Herramientas y Plataformas de ETL**

Además de los lenguajes de programación, existen herramientas específicas para ETL que pueden ser configuradas y manejadas sin necesidad de programación extensiva:

- **Talend**: Plataforma de integración de datos que soporta múltiples lenguajes y ofrece una interfaz gráfica para diseñar procesos ETL.
- **Informatica PowerCenter**: Herramienta robusta y ampliamente utilizada en empresas para la integración de datos.
- **Microsoft SQL Server Integration Services (SSIS)**: Herramienta de ETL incluida en Microsoft SQL Server.
- **Apache Nifi**: Herramienta para automatizar el flujo de datos entre sistemas.
- **Alteryx**: Plataforma de análisis de datos que facilita la preparación y mezcla de datos.

La elección del lenguaje de programación y la herramienta de ETL depende de varios factores, el entorno de trabajo, los requisitos del proyecto, el volumen de datos, y las habilidades del equipo. **Python** es uno de los más versátiles y ampliamente utilizados, a pesar
de que cada lenguaje y herramienta tiene su nicho y ventajas específicas.

## Que empresas reconocidas implementan ETL

Muchas empresas de diversos sectores implementan procesos ETL (Extracción, Transformación y Carga) para gestionar y procesar grandes volúmenes de datos. Algunas de las empresas más importantes que utilizan ETL son:

### **Amazon**

- **Amazon Web Services (AWS)**: Utiliza y ofrece servicios ETL como AWS Glue, que facilita la preparación y carga de datos para análisis y machine learning.

### **Google**

- **Google Cloud Platform (GCP)**: Ofrece servicios ETL como Google Cloud Dataflow y Google Cloud Dataprep para la integración y preparación de datos.

### **Microsoft**

- **Azure**: Proporciona herramientas como Azure Data Factory y SQL Server Integration Services (SSIS) para procesos ETL en la nube y on-premises.

### **IBM**

- **IBM DataStage**: Una herramienta ETL robusta que es parte de la plataforma IBM InfoSphere para la integración de datos.

### **Oracle**

- **Oracle Data Integrator (ODI)**: Utilizada para la integración de datos en entornos empresariales, soportando procesos ETL complejos.

### **Salesforce**

- **MuleSoft**: Parte de Salesforce, proporciona capacidades de integración de datos y servicios ETL para conectar aplicaciones, datos y dispositivos.

### **Facebook**

- Utiliza procesos ETL extensivos para gestionar datos masivos y alimentar su plataforma de análisis interno, así como servicios de terceros como Apache Hadoop y Apache Hive.

### **Netflix**

- Implementa ETL con herramientas como Apache Spark y Apache Kafka para procesar grandes volúmenes de datos de usuarios y contenidos en tiempo real.

### **Spotify**

- Utiliza ETL para procesar y analizar datos de uso y preferencias de los usuarios, empleando herramientas como Apache Airflow para la orquestación de flujos de datos.

### **Uber**

- Utiliza ETL para manejar datos de viajes, usuarios y conductores, empleando tecnologías como Apache Hadoop y Apache Kafka.

### **Airbnb**

- Implementa procesos ETL con herramientas como Apache Airflow y Apache Spark para la integración y análisis de datos de usuarios y propiedades.

### **LinkedIn**

- Utiliza procesos ETL para gestionar datos de usuarios y conexiones, utilizando tecnologías como Apache Kafka y Apache Samza.

### **Empresas de Tecnología y Consultoría**

- **Accenture, Capgemini, Deloitte**: Utilizan herramientas y procesos ETL para ayudar a sus clientes en la integración de datos y la transformación digital.
- **SAP**: Ofrece soluciones ETL como SAP Data Services para la integración y limpieza de datos empresariales.

### **Instituciones Financieras**

- **JPMorgan Chase, Bank of America, Wells Fargo**: Utilizan procesos ETL para la integración de datos financieros, análisis de riesgos y cumplimiento normativo.

### **Sector de Salud**

- **UnitedHealth Group, Anthem, Mayo Clinic**: Implementan ETL para integrar datos de pacientes, historiales médicos y análisis clínicos.

### **Retail y Comercio Electrónico**

- **Walmart, Target, Alibaba**: Utilizan ETL para integrar y analizar datos de ventas, inventarios y clientes.

Las empresas de diversos sectores implementan procesos ETL para manejar, transformar y analizar grandes volúmenes de datos provenientes de múltiples fuentes. La capacidad de integrar y preparar datos de manera eficiente es fundamental para tomar decisiones informadas y obtener insights valiosos, lo cual es crítico en la era de los datos y la inteligencia artificial.

## Caso de uso real en Retail y Comercio Electrónico

### GEPP en tus manos [(GRUPO GEPP)](https://gepp.com.mx/)

[![GEPP en tus manos](https://play-lh.googleusercontent.com/QTmd77dyeAdYMfkMXfqOioZq5dkaEnA02raN5CNN0Fzx9Yg0pi1W4t1UWaQcpa8k9us=w526-h296-rw)](https://play.google.com/store/apps/details?id=com.sw1848.pepsilealtad&hl=en_US&pli=1)

GEPP en tus manos es una aplicación diseñada para mejorar la **comunicación con nuestros Clientes Directos GEPP**, te mantendremos actualizado con tu estado en los **programas de fidelización**, conocerás el detalle de tus compras y el **cumplimiento de tu cartera GEPP**.
También compartiremos **promociones**, noticias e información interesante sobre sus marcas PEPSI, 7UP, Gatorade, e pura y todas las marcas que conforman la Familia GEPP.

## ¿Cual es el reto a enfrentar en el desarrollo del ETL del core de la APP Gepp en tus manos?

![Caso de uso](/img/etl_use_case.png)

## Soluciones tecnicas implementadas

### **Paralelismo en la lectura**

El paralelismo en la lectura se refiere a la capacidad de realizar múltiples operaciones de lectura de datos de manera simultánea, en lugar de secuencialmente. Esto es especialmente útil en procesos ETL donde grandes volúmenes de datos necesitan ser procesados eficientemente.

#### Ventajas del Paralelismo en la Lectura

- **Mayor Velocidad**: Permite reducir significativamente el tiempo necesario para leer grandes volúmenes de datos.
- **Eficiencia de Recursos**: Aprovecha al máximo los recursos del sistema, como múltiples núcleos de CPU y memoria distribuida.
- **Escalabilidad**: Facilita el manejo de grandes volúmenes de datos a medida que la cantidad de datos y la demanda de procesamiento crecen.

##### Ejemplo de Implementación

```python
# 👾
# Se crea una instancia de la clase Layouts con los archivos especificados en `files`.
layout = LayoutsBase(files)

# Se define un diccionario `tasks` que mapea nombres de tareas a métodos específicos de la instancia `layout`.
# Cada clave del diccionario es un nombre descriptivo de la tarea, y el valor es el método correspondiente
# de la clase `Layouts` que se debe ejecutar para completar esa tarea.
tasks = {
    'layout_clients': layout.layout_clients,
    'layout_clients_cdg': layout.layout_clients_cdg,
    'result_layout_program_sales': layout.layout_clients_sales,
    'result_layout_program_portfolio': layout.layout_clients_portfolio,
    'result_layout_promotions': layout.layout_promotions,
    'result_layout_customer_promotions': layout.layout_customer_promotions,
}

# Se utiliza un gestor de contexto para crear un ThreadPoolExecutor, que permite ejecutar las tareas en paralelo.
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Se crea un diccionario `futures` donde cada clave es el nombre de la tarea y el valor es el futuro
    # que representa la tarea asíncrona. `executor.submit` se utiliza para iniciar la ejecución de cada tarea.
    futures = {name: executor.submit(task) for name, task in tasks.items()}
    # Se espera a que todas las tareas se completen y se recopilan los resultados en el diccionario `results`.
    # `future.result()` bloquea hasta que la tarea asociada se completa y devuelve el resultado.
    results = {name: future.result() for name, future in futures.items()}

# Se extraen los resultados de las tareas específicas del diccionario `results` y se asignan a variables.
layout_grocers_value = results['layout_clients']
layout_grocers_cdg_value = results['layout_clients_cdg']
layout_program_sales_value = results['result_layout_program_sales']
layout_program_portfolio_value = results['result_layout_program_portfolio']
layout_promotions_value = results['result_layout_promotions']
layout_customer_promotions_value = results['result_layout_customer_promotions']

print('parallelism layout base successfully ✅')
```

### **Particionado de Datos**

El particionado de volúmenes grandes de datos es una técnica crucial en el manejo y procesamiento eficiente de grandes cantidades de datos, especialmente en entornos de Big Data. Consiste en dividir un conjunto de datos grande en partes más pequeñas y manejables, llamadas particiones, que pueden ser procesadas en paralelo para mejorar el rendimiento y la escalabilidad.

#### **Ventajas del Particionado de datos**

- **Mejora del Rendimiento**: Permite la lectura y escritura de datos en paralelo, reduciendo el tiempo total de procesamiento.
- **Escalabilidad**: Facilita el manejo de crecientes volúmenes de datos al distribuir la carga de trabajo.
- **Mantenimiento Simplificado**: Hacer operaciones de mantenimiento, como copias de seguridad y restauración, es más manejable en particiones más pequeñas.
- **Optimización de Consultas**: Las consultas pueden ser más rápidas porque solo se escanean las particiones relevantes.

#### **Desafíos del Particionado**

- **Equilibrio de Particiones**: Asegurarse de que las particiones tengan tamaños equilibrados para evitar cuellos de botella.
- **Administración de Metadatos**: Mantener información precisa sobre las particiones puede ser complejo.
- **Consistencia de Datos**: Garantizar que las particiones sean consistentes y que las operaciones de particionamiento no introduzcan errores.

#### **Herramientas y Tecnologías Comunes**

- **Apache Hadoop**: HDFS permite particionar datos y distribuirlos entre nodos.
- **Apache Spark**: Ofrece particionamiento nativo en RDDs y DataFrames para procesamiento paralelo.
- **Apache Hive**: Soporta particionamiento de tablas para optimizar consultas.
- **SQL Databases**: Bases de datos como PostgreSQL, MySQL, y Oracle soportan particionamiento de tablas.
- **NoSQL Databases**: Bases de datos como Cassandra y MongoDB utilizan particionamiento para distribuir datos.

El particionado de volúmenes grandes de datos es esencial para mantener el rendimiento y la escalabilidad en sistemas que manejan grandes cantidades de información. La elección de la estrategia de particionado adecuada depende de la naturaleza de los datos y los patrones de acceso. Implementar particionado de manera efectiva puede resultar en una mejora significativa en la eficiencia de los procesos ETL y en la capacidad de manejar datos a gran escala.

##### Ejemplo de Implementación

```python
# Se crea una instancia de DataAccessLayer.
instance = DataAccessLayer()

# Se crea una instancia de BuildDataframe.
builder = BuildDataframe()

# Se procesa el layout 'grocers_to_dispute' utilizando el builder y la instancia creada,
# pasando el dataframe 'layout_grocers_value' y especificando el método '_grocers_' junto con las columnas deseadas.
grocers_to_dispute = process_layout(builder, instance, layout_grocers_value, '_grocers_', ['column name', 'column name'])

# Define una función para calcular el número de fragmentos en que se debe dividir un dataframe basado en un tamaño máximo.
def calculate_fragments(dataframe) -> int:
    max = 10000  # Tamaño máximo de filas por fragmento.
    size_dataframe = len(dataframe)  # Total de filas en el dataframe.
    num_fragments = size_dataframe // max  # Número básico de fragmentos.
    if size_dataframe % max != 0:  # Si hay un residuo, se necesita un fragmento adicional.
        num_fragments += 1
    return num_fragments

# Define una función para dividir un dataframe en 'count' número de partes.
def dataframe_partitions(dataset, count):
    partitions = np.array_split(dataset, count)  # Utiliza numpy para dividir el dataframe.
    return partitions

# Procesa un layout aplicando un tipo de dato (si se especifica), calculando fragmentos, y aplicando una función a cada fragmento.
def process_layout(builder, instance, dataframe, method, columns, type_cast=None):
    if type_cast:
        dataframe = dataframe.astype(type_cast)  # Cambia el tipo de dato de las columnas si se especifica.
    num = calculate_fragments(dataframe) if len(dataframe) > 10000 else 2  # Calcula el número de fragmentos necesarios.
    partitions = dataframe_partitions(dataframe, num)  # Divide el dataframe en fragmentos.
    builder.__attrib__(partitions, instance, method, columns)  # Asigna atributos al builder.
    return builder.__builder__()  # Construye y devuelve el resultado final.

# Clase para construir un dataframe procesado a partir de fragmentos.
class BuildDataframe:

    # Asigna atributos necesarios para el procesamiento.
    def __attrib__(self, partitions, instance, method, columns):
        self.partitions = partitions  # Fragmentos del dataframe.
        self.is_instance = instance  # Instancia de DataAccessLayer.
        self.is_method = method  # Método a aplicar a cada fragmento.
        self.columns = columns  # Columnas a incluir en el procesamiento.

    # Construye el dataframe procesado.
    def __builder__(self):
        self.method_to_dispute = getattr(self.is_instance, self.is_method)  # Obtiene el método de la instancia.
        self.processed_dataframes = []  # Lista para almacenar dataframes procesados.
        for i, partition_dataset in enumerate(self.partitions):  # Itera sobre cada fragmento.
            dataset = partition_dataset[self.columns]  # Selecciona las columnas especificadas.
            response = self.method_to_dispute(dataset)  # Aplica el método.
            self.processed_dataframes.append(response)  # Añade el resultado a la lista.
        self.response = reduce(DataFrame.union, self.processed_dataframes)  # Combina todos los dataframes procesados.
        return self.response  # Devuelve el dataframe combinado.
```

### **BCP (Bulk Copy Program)**

BCP (Bulk Copy Program) es una herramienta de Microsoft SQL Server que permite importar y exportar grandes volúmenes de datos de manera eficiente. BCP es útil para la transferencia masiva de datos entre archivos y bases de datos SQL Server, lo que lo convierte en una herramienta valiosa para procesos ETL (Extracción, Transformación y Carga).

### Características Principales de BCP

1. **Importación y Exportación de Datos**: Permite copiar datos entre una tabla de SQL Server y un archivo de datos en formato de texto (TXT, CSV, etc.).
2. **Soporte para Grandes Volúmenes de Datos**: Diseñado para manejar grandes cantidades de datos de manera eficiente.
3. **Flexibilidad en el Formato de Datos**: Admite varios formatos de datos y permite especificar formatos personalizados.
4. **Integración con Otros Procesos**: Puede ser utilizado en scripts y procesos automatizados para la manipulación de datos.

### Comandos Básicos de BCP

#### Sintaxis General

```bash
bcp {table | view | "query"} {in | out | queryout | format} data_file 
    [-m max_errors] [-f format_file] [-e err_file] [-F first_row] [-L last_row] 
    [-b batch_size] [-n native_type] [-c character_type] [-w wide_character_type] 
    [-N keep_nulls] [-r row_term] [-t field_term] [-T trusted_connection] 
    [-S server_name[\instance_name]] [-U login_id] [-P password]
```

### Parámetros Comunes

- `-S server_name[\instance_name]`: Nombre del servidor y la instancia.
- `-U login_id`: ID de inicio de sesión.
- `-P password`: Contraseña del usuario.
- `-T`: Utiliza la autenticación de Windows.
- `-c`: Utiliza el tipo de datos de carácter.
- `-t field_term`: Especifica el delimitador de campo.
- `-r row_term`: Especifica el delimitador de fila.
- `-b batch_size`: Número de filas por lote de transacción.
- `-F first_row`: Primera fila a copiar.
- `-L last_row`: Última fila a copiar.
- `-m max_errors`: Número máximo de errores permitidos.

### Mejores Prácticas (Best Practices) para el Uso de BCP

1. **Utilizar Autenticación Segura**: Preferir la autenticación de Windows (`-T`) sobre la autenticación SQL (`-U` y `-P`), cuando sea posible.
2. **Control de Errores**: Utilizar el parámetro `-e` para especificar un archivo de errores y `-m` para establecer el número máximo de errores permitidos.
3. **Optimización de Lotes**: Ajustar el tamaño del lote (`-b`) para equilibrar la velocidad de carga y la utilización de recursos.
4. **Formato de Datos**: Usar archivos de formato (`-f`) para manejar datos con formatos complejos o personalizados.
5. **Validación de Datos**: Validar y limpiar los datos antes de la importación para minimizar errores y problemas de integridad.
6. **Paralelización**: Dividir grandes conjuntos de datos en fragmentos más pequeños y procesarlos en paralelo para mejorar el rendimiento.

##### Ejemplo de Implementación

```python
# Define una función para ejecutar un comando bcp para importar datos desde un archivo CSV a una tabla de SQL Server.
def run_bcp_command(path_csv, table_name):
    # Construye el comando bcp utilizando variables para la tabla, el archivo CSV, y las credenciales de la base de datos.
    bcp_command = f"/opt/mssql-tools/bin/bcp {table_name} in {path_csv} -c -t, -S {DATABASE_HOST} -d {DATABASE_NAME} -U {DATABASE_USER} -P {DATABASE_PASSWORD} > ./logs/bcp.log 2>&1"
    try:
        # Ejecuta el comando bcp utilizando subprocess.run. `shell=True` permite ejecutar el comando como si estuviera en la shell.
        # `check=True` hace que se lance una excepción si el comando falla.
        subprocess.run(bcp_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        # Captura cualquier error que ocurra durante la ejecución del comando bcp y lo imprime.
        print(f"Error executing bcp command: {e}")

```

## **Arquitectura y DevOps**

### Pasado execution time 8.37 hrs

![Infra](/img/architecture_microsoft_server.png)

### Presente execution time 32 min

![Infra](/img/architecture_azure.png)
<!-- 
## **Consejo de la comunidad MongoDB**

Microsoft Data Platform MVP, MongoDB Certified Developer
[Leandro Domingues](https://www.mongodb.com/community/advocacy/leandro-domingues/)

![MongoDB Conference](/img/photo_1.jpg)
![Consejo](/img/photo_2.jpg)

## **"Documentos y schemas flexibles son el nuevo petroleo piensen sobre eso."**

## **Demo**

Explicación del código de este repositorio -->

### **Consideraciones Finales**

El proceso ETL es una columna vertebral imprescindible en cualquier proyecto de Inteligencia Artificial. Asegura que los datos necesarios estén disponibles, sean de alta calidad y estén en el formato correcto. Sin un proceso ETL robusto, la creación, entrenamiento y despliegue de modelos de IA sería significativamente más complejo y menos eficiente. Por lo tanto, dominar las técnicas y herramientas de ETL no solo es beneficioso, sino esencial para cualquier profesional que trabaje en el campo de la IA y el análisis de datos.