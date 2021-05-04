# prueba-buda

## Introducción

Este es un problema de grafos, el cual puede ser solucionado de varias maneras, tales como  [Dijkstra's](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), [A*](https://en.wikipedia.org/wiki/A*_search_algorithm) o  [BFS 0-1](https://cp-algorithms.com/graph/01_bfs.html) para este caso, utilizaremos BFS 0-1 ya que tiene una eficiencia mayor y se acomoda perfecto a lo que necesitamos.


## Estructura de Entrada

```json
    {
        "stations": {
            "A": {
                "connectedStations": [
                    "B"
                ],
                "color": ""
            },
            "B": {
                "connectedStations": [
                    "A",
                    "C"
                ],
                "color": ""
            }
        }
    }
```


## Estructura de Salida

En caso de encontrar una ruta:

    A->B->C->D->E->F

En caso de no encontrar rutas:

    No Routes

## Ejecución

### Pre Configuración

    # Crear entorno virtual
    python3 -m venv buda-metro 

    # Activar entorno Virtual
    source buda-metro/bin/activate

    # Instalar Paquetes
    pip install -r requirements.txt


### Ejecución

    python src/main.py test_inputs/example_input.json A F red              

## Pruebas Unitarias
Estas pruebas deben ejecutarse desde el directorio root

    pytest
