# %% [markdown]
# # Analisis de datos Netflix (Jesus Morillo)

# %%

import pandas as pd
data = pd.read_csv(r"D:\Documentos\Visual Code\Analisis de datos netflix\Netflix_DataSet.csv")

data

# %% [markdown]
# # ¿Hay registros duplicados en este conjunto de datos? En caso afirmativo, elimine los registros duplicados.

# %%
data.head()

# %%
data.shape

# %%
data[data.duplicated()] #con este codigo buscamos datos duplicados

# %%
data.drop_duplicates(inplace = True)#con este codigo eliminamos datos duplicados permanentemente

# %%
data[data.duplicated()]

# %%
data.shape

# %% [markdown]
# # ¿Hay algún valor nulo preestablecido en alguna columna? mostrar con mapa de calor

# %%
data.isnull()

# %%
import seaborn as sns 
sns.heatmap(data.isnull ())

# %% [markdown]
# # Para "castillo de cartas", ¿cuál es el ID del programa y quién es el director de este programa?

# %%
data.head()

data[data['Title'].isin(['House of Cards'])]

data[data['Title'].str.contains('House of Cards')]

# %% [markdown]
# # ¿En qué año se estrenó el mayor número de programas de televisión y películas? mostrar con gráfico de barras

# %%

data['Date_N'] = pd.to_datetime(data['Release_Date'], errors='coerce')

data.head()


# %%
data["Date_N"].dt.year.value_counts() #Esto cuentas los años individualmente 

data['Date_N'].dt.year.value_counts().plot(kind='bar')

# %% [markdown]
# # ¿Cuántas películas y programas de televisión hay en el conjunto de datos? mostrar con gráfico de barras
# 

# %%
data.groupby('Category').Category.count()
import seaborn as sns
sns.countplot(x='Category', data=data)


# %% [markdown]
# # mostrar todas las películas que se estrenaron en el año 2000

# %%

data['Year'] = data ['Date_N'].dt.year

data [ (data['Category'] == 'Movie') & (data['Year']==2000) ] 

# %%
data [ (data['Category'] == 'Movie') & (data['Year']==2020) ] 

# %% [markdown]
# 
# # Top 10 de directores a los que le dieron las mayores nominaciones a series y películas de netflix

# %%
data.head(2) 

# %%
data['Director'].value_counts().head(10)

# %% [markdown]
# # mostrar todos los registros, donde "la categoría es película y el tipo son comedias" o "el país es reino unido"

# %%

data[ (data['Category'] == 'Movie') & (data['Type']=='Comedies') | (data['Country']=='United Kingdom')]

# %% [markdown]
# 
# # ¿Cuáles son las diferentes clasificaciones definidas por Netflix?

# %%
data.head(2)

data['Rating'].nunique()

data['Rating'].unique()

# %% [markdown]
# # ¿Cuanto fue la máxima duracion de una pelicula o espectaculo en netflix?

# %%
data.Duration.unique() 
data.Duration.dtype
data.head(2)

data[['Minutes', 'Unit']] = data ['Duration'].str.split(' ',expand = True)

data.head(2)


# %%
data['Minutes'].max()  

# %%
data['Minutes'].min()

# %% [markdown]
# # ¿Cómo podemos ordenar el conjunto de datos por año?

# %%
data.sort_values(by = 'Year', ascending= False).head(10)

# %% [markdown]
# # Categorize peliculas y series
# 

# %%
data [ (data['Category'] == 'Movie') & (data ['Type'] == 'Dramas')].head(2)


