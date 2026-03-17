# Estrategia de Reutilización Anual de Sitios

Cuando un evento se repite cada año (Ej: *The Walk 2024*, *The Walk 2025*), surge la pregunta: **¿Reutilizo el mismo sitio de SharePoint y borro lo viejo, o creo uno nuevo?**

En SharePoint Moderno, la recomendación de Microsoft es casi siempre **crear un sitio nuevo**. Aquí explicamos por qué y cómo manejar ambas estrategias.

---

## Estrategia 1: "Nuevo Año, Nuevo Sitio" (Recomendada)

En lugar de borrar tareas viejas, creas un sitio fresco usando el **Site Script** que ya automatizamos.

*   **Ejemplo:** Tienes `casafamiliar.sharepoint.com/sites/TheWalk2024`. El próximo año creas `.../sites/TheWalk2025`.

### Ventajas
1.  **Auditoría perfecta:** Tienes un archivo histórico intacto de lo que pasó en 2024 (quién hizo qué, cuánto costó, qué falló).
2.  **Cero riesgo de borrado:** No hay peligro de que alguien borre por accidente un contrato de 2024 creyendo que era "basura" para limpiar la lista.
3.  **Cumplimiento Legal (Purview):** Las políticas de retención de 10 años funcionan perfectamente porque el sitio viejo simplemente se archiva (ver [[05-Plan-Gobernanza-Datos]]).
4.  **Rapidez:** Gracias a tu Site Script ([[04h-Site-Script]]), crear el sitio 2025 y sus listas toma menos de 2 minutos.

### Desventajas
*   Genera más sitios en tu consola de administración (lo cual es normal y esperado en Microsoft 365).

### Flujo de Trabajo (Paso a Paso):
1.  **Cierre del Evento (Noviembre 2024):** Cambias los permisos del sitio `TheWalk2024` a "Solo Lectura". Nada se toca.
2.  **Inicio Nuevo Ciclo (Enero 2025):** Creas el sitio `TheWalk2025`.
3.  **Aplicar Template:** Ejecutas el template "Casa Familiar - Full Event Setup" en el nuevo sitio.
4.  **Enlazar al Hub:** El script ya lo conecta automáticamente al hub principal.
5.  **Copiar Plantillas:** Mueves manualmente solo los documentos de plantilla "en blanco" (ej: formato de check-in) del sitio 2024 al 2025.

---

## Estrategia 2: "Reciclaje de Sitio" (No recomendada, pero posible )

Usas exactamente el mismo sitio (`casafamiliar.sharepoint.com/sites/TheWalk`) año tras año, limpiando las listas.

### Ventajas
*   La URL nunca cambia. Los voluntarios siempre guardan el mismo link en sus favoritos.
*   No tienes que mover ni copiar documentos base de un año a otro.

### Desventajas (Riesgos Altos)
1.  **Pérdida de Historial:** Para usar listas como *Event Tasks* limpias, alguien tiene que borrar las tareas del año pasado. Se pierde el historial operativo.
2.  **Choque Legal:** Si configuras la política de Retención de 10 años, **Microsoft M365 te impedirá borrar elementos** de la lista para reciclarlos. El sistema te marcará error al intentar "limpiar" para el nuevo año.
3.  **Saturación de Vistas:** Si decides *no* borrar, sino solo cambiar la columna `CF_YearCycle` (ej: filtrar la vista para que solo muestre "2025"), después de 3 años tu lista de Tareas será inmensa, muy lenta de cargar, y la búsqueda será un caos.

### Flujo de Trabajo (Si decides hacerlo así):
1.  **Cierre del Evento:** Debes exportar tus listas (Tasks, Risks, Budget) a Excel como respaldo histórico.
2.  **Limpieza manual:** Un administrador debe entrar y borrar **todos** los elementos de todas las listas. *(Reitero: esto fallará si tienes Retention Policies activas)*.
3.  **Actualizar Documentos:** Mover los documentos del año pasado a una carpeta llamada "Archive 2024".

---

## Veredicto para Casa Familiar

Dado que has implementado **Site Scripts Autómatizados** y necesitas **Políticas de Retención de Contratos**, la única estrategia viable y segura a largo plazo es la **Estrategia 1 (Nuevo Año, Nuevo Sitio)**.

**Solución al problema del "link eterno":**
Para evitar que los usuarios se confundan con URLs nuevas cada año, la mejor práctica es:
En tu **Hub Site principal**, pon un botón gigante que diga "Ir al Evento The Walk Actual". Tú como administrador, solo actualizas ese botón cada año para que apunte al nuevo sitio (del 2024 al 2025). El usuario final solo tiene que recordar la ruta del Hub Site.

### 📂 Relacionado
*   [[04h-Site-Script|Recuerda cómo aplicar el template para sitios nuevos]]
*   [[05-Plan-Gobernanza-Datos|Reglas sobre qué hacer con los sitios viejos]]
