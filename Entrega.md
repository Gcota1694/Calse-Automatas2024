Informe de Progreso y Planificación de Proyecto

 Funcionalidades Actuales del Programa Evaluador de Archivos JSON 

Este documento detalla las funcionalidades actuales de nuestro programa evaluador de archivos JSON, así como las posibles actualizaciones y proyecciones del proyecto.

Funcionalidades del Programa 

 la fecha, nuestro programa realiza las siguientes tareas:

1. **Lectura de Archivos**: Lee un archivo JSON externo.
2. **Asignación de Tokens**: Genera una lista de cada carácter del archivo, asignándole su respectivo token en valor unicode.
3. **Validación de JSON**: Verifica si el archivo JSON es válido, comprobando que el primer token sea `{`. Si no es así, el programa se detiene y muestra un mensaje de error.
4. **Verificación de Cierres**: Asegura que las comillas dobles iniciales tengan su correspondiente cierre, y en caso contrario, emite una alerta.
5
 Funcionalidades Pendientes 

El programa está en desarrollo y necesita incluir las siguientes funcionalidades:

1. **Validación de Fechas**: Confirmar que el formato de fecha sea válido.
2. **Validación de Flotantes**: Asegurar que los elementos de tipo flotante solo contengan un punto decimal.
3. **Verificación de Llaves de Cierre**: Evaluar la presencia de una llave de cierre `}`.


Proyecciones y Alcance del Proyecto 

Actualmente, el programa actúa principalmente como un evaluador léxico de archivos JSON. En el futuro, sería beneficioso e interesante expandir sus capacidades para incluir análisis sintáctico y semántico. 
