La distancia calculada por la función `haversine` está expresada en **kilómetros**. Esto se debe a que el valor del radio de la Tierra `R` en la función se define como 6371, que es el radio medio de la Tierra en kilómetros.

### Explicación de la Función `haversine`

1. **Definición del Radio de la Tierra:**
   ```python
   R = 6371  # Radio de la tierra en kilómetros
   ```
   El radio de la Tierra se define en kilómetros.

2. **Cálculo de la Diferencia en Radianes:**
   ```python
   dlat = np.radians(lat2 - lat1)
   dlon = np.radians(lon2 - lon1)
   ```
   Se convierten las diferencias de latitud y longitud de grados a radianes.

3. **Fórmula de Haversine:**
   ```python
   a = np.sin(dlat / 2) * np.sin(dlat / 2) + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2) * np.sin(dlon / 2)
   c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
   return R * c
   ```
   Se aplica la fórmula de Haversine para calcular la distancia en la superficie de una esfera. El resultado final se multiplica por el radio de la Tierra en kilómetros para obtener la distancia en kilómetros.

### Uso en el DataFrame

La distancia calculada y agregada al DataFrame `df` es la distancia en kilómetros desde cada ubicación en el DataFrame hasta la Ciudad de México.

### Ejemplo Completo

Aquí está el código completo para calcular y mostrar las distancias:

```python
import pandas as pd
import numpy as np

data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'name': ['San Fernando', 'Baja California', 'Atlautla', 'Sonora', 'Guerrero', 'Campeche', 
             'San Fernando', 'Baja California', 'Atlautla', 'Sonora', 'Guerrero', 'Campeche'],
    'lat': [24.824646, 29.647522, 19.017468, 29.197306, 17.608842, 19.095527, 24.824646, 29.647522, 
            19.017468, 29.197306, 17.608842, 19.095527],
    'lon': [-98.093303, -115.507482, -98.728794, -110.500352, -100.284628, -90.508196, 
            -98.093303, -115.507482, -98.728794, -110.500352, -100.284628, -90.508196],
    'weather_description': ['nubes', 'algo de nubes', 'lluvia ligera', 'cielo claro', 'lluvia ligera', 
                            'nubes', 'nubes', 'algo de nubes', 'lluvia ligera', 'cielo claro', 
                            'lluvia ligera', 'nubes'],
    'sys_country': ['MX'] * 12,
    'address': ['San Fernando', 'Punta San Carlos', 'Atlautla', 'Noria', 'Cruz de Ocote', 
                'Carrillo Puerto', 'San Fernando', 'Punta San Carlos', 'Atlautla', 'Noria', 
                'Cruz de Ocote', 'Carrillo Puerto'],
    'city': ['Tamaulipas', 'Baja California', 'State of Mexico', 'Sonora', 'Guerrero', 
             'Campeche', 'Tamaulipas', 'Baja California', 'State of Mexico', 'Sonora', 
             'Guerrero', 'Campeche'],
    'country': ['Mexico'] * 12
}

df = pd.DataFrame(data)

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radio de la tierra en kilómetros
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    a = np.sin(dlat / 2) * np.sin(dlat / 2) + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2) * np.sin(dlon / 2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return R * c

# Coordenadas de la Ciudad de México
cdmx_lat, cdmx_lon = 19.432608, -99.133209

df['distance_to_cdmx'] = df.apply(lambda row: haversine(row['lat'], row['lon'], cdmx_lat, cdmx_lon), axis=1)

print(df[['name', 'distance_to_cdmx']])
```

Esto mostrará las distancias en kilómetros desde cada ubicación hasta la Ciudad de México.