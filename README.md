# Kata de Refactorización de Yatzy

**Readme de la kata por [Emily Bache](https://github.com/emilybache)** ¡Gracias! :clap::clap:

[Repositorio de kata de Emily Bache](https://github.com/emilybache/Yatzy-Refactoring-Kata)

*Diseñada por Jon Jagger. Está disponible en su Cyber-Dojo. [Publicación en el blog](http://jonjagger.blogspot.co.uk/2012/05/yahtzee-cyber-dojo-refactoring-in-java.html)*

---

## Kata: Reglas de Yatzy

El juego de Yatzy es un simple juego de dados. Cada jugador
lanza cinco dados de seis caras. Pueden volver a tirar algunos o todos
los dados hasta tres veces (incluido el lanzamiento inicial).

Por ejemplo, supongamos que un jugador lanza:

    3,4,5,5,2
    
Mantiene (-,-,5,5,-) y vuelve a tirar (3,4,-,-,2):

    5,1,5,5,3

Mantiene (5,-,5,5,-) y vuelve a tirar (-,1,-,-,3):

    5,6,5,5,2

El jugador luego coloca la tirada en una categoría, como unos,
doses, cincos, par, dos pares, etc. (ver más abajo). Si la tirada es
compatible con la categoría, el jugador obtiene una puntuación
según las reglas. Si no es compatible con la categoría, el jugador
obtiene cero puntos.

Por ejemplo, supongamos que un jugador obtiene 5,6,5,5,2 en la categoría
de cincos. Puntuaría 15 (tres cincos). La puntuación de esa ronda
se suma al total del jugador y la categoría no puede volver a usarse
durante el resto del juego.
Un juego completo consiste en una tirada para cada categoría. Por lo tanto, en
la última ronda de un juego, un jugador debe elegir su única categoría restante.

Tu tarea es puntuar una **tirada dada** en una **categoría dada**.
No necesitas programar el lanzamiento aleatorio de los dados.
El juego **no implica que el ordenador elija la categoría con mayor puntuación**
para una tirada.

---

## Kata: Categorías de Yatzy y Reglas de Puntuación

### Chance: 
El jugador puntúa la suma de todos los dados, sin importar el valor.  
Por ejemplo:
  
-   1,1,3,3,6 colocado en "chance" puntúa 14 (1+1+3+3+6)
-   4,5,5,6,1 colocado en "chance" puntúa 21 (4+5+5+6+1)  

### Yatzy: 
Si todos los dados tienen el mismo número, el jugador puntúa 50 puntos.  
Por ejemplo:
  
-   1,1,1,1,1 colocado en "yatzy" puntúa 50
-   1,1,1,2,1 colocado en "yatzy" puntúa 0

### Unos, Doses, Treses, Cuatros, Cincos, Seises: 
El jugador puntúa la suma de los dados que coincidan con el número correspondiente.  
Por ejemplo:

-   1,1,2,4,4 colocado en "cuatros" puntúa 8 (4+4)
-   2,3,2,5,1 colocado en "doses" puntúa 4  (2+2)
-   3,3,3,4,5 colocado en "unos" puntúa 0

### Par: 
El jugador puntúa la suma de los dos dados iguales más altos.  
Por ejemplo, cuando se coloca en "par":
  
-   3,3,3,4,4 puntúa 8 (4+4)
-   1,1,6,2,6 puntúa 12 (6+6)
-   3,3,3,4,1 puntúa 6 (3+3)
-   3,3,3,3,1 puntúa 6 (3+3)

### Dos pares: 
Si hay dos pares de dados iguales, el jugador puntúa la suma de estos dados.  
Por ejemplo, cuando se coloca en "dos pares":
  
-   1,1,2,3,3 puntúa 8 (1+1+3+3)
-   1,1,2,3,4 puntúa 0
-   1,1,2,2,2 puntúa 6 (1+1+2+2)

### Trío: 
Si hay tres dados iguales, el jugador puntúa la suma de estos dados.  
Por ejemplo, cuando se coloca en "trío":
    
-    3,3,3,4,5 puntúa 9 (3+3+3)
-    3,3,4,5,6 puntúa 0
-    3,3,3,3,1 puntúa 9 (3+3+3)

### Póker (Cuatro iguales): 
Si hay cuatro dados iguales, el jugador puntúa la suma de estos dados.  
Por ejemplo, cuando se coloca en "cuatro iguales":
  
-    2,2,2,2,5 puntúa 8 (2+2+2+2)
-    2,2,2,5,5 puntúa 0
-    2,2,2,2,2 puntúa 8 (2+2+2+2)

### Escalera pequeña: 
Cuando se coloca en "escalera pequeña", si los dados son:

   1,2,3,4,5, 
   
el jugador puntúa 15 (la suma de los dados).

### Escalera grande: 
Cuando se coloca en "escalera grande", si los dados son:

   2,3,4,5,6, 
   
el jugador puntúa 20 (la suma de los dados).

### Full: 
Si los dados forman un trío y un par, el jugador puntúa la suma de todos los dados.  
Por ejemplo, cuando se coloca en "full":
   
-    1,1,2,2,2 puntúa 8 (1+1+2+2+2) 
-    2,2,3,3,4 puntúa 0
-    4,4,4,4,4 puntúa 0
