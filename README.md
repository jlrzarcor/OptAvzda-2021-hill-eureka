# Maestría en Ciencia de Datos,

<p align = "center">
    <img src="images/logo_itam.png" width="300" height="110" />

-------

### *Optimización Avanzada* (Primavera 2021)

### Prof. Mat. Erick Palacios Moreno

**Proyecto Final**

-------


**Equipo 5.**


| Github_User | Alumno | Rol |
|:---:|:---|:---|
| @lobolc | Miguel | Programmer |
| @Carlosrlpzi | Carlos | Programmer | 
| @ZarCorvus | José Luis | Reviewer & Project Manager |

-------


#### Título del proyecto:  

### Implementación y Optimización del método heurístico _Hill Climbing_ para resolver el _Traveling Salesman Problem_ (TSP)

#### Objetivo del proyecto:

En optimización matemática y ciencias de la computación, los métodos heurísticos y metahurísticos se desarrollaron para resolver problemas del tipo 
_large scale_ (PL´s o de optmización combinatoria) que son muy grandes y complicados como para resolverlos por medio de algoritmos exactos. Típicamente se
ajustan a problemas especificos.

En nuestro caso, seleccionamos _Hill Climbing_, método de optimización que pertenece al grupo de búsqueda local. Encuentra la solución óptima en 
el caso de problemas convexos (como el algoritmo símplex que resuelve problemas de optimización convexa mediante _hill climbing_) y soluciones óptimas locales 
(no necesariamente son soluciones óptimas globales) entre todas las posibles soluciones del espacio de búsqueda. Por lo tanto, es importante remarcar que no
existe garantía acerca de la calidad de la solución que se obtiene.

Existe un problema importante conocido como el _Traveling Salesman Problem_ (TSP), el cual plantea la siguiente interrogante:

"Dado un conjunto de ciudades y la distancia que existe entre cada par de ellas... ¿cuál es la ruta más corta posible que visita cada ciudad exactamente una vez
y retorna a la ciudad orígen?"

Responder a estar interrogante es equivalente a calcular todas las rutas posibles (permutaciones) y determinar la de menor distancia (algortimo de fuerza bruta),
lo cual implica un tiempo de ejecución que cae en un factor polinommial el orden $O(n!)$ (el factorial del número de ciudades), lo cual es impráctico tan sólo 
para 20 ciudades.
 
El método _Hill Climbing_ se puede aplicar para resolver el TSP y obtener una solución óptima para un conjunto pequeño de ciudades de forma muy rápida. Conforme
se incrementa el tamaño del conjunto, este método requiere mayor tiempo para explorar el espacio de posibles soluciones de forma suficiente para encontrar una solución
óptima global. Por lo que, nuestro objetivo es explorando diversas opciones que permiten una implementación más eficiente del método, ya sea
* Modificaciones en la técnica, p.e. _random restart_
* Integrar eficiencia de código como cómputo en paralelo o _multiprocessing_ 
* Utilizar estrategias de solución como el uso de Kubernetes (minikube) con contenedore de Docker. 
buscando obtener soluciones más cercanas al óptimo global en un periodo de tiempo razonable.

-------

**Fecha de Entrega:** Jueves 20 de Mayo del 2021, 23:59 hrs.

-------

Para una experiencia interactiva con el código de nuestro repositorio, puedes utilizar el botón [binder](https://mybinder.org/):


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jlrzarcor/OptAvzda-2021-hill-eureka/main?urlpath=lab)

Es necesario instalar nuestro paquete **hill_cg** en este ambiente para poder ejecutar nuestro reporte.

______

Puedes visitar nuestro sitio para conocer la documentación del paquete en línea:

[paquete_experimental_hill_climbing](https://optimizacion-2-2021-1-gh-classroom.github.io/practica-2-segunda-parte-jlrzarcor/)

______

**Bibliografía**
* Russell, Stuart J.; Norvig, Peter (2003), Artificial Intelligence: A Modern Approach (2nd ed.), Upper Saddle River, New Jersey: Prentice Hall, pp. 111–114.

**Referencias:**
* [Hill climbing towards article](https://towardsdatascience.com/how-to-implement-the-hill-climbing-algorithm-in-python-1c65c29469de)
* [Perfilamiento, Notas del Prof. Erick](https://itam-ds.github.io/analisis-numerico-computo-cientifico/V.optimizacion_de_codigo/5.2/Herramientas_de_lenguajes_y_del_SO_para_perfilamiento_e_implementaciones_de_BLAS.html)
* [Compilación a C, Notas del Prof. Erick](https://itam-ds.github.io/analisis-numerico-computo-cientifico/V.optimizacion_de_codigo/5.3/Compilacion_a_C.html)
* [OR tools TSP](https://developers.google.com/optimization/routing/tsp)

* [Hill climbing, Wikipedia](https://en.wikipedia.org/wiki/Hill_climbing)
* [Combinatorial optimization, Wikipedia](https://en.wikipedia.org/wiki/Combinatorial_optimization)
* [Time complexity](https://en.wikipedia.org/wiki/Time_complexity)
* [NP-completeness, Wikipedia](https://en.wikipedia.org/wiki/NP-completeness)
* [NP-hardness, Wikipedia](https://en.wikipedia.org/wiki/NP-hardness)
* [Metaheuristic, Wikipedia](https://en.wikipedia.org/wiki/Metaheuristic)
* [Travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)
