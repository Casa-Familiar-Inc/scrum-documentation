# JSON Formatting Templates

Estos códigos se pegan en la sección **"Column Formatting"** (al final de la pantalla de creación de la columna) o seleccionando la columna en la lista -> **Column settings** -> **Format this column**.

### 1. [[CF_TaskStatus_Formatting|JSON para CF_TaskStatus (Estado)]]
Este JSON crea burbujas de color con texto en blanco para visibilidad inmediata.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/sp/v2/column-formatting.schema.json",
  "elmType": "div",
  "txtContent": "@currentField",
  "style": {
    "padding": "4px 10px",
    "border-radius": "16px",
    "color": "white",
    "font-weight": "600",
    "text-align": "center",
    "background-color": "=if(@currentField == '1. Pending', '#607d8b', if(@currentField == '2. In Progress', '#0078d4', if(@currentField == '3. Blocked', '#d13438', if(@currentField == '4. Completed', '#107c10', '#f3f2f1'))))"
  }
}
```

---

### 2. [[CF_YearCycle_Formatting|JSON para CF_YearCycle (Año)]]
Muestra el año en una etiqueta sutil con borde.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/sp/v2/column-formatting.schema.json",
  "elmType": "div",
  "txtContent": "@currentField",
  "style": {
    "padding": "2px 8px",
    "border": "1px solid #0078d4",
    "border-radius": "4px",
    "color": "#0078d4",
    "font-weight": "500",
    "display": "inline-block"
  }
}
```

---

### 3. [[CF_CommitteeRole_Formatting|JSON para CF_CommitteeRole (Rol)]]
Etiquetas tipo "pill" con colores suaves por rol.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/sp/v2/column-formatting.schema.json",
  "elmType": "div",
  "txtContent": "@currentField",
  "style": {
    "padding": "4px 8px",
    "border-radius": "8px",
    "background-color": "=if(@currentField == 'Event Lead', '#edebe9', if(@currentField == 'Finance / Treasury', '#fff4ce', if(@currentField == 'Logistics', '#dff6dd', if(@currentField == 'Volunteer Management', '#d1e4fe', '#f3f2f1'))))",
    "color": "#323130",
    "font-size": "12px",
    "font-weight": "500"
  }
}
```
