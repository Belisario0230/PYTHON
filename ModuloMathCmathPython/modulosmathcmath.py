# -*- coding: utf-8 -*-
"""ModulosMathCmath.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11MzHnDIw9AfrQpvB5kncKsgAL9aWNhpq

# Módulos de `Python`: `math` y `cmath`

## `math`

El módulo `math` nos proporciona funciones matemáticas definidas según los estándares del lenguaje de programación `C`.

**¡Cuidado!** Las funciones del módulo `math` no pueden ser usadas con números complejos. Para trabajar con números complejos, tenemos el módulo `cmath` que trataremos más adelante en esta misma sección.
"""

import math

dir(math)

"""### Constantes del módulo `math`

El número $\pi = 3.141492\dots$ lo obtenemos como atributo del módulo `math` como
"""

math.pi

"""El número $e = 2.718281\dots$ lo botenemos como atributo del módulo `math` como"""

math.e

"""La constante $\tau = 6.283185\dots$ también forma parte del módulo `math`"""

math.tau

"""El infinito positivo, $\infty$, lo obtenemos en el módulo `math` como"""

math.inf

"""**Observación.** El infinito negativo, -$\infty$, puede obtenerse multiplicando -1 al resultado de `math.inf`"""

-math.inf

"""El último atributo del módulo `math` es `nan` (valor `NaN`, not a number)"""

math.nan

"""### Métodos del módulo `math`

#### Parte entera de un número

**Parte entera de $x$.** Dado un número real $x$, se define su parte entera como el mayor número entero menor o igual que $x$.

Para obtener la parte entera de un número real, podemos usar el método `.floor()`
"""

x = 2.75
math.floor(x)

x = -3.1415
math.floor(x)

"""**Parte entera por exceso de $x$.** Dado un número real $x$, se define su parte entera por exceso como el menor número entero mayor o igual que $x$.

Para obtener la parte entera por exceso de un número real, podemos usar el método `.ceil()`
"""

x = 2.75
math.ceil(x)

x = -3.1415
math.ceil(x)

"""Existen otra función más que dado un número real, nos devuelven su parte entera. Se trata de la función de truncamiento.

Para truncar un número, utilizamos el método `.trunc()`
"""

x = 2.75
math.trunc(x)

x = -3.1415
math.trunc(x)

"""#### Aritmética

Para calcular el resto de $x$ entre $y$ siendo $x,y$ números reales, se prefiere usar el método `.fmod()` al operador `%`, pues el primero tiene mucha más precisión al tratar con números reales.
"""

x = 5.25
y = 2.5
math.fmod(x, y)

"""En este caso, para comprobar nuestros resultados, podríamos hacer lo siguiente"""

x == math.floor(x / y) * y + math.fmod(x, y)

"""Dado un objeto iterable (por ejemplo una lista) de números reales, el método `.fsum()` calcula la suma de todos los elementos de dicho iterable de forma precisa en coma flotante"""

l = [.1] * 10
print("El resultado de sum() sería {}".format(sum(l)))
print("El resultado de math.fsum() sería {}".format(math.fsum(l)))

"""Con el método `.modf()` conseguimos la tupla de parte decimal y entera de un número real $x$"""

math.modf(4.25)

math.modf(-3.1415)

"""#### Potencias y logaritmos

El método `.exp()` nos devuelve el número $e^x$ donde $x$ es el valor indicado por parámetro
"""

math.exp(2)

"""**Observación.** Por tanto, el número $e$ en `Python` se puede obtener como la función exponencial para $x = 1$. No obstante, recordemos que el módulo  `math` tiene el atributo `e` que es precisamente dicho número"""

e = math.exp(1)
e

math.e

"""Siguiendo con la función exponencial, tenemos el método `.expm1()` que es el resultado de $e^x - 1$ donde $x$ es el número que introducimos por parámetro"""

math.exp(2) - 1

math.expm1(2)

"""**Observación.** La existencia de este método se debe a la gran pérdida de precisión que conlleva restar una unidad directamente. De este modo, el método `.expm1()` ha sido programado de forma que no se pierda tal cantidad de precisión al llevar a cabo dicha operación.

El método `.frexp()` de un número real $x$ nos devuelve el par `(m, e)` donde $m$ y $e$ son tales que $x = m\cdot 2^e$
"""

x = 25
m, e = math.frexp(x)
print("(m = {}, e = {})".format(m, e))

"""Para comprobar nuestro resultado, hacemos lo siguiente"""

x == m * 2 ** e

"""Por su parte, existe el método inverso a `.frexp()`, que es el método `.ldexp()`, al que por parámetros introducimos `x` e `i` y se nos devuelve el valor $y$ tal que $y = x \cdot 2^i$"""

