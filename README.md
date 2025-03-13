# Entrega nro 3

# Pruebas de la Aplicación "AppCoder"

Para probar la aplicación "AppCoder", sigue estos pasos:

1. **Iniciar el servidor de Django**:
   - Comando:
     ```bash
     python manage.py runserver
     ```

2. **Acceder al panel de administración**:
   - Abre tu navegador, abre el panedl de admin de django con "(RutaDeTuLocalhost)/admin"
   - Inicia sesión con las siguientes credenciales:
     - **Usuario**: admin
     - **Contraseña**: 1234

3. **Añade modelos**:
   - Una vez dentro del panel de administración, puedes crear los siguientes modelos:
     - **Gerente**
     - **Empleado**
   - Ten en cuenta que para crear un **Pedido**, primero debes haber creado al menos un **Empleado**.

4. **Visualizar los modelos**:
   - Después de crear los modelos, sal del panel de administración y dirígete a la ruta raíz "http://localhost:8000/".
   - Allí verás una barra que muestra todos tus modelos. Al hacer clic en cualquiera de ellos, accederás a un listado de los **Gerentes**, **Empleados** o **Pedidos** que has creado.

Con estos pasos, habrás probado con éxito la aplicación "AppCoder".

# Consigna

Crea una web en Django utilizando Herencia de plantillas, con un modelo de por lo menos 3 clases, un formulario para ingresar datos a las 3 clases y un formulario para buscar algo en la base de datos. No hace falta que la búsqueda abarque las tres clases; con realizar la búsqueda sobre una será suficiente.

Te sugerimos que hagas una web estilo blog para ir preparando la entrega final.

## Objetivos

Desarrollar tu primera web en Django utilizando el patrón MVT.

## Requisitos

- Link de GitHub con el proyecto totalmente subido a la plataforma.

### Proyecto Web Django con patrón MVT que incluya:

- Herencia de HTML.
- Por lo menos 3 clases en `models`.
- Un formulario para insertar datos para cada modelo creado.
- Un formulario para buscar algo en la base de datos.
- Un archivo `README` que indique el orden en el que se prueban las cosas y/o dónde están las funcionalidades.

## Formato

Link al repositorio de GitHub con el nombre “TuPrimeraPagina+Apellido”, por ejemplo “TuPrimeraPagina+Fernandez”.
