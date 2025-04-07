# Entrega Final

# Python Comisión 75140 - Alumno: Andy Garcia. 

# ¿De qué se trata el proyecto?

El proyecto se trata de un "sistema de gestion" basico para un restaurante de tipo "Sandwich".

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

## Caracteristicas:

1. Cuenta con la posibilidad de hacer CRUD con absolutamente todos los modelos presentes.

2. Cuenta con una estetica moderna y responsiva.

3. Es increiblemente mejorable a futuro.

4. Cuenta con un login funcional.

## Mejoras a futuro:

1. La posibilidad de transforma el campo de "nombre" a la hora de crear un pedido por una caja selectiva entre otro modelo llamado "Platos" donde se especificaria cuales son los platos disponibles en ese momento.

2. Mejora significativa en la estetica de la pagina en si.

3. Mejora en el sistema de login.

4. Crear barras "nav" diferentes, tanto para los empleados, como para los hipoteticos chefs o para el gerente en caso de despedir a alguien.

5. Mejora a la seguridad del sistema.

6. Entre muchisimas otras mejoras posibles.