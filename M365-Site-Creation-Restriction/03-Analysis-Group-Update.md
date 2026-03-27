---
title: Análisis - Actualización de GroupCreationAllowedGroupId
tags: [analysis, m365, configuracion, graph-api, entra-id]
---

# Análisis: ¿Agregar configuración, recrear o actualizar?

## Contexto del Problema
Al bloquear la creación de grupos en M365 (donde `EnableGroupCreation` es `false`), surge la necesidad de permitir excepciones usando `GroupCreationAllowedGroupId`. La pregunta operativa es cómo inyectar esta modificación en el tenant.

## Análisis de Opciones según Microsoft Graph

En Entra ID y Microsoft Graph, las políticas generadas a través de `groupSettingTemplates` tienen una directiva estricta: **Solo puede existir una (1) instancia de configuración por cada plantilla a nivel tenant.**

Bajo esta regla, evaluamos los escenarios:

### 1. ¿Intentar crear una "nueva" configuración? ❌ (Descartado)
No puedes realizar otra petición `POST` con el mismo `templateId`. Si la configuración "Group.Unified" ya fue creada para bloquear el tenant, Graph API rechazará cualquier intento de crear un duplicado, devolviendo un error de conflicto.

### 2. ¿Eliminar y Recrear? ⚠️ (No Recomendado)
Técnicamente puedes ejecutar un `DELETE` sobre la configuración actual y seguidamente un `POST` con los nuevos valores.
- **El Riesgo Operativo:** En el intervalo entre la eliminación y la nueva creación, el tenant vuelve a sus "valores de fábrica" (donde `EnableGroupCreation` es `true`). Esta ventana de tiempo, por muy breve que sea, permite la creación no auditada de sitios y grupos, rompiendo el esquema de seguridad temporalmente.

### 3. ¿Actualizar (PATCH) la configuración existente? ✅ (Método Recomendado)
Esta es la ruta de diseño nativa de Microsoft. Consiste en realizar una petición `PATCH` apuntando al `id` de la configuración que ya existe.
- **Beneficio Principal:** La política se actualiza "en caliente". Envías el bloque `values` con ambos parámetros (`EnableGroupCreation` en `false` y `GroupCreationAllowedGroupId` con el respectivo ID) y Entra ID absorbe el cambio sin dejar espacios vulnerables.

## Recomendación Final

**Debes Actualizar (PATCH) tu configuración.**

Solo tienes que obtener el `id` de tu configuración actual (con un GET) y enviarle la modificación usando el script del **Paso 5 de PowerShell** o el **Paso 6 de Graph Explorer**. Esto garantiza que tu tenant se mantenga seguro en todo momento y cumple con las mejores prácticas de administración en Microsoft 365.
