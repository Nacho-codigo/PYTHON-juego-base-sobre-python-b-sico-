print("\t\t\t\t---------------------------------------------------")
print("\t\t\t\t\t\t🅳 🅴 🆂 🅰  🅵 í🅾   🆀 🆄 🅸 🆉")
print("\t\t\t\t---------------------------------------------------")
print("\t\t\t\t\t\t5 preguntas para saber...")
print("\t\t\t\t\t\t¿que tanto sabes de python?")
print("\t\t\t\t---------------------------------------------------")
nombre=input("\t\t\t\t\tingrese su nombre: ")
print("\t\t\t\t---------------------------------------------------")
input("\t\t\t\t\tprecione la tecla Enter para comenzar...").upper()
puntos=0
preguntas=["¿Qué es Python y para qué se usa?",
           "¿Qué es una lista en Python ?",
           "¿Cómo se utiliza un bucle `for` en Python?",
           "¿Qué es una función en Python y cómo se define?",
           "¿Qué es una cadena de texto en Python?"]
respuestas=["1","2","3","1","3"]

pregunta=[ 
"\t\t\t\t  "
"\n1) Python es un lenguaje de programación. Se usa en desarrollo web, análisis de datos, IA, desarrollo de software y automatización de tareas."
"\n2) Python es un lenguaje solo compatible con sistemas operativos Windows y no puede ejecutarse en Linux o macOS."
"\n3) Un bucle `for` en Python se utiliza para iterar sobre una secuencia (como una lista, tupla, cadena o rango).",
"\n\t\t\t\t-----Opciones de la segunda pregunta-----"
"\n1) Las listas en Python no pueden contener otros tipos de datos, solo pueden almacenar números enteros."
"\n2) Una lista en Python es una colección ordenada y mutable de elementos que se define entre corchetes `[]`."
"\n3) Las listas en Python tienen un tamaño fijo y no se pueden modificar después de ser creadas.",
"\n\t\t\t\t-----Opciones de la tercera pregunta-----"
"\n1) Un bucle `for` en Python solo se puede usar con listas; no se puede usar con cadenas o tuplas."
"\n2) El bucle `for` se ejecutará infinitamente a menos que se use la palabra clave `stop` para detenerlo."
"\n3) Un bucle `for` en Python se utiliza para iterar sobre una secuencia (como una lista, tupla, cadena o rango).",
"\n\t\t\t\t-----Opciones de la cuarta pregunta-----"
"\n1) Una función en Python es un bloque de código reutilizable que se define para realizar una tarea específica. "
"\n2) En Python, para definir una función, debes usar la palabra clave `function`, como en otros lenguajes."
"\n3) Las funciones en Python no pueden recibir parámetros y siempre deben devolver un valor.",
"\n\t\t\t\t-----Opciones de la quinta pregunta-----"
"\n1) Una cadena de texto en Python es una colección de datos que se puede definir solo entre corchetes {}"
"\n2) Una cadena de texto en Python es un tipo de dato que solo puede contener números enteros."
"\n3) Una cadena de texto (string) es una secuencia de caracteres, que se puede definir entre comillas simples ' o dobles ''."
]

print("\t\t\t\t---------------------------------------------------")
print("\t\t\t\t\t\t\tEN JUEGO")
print("\t\t\t\t\t\t\t¡¡VAMOS!!") 
print("\t\t\t\t---------------------------------------------------")

opciones=["1","2","3"]
for x in range (5):
    print(preguntas[x])
    print(pregunta[x])
    while True:
        respuesta=input(f"escriba la respuesta conveniente de la pregunta número {x+1}:  ")
        if respuesta in opciones:
            break
        else:
            print("Carácter inválido. Por favor, ingrese 1, 2 o 3.")

    if respuesta==respuestas[x]:
        print("\t\t\t\t\t\t\t¡¡correcto!!")
        print("\t\t\t\t\t\t\t¡¡¡MUY BIEN!!!")
        puntos+=2
    else:
        print("\t\t\t\t\t\t\t\tincorrecto")
        print("\t\t\t\t\t\t\t¡CASI!,!SIGUE INTENTANDO¡")    

print("\t\t\t\t\t\t\t¡¡¡TERMINASTE!!!")
if puntos == 10:
        print(f"¡puntaje perfecto {nombre}!, tu puntaje es de {puntos} puntos APROBASTE   :)")
elif   puntos<=9 and puntos >=6:
        print (f"¡bien echo {nombre}!,tu puntaje es de {puntos} puntos APROBASTE   :)")
else: 
        print(f"que lastima {nombre}, no obtuviste lo suficiente para aprobar :( , tu puntaje es de: {puntos} puntos") 