x = 0.78125
i = 5
math.ldexp(x, i)

"""El método `.log()` nos devuelve resultados diferentes según los argumentos proporcionados:

* Si solamente indicamos el número $x$ al que queremos aplicar el logaritmo, entonces se nos devuelve el resultado de calcular el logaritmo neperiano (logaritmo en base $e$) de $x$
* Si introducimos dos parámetros, el primero será el número $x$ al que aplicamos el logaritmo, y el segundo, la base.
"""

# Logaritmo neperiano de 55
math.log(55)

# Logaritmo neperiano de 55
math.log(55, math.e)

# Logaritmo en base 10 de 100
math.log(100, 10)

"""El método `.log1p()` devuelve el logaritmo neperiano de $1 + x$, donde $x$ es el número que introducimos por parámetro. La existencia de este método aumenta la precisión del resultado cuando $x$ es próximo a 0."""

math.log1p(2)

math.log(3)

"""El método `.log2()` nos devuelve el logaritmo en base 2 de $x$, $\log_2(x)$, siendo $x$ el número real que introducimos por parámetro"""

math.log2(1024)

math.log(1024, 2)

"""Del mismo modo, existe el método `.log10()` para calcular el logaritmo en base 10 de $x$, $\log_{10}(x)$"""

math.log10(100)

math.log(100, 10)

"""El método `.pow()` ya lo conocemos. Nos calcula la potencia $x^y$, siendo `x` el primer parámetro indicado e `y` el segundo."""

math.pow(2, 10)

2 ** 10

"""El método `.sqrt()` aplicado a un número entero $n$ nos devuelve la raíz cuadrada de dicho número entero $n$."""

math.sqrt(25)

math.sqrt(77)

"""#### Máximo común divisor y mínimo común múltiplo

Para calcular el máximo común divisor de dos números, usamos el método `.gcd()` (del inglés, greatest common divisor)
"""

math.gcd(16, 8)

"""Para calcular el mínimo común múltiplo de dos números, usamos el método `.lcm()` (del inglés, least common multiple), disponible a partir de la versión 3.9 de `Python`. Como nosotros en este momento todavía trabajamos con la 3.8, hemos decidido crear una implementación:"""

def lcm(a, b):
    return math.fabs(a*b) // math.gcd(a, b)

lcm(16, 8)

"""#### Combinatoria

**Factorial de $n$.** Dado un número entero positivo $n$, definimos su número factorial como $$n! = n\cdot (n-1)\cdot (n-2)\cdots 2\cdot 1$$

Para calcular el factorial de un número entero, usamos el método `.factorial()`
"""

math.factorial(10)

"""**Número combinatorio ${n\choose k}$.** El número de $n$ sobre $k$, siendo $n\ge k$ ambos números enteros positivos, viene dado por

$${n\choose k} = \frac{n!}{k!(n-k)!}$$

Si quisiésemos calcular un número combinatorio, podríamos usar el método `.comb()`, pero existe un bug en el cual en versiones más recientes de `Python`, este método no forma parte del módulo `math`, de modo que hemos decidido implementar dicho método nosotros mismos.
"""

def choose(n, k):
  if (n >= k and k >= 0):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
  else:
    return "No se puede calcular el número factorial indicado"

choose(10, 2)

"""#### Valor absoluto

Para calcular el valor absoluto de un número real $x$, utilizamos el método `.fabs()`
"""

x = -2.36
math.fabs(x)

"""#### Signo

Dados dos números reales $x$ e $y$, si usamos el método `.copysign()` obtendremos como resultado el valor absoluto del primer parámetro introducido, $x$, pero con el signo dado por el segundo parámetro, $y$.
"""

x = 2.5
y = -3.4
math.copysign(x, y)

x = -2.5
y = -3.4
math.copysign(x, y)

x = -2.5
y = 3.4
math.copysign(x, y)

x = 2.5
y = 3.4
math.copysign(x, y)

"""#### Funciones trigonométricas

Todas las funciones tringonométricas toman como parámetro radianes o bien, devuelven el resultado en radianes.

Para convertir de grados a radianes, podemos usar el método `.radians()`
"""

math.radians(90)

"""Para convertir de radianes a grados, podemos usar el método `.degrees()`"""

math.degrees(math.pi/2)

"""La función seno se calcula con el método `.sin()`"""

math.sin(math.pi/2)

"""La función coseno se calcula con el método `.cos()`"""

math.cos(math.pi/2)

"""La función tangente se calcula con el método `.tan()`"""

math.tan(math.pi/4)

"""La función arcoseno se calcula con el método `.asin()`"""

math.asin(1)

