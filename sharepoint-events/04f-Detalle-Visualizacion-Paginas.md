# Detalle Técnico: Visualización en Páginas (Web Parts)

### 1. La Diferencia entre Lista y Página
*   **La Lista:** Es el "depósito" de datos. Es donde entras a escribir las tareas, elegir el año y ver los colores. (Ej: `https://tu-sitio/Lists/EventTasks`).
*   **La Página:** Es la "cara" del sitio. Es lo que los usuarios ven al entrar (Home). Aquí es donde **muestras** la lista de forma elegante.

---

### 2. Cómo agregar tus Columnas Maestras a una Lista
Si ya tienes una lista creada y quieres empezar a usar tus columnas (Status, Year, Role), sigue esta ruta para no tener que crearlas de nuevo:

1.  Entra a la lista en SharePoint.
2.  Haz clic en el engrane (Settings) -> List settings.
3.  Baja a la sección Columns y haz clic en Add from existing site columns.
4.  En "Select columns from", elige tu grupo _Casa Familiar.
5.  Selecciona la columna, dale a Add > y luego a OK.

---

### 3. Cómo mostrar tu lista en la Página Principal (Home)
Para que el comité vea sus tareas al entrar al sitio:
1. Ve a la página de inicio (Home) y haz clic en Edit (esquina superior derecha).
2. Haz clic en el círculo con el símbolo de más (+) para agregar un nuevo web part.
3. Busca y selecciona el web part de List.
4. Selecciona la lista de tareas (ej: Event Tasks).
5. Haz clic en Republish para guardar los cambios.

---

### 4. Personalizar la vista en la Página
Una vez que la lista está en la página, puedes:
*   **Filtrar:** Configurar el componente para que solo muestre las tareas "Blocked".
*   **Esconder columnas:** Para que la página no se vea muy cargada, puedes esconder la columna "ID" o "Creado por" y dejar solo lo importante.

### 5. Resumen Visual
*   **¿Dónde vive la columna?** En la Lista.
*   **¿Dónde se ve el Dashboard?** En la Página (usando el Web Part de Lista).

### Relacionado
*   [[04b-JSON-Formatting-Templates|Asegúrate de tener aplicados los colores JSON para que la página sea impactante.]]
*   [[04-Guia-Implementacion-Practica|Volver a la Guía Principal]]
