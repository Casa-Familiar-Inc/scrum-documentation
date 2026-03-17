# Detalle Técnico: Content Types (Plantillas de Listas)

### 1. ¿Qué es un "Content Type"?
Si las **Site Columns** son los ingredientes, el **Content Type** es la "receta". Es una plantilla que agrupa varias columnas para que puedas aplicarlas a una lista de un solo golpe.

---

### 2. Instrucciones para Crear el Content Type

Para ambos, ve a: **Settings** (Engranaje) -> **Site information** -> **View all site settings** -> **Site content types** -> **Create content type**.

#### A. Content Type: `Event Task CT` (Para Tareas)
Llena los campos exactamente así:

*   **Name:** `Event Task CT`
*   **Description:** `Plantilla maestra para las tareas de los eventos de Casa Familiar.`
*   **Category:** Selecciona **"New category"** y escribe `_Casa Familiar` (Para que aparezca junto a tus columnas).
*   **Parent content type:**
    *   **Parent category:** `List Content Types`
    *   **Content type:** `Item` (Es la base más limpia para construir listas personalizadas).

---

#### B. Content Type: `Roster CT` (Para el Comité)
Llena los campos exactamente así:

*   **Name:** `Roster CT`
*   **Description:** `Plantilla maestra para el listado de personas y roles del comité.`
*   **Category:** Selecciona **"Existing category"** -> `_Casa Familiar`.
*   **Parent content type:**
    *   **Parent category:** `List Content Types`
    *   **Content type:** `Item`.

---

### 3. El Paso Final: Agregar tus Columnas
Una vez que le des a **Create**, SharePoint te llevará a la pantalla del nuevo Content Type. Haz lo siguiente para terminar la "receta":

1.  Haz clic en **Add site column** (o *Add from existing site columns*).
2.  Busca tu grupo `_Casa Familiar`.
3.  Agrega las columnas correspondientes:
    *   Para `Event Task CT`: Agrega `CF_TaskStatus` y `CF_YearCycle`.
    *   Para `Roster CT`: Agrega `CF_CommitteeRole` y `CF_YearCycle`.

### 📂Relacionado
*   [[04a-Detalle-Columnas-Base|Guía de Columnas (Ingredientes)]]
*   [[04-Guia-Implementacion-Practica|Volver a la Guía Principal]]