"""La función arcocoseno se calcula con el método `.acos()`"""

math.acos(0)

"""La función arcotangenet se calcula con el método `.atan()`"""

math.atan(1)

"""Existe el método `.atan2()` que toma dos parámetros, $y$ en primer lugar y $x$ en segundo, que proceden de las coordenadas del punto $(x,y)$. El propósito de este método es que devuelve el resultado en el intervalo $(-\pi, \pi]$, pues conoce el signo de ambas coordenadas, de modo que puede computar el correcto cuadrante para el ángulo correspondiente al formado por el punto $(x,y)$ con respecto a la parte positiva del eje horizontal."""

math.atan2(1, 1)

math.atan2(-1, -1)

"""El método `.hypot()` calcula la norma euclídea del vector 2-dimensional cuyas coordenadas indicamos por parámetro

**Norma euclídea.** La norma euclídea de un vector $x$ $2$-dimensional viene dada por

$$||x|| = \sqrt{x_1^2 + x_2^2}$$
"""

# Norma euclídea del vector (3, 4)
math.hypot(3, 4)

"""#### Funciones hiperbólicas

De nuevo, o bien los parámetros o bien los resultados de estas funciones se encuentran en radianes.

El seno hiperbólico se calcula con el método `.sinh()`
"""

math.sinh(math.pi)

"""El coseno hiperbólico se calcula con el método `.cosh()`"""

math.cosh(math.pi)

"""La tangente hiperbólica se calcula con el método `.tanh()`"""

math.tanh(math.pi)

"""El arcoseno hiperbólico se calcula con el método `.asinh()`"""

math.asinh(11.548739357257748)

"""El arcocoseno hiperbólico se calcula con el método `.acosh()`"""

math.acosh(11.591953275521519)

"""La arcotangente hiperbólica se calcula con el método `.atanh()`"""

math.atanh(0.99627207622075)

"""#### Funciones de clasificación

Para comprobar si dos números son cercanos, concepto que dependerá de las tolerancias relativa y absoluta indicadas, usamos el método `isclose()`

* La tolerancia relativa, `rel_tol`, es la diferencia máxima permitida entre los parámetros `a` y `b`, relativa al mayor valor absoluto de dichos parámetros. La tolerancia relativa se encuentra en el intervalo [0, 1].
* La tolerancia absoluta es la tolerancia absoluta mínima. Como mínimo debe valer 0.
"""

math.isclose(4, 4.000000000001)

math.isclose(4, 5, rel_tol = 0.5)

"""El método `.isfinite()` nos devolverá `True` siempre que el parámetro `x` introducido no se trate ni del infinito ni de un valor `NaN`."""

math.isfinite(2.8)

math.isfinite(math.nan)

math.isfinite(math.inf)

"""Por el contrario, el método `.isinf()` nos devolverá `True` si el parámetro introducido `x` se trata de un valor infinito."""

math.isinf(2.8)

math.isinf(math.inf)

math.isinf(math.nan)

"""También tenemos el método `is.nan()` que nos devuelve `True` si el parámetro `x` se trata de un valor `NaN`"""

math.isnan(math.nan)

"""#### Funciones especiales

Ya para terminar con el módulo `math`, veremos 4 métodos más:

El método `.erf()` sirve para calcular la función de error en el valor $x$ que indicamos por parámetro

**Función error.** Viene dada por `erf(x)` = $\frac{2}{\pi}\int_0^xe^{-t^2}dt$
"""

math.erf(25 / math.sqrt(2))

"""El método `.erfc()` sirve para calcular el complementario de la función error en el valor $x$ que introducimos por parámetro. Este viene dado por `erfc(x) =  1 - erf(x)`"""

math.erfc(25 / math.sqrt(2))

"""El método `.gamma()` nos calcula el valor de la función Gamma en $x$, donde la función Gamma viene dada por

$$\Gamma(x) = \int_0^{\infty}y^{x-1}e^{-y}dy$$

$\Gamma(x) = (x-1)!$ si $x$ es un número entero
"""

math.gamma(3)

"""Por último, el método `.lgamma()` nos devuelve el logaritmo neperiano del valor de la función Gamma evaluada en $x$. Es decir, nos calcula $\log(\Gamma(x))$"""

math.lgamma(3)

math.log(math.gamma(3))

"""## `cmath`

El módulo `cmath` nos proporciona funciones matemáticas definidas según los estándares del lenguaje de programación `C` que pueden usarse con números complejos a modo de argumento.
"""

import cmath

