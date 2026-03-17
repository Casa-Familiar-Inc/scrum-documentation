# Detalle Técnico: Retention Policies (Microsoft Purview)

### 1. ¿Qué es una Retention Policy?
Es una regla de cumplimiento que vive por encima de SharePoint, en el **Microsoft Purview (Compliance Center)**. Sirve para asegurar que la información importante no se pierda, ya sea por error humano o de forma intencionada.

En tu proyecto, los **contratos y presupuestos** son críticos. Una política de retención garantiza que, aunque alguien intente borrar un archivo, SharePoint guardará una copia oculta durante el tiempo que definas.

---

### 2. Configuración en Microsoft Purview

Para configurar esto, un administrador debe ir a: **Microsoft 365 Admin Center** -> **Compliance** (o Purview) -> **Data Lifecycle Management** -> **Microsoft 365** -> **Retention Policies**.

#### Configuración Recomendada para Casa Familiar:
*   **Name:** `Retention Policy - Event Contracts (5 Years)`
*   **Description:** `Retención obligatoria para documentos de contratos y finanzas de eventos.`
*   **Type:** **Static** (Para aplicar a sitios específicos).
*   **Locations:** Selecciona **SharePoint sites**. Puedes elegir aplicarlo a todos los sitios o solo a los que pertenecen al Hub de eventos.
*   **Retention Settings:**
    *   **Retain items for a specific period:** `5 years`.
    *   **Start the retention period based on:** `When items were created`.
    *   **At the end of the retention period:** `Do nothing` (o borrar automáticamente si quieres limpieza total).

---

### 3. ¿Cómo funciona en la vida real?
Si un usuario intenta borrar un contrato bajo esta política:

1.  El archivo parece desaparecer de la biblioteca de documentos.
2.  Sin embargo, SharePoint lo mueve automáticamente a una biblioteca oculta llamada **"Preservation Hold Library"**.
3.  Solo los administradores con permisos especiales pueden ver o recuperar esos archivos de esa biblioteca oculta durante los 5 años que dura la política.

### 4. Diferencia entre "Retention Policy" y "Retention Label"
*   **Policy (Política):** Se aplica a **todo el sitio** o biblioteca. Es automática y el usuario no tiene que hacer nada. *(Esta es la recomendada para tu Fase 1).*
*   **Label (Etiqueta):** El usuario elige manualmente qué archivos marcar (ej: marcar solo el archivo "Contrato.pdf"). Es más flexible pero requiere que la gente se acuerde de poner la etiqueta.

### 📂 Relacionado
*   [[04-Guia-Implementacion-Practica|Volver a la Guía Principal]]
