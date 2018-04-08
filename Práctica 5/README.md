# Análisis Léxico y Sintáctico

Se crean los autómatas finitos deterministas por medio de expresiones regulares y ya no por medio de un menú para cada operación existente.

- Crear Autómata: A partir de una expresión regular ingresada se crea el AFN con las siguientes reglas:
  - &: Concatenación
  - |: Unión
  - +: Cerradura Positiva
  - *: Cerradura de Kleene
  - ?: Cerradura Opcional
  - [a-z]: Rangos (dentro de corchetes)
  - \: Anteceder a un símbolo especial (Ejemplo: &, |, +, *, ?, (, ), [, ], -) para que forme parte del alfabeto y no sea una operación.
- Validar cadena: A partir de un autómata creado, se ingresan cadenas para validar si pertenecen o no al lenguaje del AFN.
- Unir Autómatas: Unión de n autómatas definidos por el usuario manteniendo los estados de aceptación de cada uno.
- Convertir a AFD: Conversión de un AFN a un AFD
- Análisis léxico: Muestra la secuencia de tokens y lexemas según la cadena ingresada a partir de un AFD.

# Autores

Joel Mauricio Romero Gamarra

Luis Ricardo Téllez Girón