"""### Constantes del módulo `cmath`

Además de tener las mismas constantes que el módulo `math`

* `cmath.pi`
* `cmath.e`
* `cmath.tau`
* `cmath.inf`
* `cmath.nan`

el módulo `cmath` consta de 2 constantes extras:

* `cmath.infj`: se trata del número complejo cuya parte real vale 0 y cuya parte imaginaria vale $\infty$
* `cmath.nanj`: se trata del número complejo cuya parte real vale 0 y cuya parte imaginaria vale `NaN`

### Métodos del módulo `cmath`

#### Coordenadas polares

El método `.phase()` nos calcula el argumento del número complejo `x` que introducimos por parámetro. El resultado es devuelto en radianes dentro del intervalo $[-\pi, \pi]$
"""

cmath.phase(complex(-1, 0))

"""Para pasar de coordenadas rectangulares a coordenadas polares, hacemos uso del método `.polar()`"""

cmath.polar(complex(-1, 0))

"""Si queremos hacer el cambio inverso, es decir, pasar de coordenadas polares a coordenadas cartesianas, entonces usamos el método `.rect()`, donde como primer parámetro pasamos el módulo, y en segundo lugar, el argumento del número complejo en cuestión."""

cmath.rect(1, cmath.pi)

"""#### Potencias y logaritmos

Los métodos que encontramos en este módulo en relación al cálculo de potencias y logartimos, son algunos de los que ya vimos en el módulo `math`:

* `cmath.exp()`: calcula $e^x$, donde `x` es el número complejo que introducimos por parámetro
* `cmath.log()`: si no indicamos la base, por defecto se calcula el logaritmo neperiano de $x$, siendo `x` el número complejo indicado por parámetro. Si por el contrario introducimos un segundo argumento, la base, entonces se calculará el logaritmo en la base indicada del número complejo `x`
* `cmath.log10()`: calcula el logartimo en base 10 de $x$, siendo `x` el número complejo introducido por parámetro
* `cmath.sqrt()`: calcula la raíz cuadrada del número complejo `x` indicado por parámetro
"""

x = complex(1, -1)
print("x =", x)
print("e^x =", cmath.exp(x))
print("ln(x) =", cmath.log(x))
print("log_{10}(x) =", cmath.log10(x))
print("sqrt(x) =", cmath.sqrt(x))

"""#### Funciones trigonométricas

Para el caso de números complejos en `Python`, tenemos las siguientes funciones trigonométricas:

* `cmath.sin()`
* `cmath.cos()`
* `cmath.tan()`
* `cmath.asin()`
* `cmath.acos()`
* `cmath.atan()`
"""

x = complex(0, -1)
print("x =", x)
print("sin(x) =", cmath.sin(x))
print("cos(x) =", cmath.cos(x))
print("tan(x) =", cmath.tan(x))
print("asin(-1.1752011936438014j) =", cmath.asin(-1.1752011936438014j))
print("acos(1.5430806348152437+0j) =", cmath.acos(1.5430806348152437+0j))
print("atan(-0.7615941559557649j) =", cmath.atan(-0.7615941559557649j))

"""#### Funciones hiperbólicas

Las funciones hiperbólicas que vimos en el módulo `math` admiten el uso de números complejos a modo de parámetros si las llamamos desde el módulo `cmath`:

* `cmath.sinh()`
* `cmath.cosh()`
* `cmath.tanh()`
* `cmath.asinh()`
* `cmath.acosh()`
* `cmath.atanh()`
"""

x = complex(0, 1)
print("x =", x)
print("sinh(x) =", cmath.sinh(x))
print("cosh(x) =", cmath.cosh(x))
print("tanh(x) =", cmath.tanh(x))
print("asinh(0.8414709848078965j) =", cmath.asinh(0.8414709848078965j))
print("acosh(0.5403023058681398+0j) =", cmath.acosh(0.5403023058681398+0j))
print("atanh(1.5574077246549023j) =", cmath.atanh(1.5574077246549023j))

"""#### Funciones de clasificación

En el módulo `cmath` también hallamos las funciones de clasificación que tratamos al hablar del módulo `math`:

* `cmath.isclose()`
* `cmath.isfinite()`
* `cmath.isinf()`
* `cmath.isnan()`

que funcionan exactamente igual, salvo por el hecho de que admiten números complejos como parámetro
"""

# Comprobar si dos números complejos son cercanos según la tolerancia
cmath.isclose(4j, 4.000000000001j)

# Comprobar si un número es finito
cmath.isfinite(cmath.infj)

cmath.isfinite(5 + 5j)

# Comprobar si un número es infinito
cmath.isinf(cmath.infj)

cmath.isinf(5 + 5j)

# Comprobar si un número es NaN
cmath.isnan(cmath.nan + 1j)

cmath.isnan(cmath.nanj)

cmath.isnan(cmath.nan + cmath.nanj)