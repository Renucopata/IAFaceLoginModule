# Login con reconocimiento facial - Final Topicos IA

## Desarrollador
Rene Alejandro Rengel Arevalo  
Código de estudiante: 49962

## Descripción del Proyecto
Este proyecto implementa un sistema de autenticación biométrica a través de reconocimiento facial para proporcionar un método seguro y conveniente de acceso a cuentas. La aplicación incluye una pantalla de inicio de sesión y otra de registro que permite a los usuarios registrar su rostro como credencial para acceder a sus cuentas de manera rápida y segura. Este proyecto pretende ser un mudulo de registro para alguna aplicacion la cual quiera implementar este metodo de seguridad en cualquier aplicacion de computadora.

### Autenticación Facial:
Utiliza la MTCNN + TensorFlow para el reconocimiento de rostros y entrenamiento del modelo, permitiendo a los usuarios autenticarse mediante la verificación de su rostro.
### Interfaz Gráfica con Tkinter:
La interfaz de usuario está construida con Tkinter, proporcionando una interfaz fácil de usar y entender.

## Version de Python
Para este proyecto python 3.10.4

## Instrucciones de Uso
1. Instale las dependencias especificadas en el archivo `requirements.txt` con el comando: pip install -r requirements.txt.
2. En Visual Studio Code abra el archivo Login.py y apretar el boton "Run Code"
3. Para tomar la foto ya sea para el registro del nuevo rostro o el login, aprete la tecla de espacio (ASCII --> 32).
4. Tome en cuenta verificar la seccion de output en VS code para poder visualizar todos los mensajes y el porcentaje de similitud que se encontro para la autenticacion
5. Este porcentaje de tolerancia puede ser modificado en la linea 145 del codigo.
