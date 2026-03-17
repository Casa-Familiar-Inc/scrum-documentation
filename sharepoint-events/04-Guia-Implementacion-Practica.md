# Guía Maestra de Implementación: Sistema "Casa Familiar Events"

Esta es la guía definitiva para implementar y administrar el ecosistema de sitios de eventos. El sistema está diseñado en la **Experiencia Moderna de SharePoint** (Modern Experience).

---

## Prerrequisitos de Automatización (Septiembre 2024)
Antes de ejecutar cualquier script (`.ps1`) o subir archivos JSON, tienes dos opciones según tu preferencia:

### Opción A: Módulo Oficial de SharePoint (SPO)
*   **Uso:** Ideal para registrar el Site Script (JSON) de forma "oficial".
*   **Fácil:** No requiere registrar aplicaciones de terceros.
*   **Guía:** **[[04j-Official-SPO-Deployment|Ver pasos con el módulo oficial aquí]]**.

### Opción B: PnP PowerShell (Recomendado para Expertos)
*   **Uso:** Necesario para crear carpetas, menús complejos y automatización de contenido.
*   **Poderoso:** Mucho más flexible pero requiere el registro de Entra ID.
*   **Guía:** **[[04e-Detalle-Site-Scripts|Ver pasos con PnP aquí]]**.

---

## Fase 1: Configuración del Hub (The "Brain")
*Esta fase se realiza manualmente por única vez en el sitio principal.*

1.  **Crear el Hub Site:**
    *   Nombre: `Event Planning Improvements Project` (o el nombre de tu Hub).
    *   Registrarlo como **Hub Site** en el Centro de Administración de SharePoint.
2.  **Columnas de Sitio (The Metadata):**
    *   Define las 3 columnas maestras en el Hub para que todos los eventos hablen el mismo idioma.
    *   **[[04a-Detalle-Columnas-Base|Ver configuración exacta de columnas aquí]]**
3.  **Políticas de Cumplimiento (Compliance):**
    *   Configura las reglas para que los contratos y actas no se borren por error.
    *   **[[04d-Detalle-Retention-Policies|Ver configuración de Retención]]**
4.  **Estructura de Archivos y Menú:**
    *   Configura las bibliotecas de "Master Templates" y el "MegaMenu" en inglés.
    *   **[[08-Hub-Site-English-Content|Ver blueprint del Hub y Menú]]**
    *   **[[09-Event-Site-Folder-Structure|Ver estructura operativa para Sitios de Eventos]]**
    *   **Automatización:** Usa `create-hub-folders.ps1` para el Hub y `create-event-folders.ps1` para cada sitio nuevo.

---

## Fase 2: Automatización de Sitios (The "Blueprint")
*Usa plantillas (Site Scripts) para crear sitios de eventos en 2 minutos.*

1.  **El Molde Maestro (JSON):**
    *   Usa la versión "Ultimate" que ya tiene todos los campos de Tareas, Presupuesto, Riesgos y Roster configurados.
    *   **[[04h-Site-Script|Instrucciones de Despliegue del Script V5]]**
2.  **Registro del Tema (Branding):**
    *   Asegúrate de registrar el tema "Teal" para que los sitios se vean profesionales. (Instrucciones dentro de la guía de Site Scripts arriba).

---

## Fase 3: Gobierno y Continuidad (The "Control")
*Cómo mantener el orden a través de los años.*

1.  **Plan de Gobernanza:**
    *   Reglas sobre quién puede editar qué y cuándo los sitios pasan a modo "Solo Lectura".
    *   **[[05-Plan-Gobernanza-Datos|Plan de Gobernanza de Datos]]**
2.  **Estrategia de Reutilización:**
    *   ¿Crear sitio nuevo o limpiar el viejo? (Pista: Siempre es mejor uno nuevo).
    *   **[[06-Estrategia-Reutilizacion-Anual|Plan de Reutilización Anual]]**
3.  **Gestión Centralizada de Archivos:**
    *   Cómo fluyen las plantillas desde el Hub hacia los sitios de eventos.
    *   **[[07-Estrategia-Archivos-Centralizados|Estrategia de Documentos]]**

---

## Fase 4: Visualización y Formato (The "Look")
*Haz que la información sea fácil de consumir para los voluntarios.*

1.  **Formato de Colores (JSON):**
    *   Códigos para que el estatus "Blocked" sea rojo y "Completed" verde automáticamente.
    *   **[[04b-JSON-Formatting-Templates|Ver códigos de formato visual]]**
2.  **Diseño de Páginas:**
    *   Cómo acomodar los elementos en la página principal para que el comité vea sus tareas al entrar.
    *   **[[04f-Detalle-Visualizacion-Paginas|Ver guía de diseño de páginas]]**

---

## Fase 5: Futuras Mejoras (Native Power)
Para el futuro, considera usar herramientas nativas para extender la funcionalidad:
*   **[[05-Future-Native-Improvements|Ver ideas de automatización con Power Automate]]**

---
