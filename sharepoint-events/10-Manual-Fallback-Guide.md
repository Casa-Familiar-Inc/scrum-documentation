# 10 - Plan B: Guía de Creación Manual (Fallback)

Si por alguna razón técnica (temas de permisos, bloqueos de TI, o fallos de conexión) los scripts automatizados de JSON (`hub-site-template.json` y `event-site-template.json`) no se pueden ejecutar, deberás crear la infraestructura de forma manual. 

Esta guía detalla **exactamente** qué configura el código JSON para que puedas replicarlo a mano haciendo clics en la interfaz de SharePoint.

---

## 1. Configuración Manual del HUB SITE (El Portal Principal)

### 1.1 Apariencia y Navegación
1. Ve al engrane (⚙️) > **Change the look** > **Navigation**.
2. Cambia el diseño de la navegación a **Megamenu**.
3. Ve al engrane (⚙️) > **Change the look** > **Header** y cámbialo a **Compact**.
4. Edita la navegación principal (Edit en el menú) y **elimina**: `Home`, `Conversations`, `Documents`, `Notebook`, `Pages`, `Site contents`.
5. **Agrega** los siguientes enlaces:
   * Home
   * Master Templates
   * Global Policies
   * Event Directory
   * Past Events Archive

### 1.2 Lista: Event Directory (Directorio de Eventos)
Crea una nueva lista en blanco (engrane > Add an app > Custom List) llamada **Event Directory**.
Agrega las siguientes columnas (Type: `Text` o el indicado):
* **Title** (Por defecto, renómbralo a "Event Link Name" si deseas).
* **Event Name** (Text - *Requerido*)
* **Event Date** (DateTime - *Requerido*)
* **Event Year** (Text - *Requerido*)
* **Event Lead** (User - *Requerido*)
* **Event Status** (Text - *Requerido*)
* **Event Budget Limit** (Number)

### 1.3 Lista: Casa Familiar Vendors (Proveedores)
Crea una nueva lista llamada **Casa Familiar Vendors**.
Agrega las siguientes columnas:
* **Vendor Name** (Text - *Requerido*)
* **Vendor Type** (Text - *Requerido*)
* **Contact Name** (Text - *Requerido*)
* **Phone Number** (Text)
* **Email Address** (Text)
* **Rating (1-5)** (Number)
* **Notes** (Note/Multiple lines of text)

---

## 2. Configuración Manual del EVENT SITE (Sitios Individuales)

Cada vez que crees un nuevo evento (ej. "The Walk 2024"), deberás configurar manualmente sus 4 listas operativas y el menú lateral.

### 2.1 Navegación Izquierda
1. Edita el menú lateral y **elimina**: `Home`, `Conversations`, `Documents`, `Notebook`, `Pages`, `Site contents`.
2. **Agrega** los siguientes enlaces apuntando a las listas:
   * Home
   * Event Tasks
   * 01 - Budget & Financials
   * 02 - Risk Register
   * 03 - Committee Roster
   * Working Documents (apuntando a la biblioteca de Documentos)

### 2.2 Lista 1: Event Tasks (Tareas)
Crea una lista en blanco llamada **Event Tasks**. Agrega:
* **Title** (Columna por defecto, úsala para el "Nombre / Descripción corta de la tarea").
* **CF_TaskStatus** (Choice)
* **CF_YearCycle** (Choice)
* **Due Date** (DateTime - *Requerido*)
* **Assigned To** (User - *Requerido*)
* **Priority** (Text)
* **Category** (Text)
* **Percent Complete** (Number)
* **Notes** (Note)
* **Start Date** (DateTime)

### 2.3 Lista 2: Risks (Riesgos)
Crea una lista en blanco llamada **Risks**. Agrega:
* **Title** (Columna por defecto, úsala para el "Título del Riesgo").
* **CF_TaskStatus** (Choice)
* **Risk Category** (Text)
* **Probability** (Text)
* **Impact Level** (Text)
* **Risk Owner** (User)
* **Mitigation Plan** (Note)
* **Review Date** (DateTime)

### 2.4 Lista 3: Committee Roster (Directorio del Comité)
Crea una lista en blanco llamada **Committee Roster**. Agrega:
* **Title** (Columna por defecto, úsala para el "Nombre del Miembro").
* **Role** (Text - *Requerido*)
* **Year** (Text - *Requerido*)
* **Phone** (Text)
* **Email** (Text)
* **Emergency Contact** (Text)
* **Availability** (Text)
* **Special Skills** (Note)

### 2.5 Lista 4: Event Budget (Presupuesto)
Crea una lista en blanco llamada **Event Budget**. Agrega:
* **Title** (Columna por defecto, úsala para el "Concepto / Nombre del Gasto").
* **Expense Category** (Text - *Requerido*)
* **Vendor** (User - O campo tipo Lookup si se prefiere)
* **Estimated Cost** (Number - *Requerido*)
* **Actual Cost** (Number)
* **Payment Status** (Text)
* **Approved By** (User)
* **Invoice Date** (DateTime)
* **Receipt Notes** (Note)

---
> **Nota de Gobernanza:** Recuerda que tras crear estas columnas como "Texto", la guía recomienda cambiarlas a tipo "Choice" (Opciones desplegables) entrando a Settings > List Settings, para evitar errores de captura de los usuarios.
