---
title: Análisis de Mapeo: Lista de Tareas a Scrum Master Workflow
project: Casa Familiar Tooling
it_analyst: Nefi Lopez
date: 2026-03-16
tags: [analysis, scrum, sharepoint, productivity]
---

# 🛠️ Análisis: Transformación de Listas a Framework Scrum

Para gestionar múltiples proyectos como Scrum Master de manera efectiva en Casa Familiar, necesitamos que tu infraestructura de datos (SharePoint/Lists) deje de ser una lista de "Cosas por hacer" y se convierta en una **Herramienta de Flujo de Valor**.

A continuación, la propuesta de mapeo de tus columnas actuales hacia campos de **Agile/Scrum**:

## 📋 Mapeo de Columnas

| Columna Actual | Equivalente Scrum / Agile | Propósito en el Sprint |
| :--- | :--- | :--- |
| **Title** | **User Story / Task Summary** | Título conciso de la unidad de trabajo. |
| **Description** | **Acceptance Criteria (AC)** | Define exactamente cuándo la tarea está "Done". |
| **Category** | **Epic / Feature / Component** | Agrupa por proyecto (Ej: Salesforce, IT Support, FOC). |
| **Progress** | **Workflow State (Board)** | *To Do, In Progress, Review, Done*. |
| **Priority** | **MoSCoW / Business Value** | *Must Have, Should Have...* para priorizar el Sprint Backlog. |
| **Start / Due date** | **Sprint Timeline** | No se suelen usar fechas fijas en Scrum, sino la ventana del Sprint. |
| **Assigned to** | **Owner / Developer** | Miembro del equipo responsable de la ejecución. |
| **Key stakeholders** | **Business Owner** | Quién valida que el requerimiento se cumplió (Gema/Mayra). |
| **Notes** | **Impediments / Blockers** | Espacio para anotar por qué una tarea no se mueve. |

## 🚀 Sugerencias de Optimización para Gestión Multi-Proyecto

### 1. Agregar Columna: "Story Points" (Número)
Indispensable para medir la velocidad del equipo y no saturar el Sprint. No midas en horas, mide en complejidad.

### 2. Agregar Columna: "Sprint" (Choice)
Crea una lista de opciones: `Sprint 1`, `Sprint 2`, `Backlog`. Esto te permitirá filtrar y ver solo lo que estás trabajando en las dos semanas actuales.

### 3. Implementar "Views" (Vistas) en tu herramienta:
- **Vista de Sprint Actual**: Filtrar por `Sprint = Sprint Actual` y agrupar por `Progress`.
- **Vista Ejecutiva (Reporte para Jefe)**: Agrupar por `Category` (Proyecto) y mostrar porcentaje de completitud.
- **Vista de Backlog**: Todo lo que no tiene Sprint asignado, ordenado por prioridad.

### 4. Automatización con Power Automate (Low-Code):
- **Notificación de Bloqueos**: Si una tarea pasa más de 3 días en "In Progress", enviar correo automático al Scrum Master.
- **Reporte Semanal**: Exportar automáticamente a un Excel de resumen los viernes para tu jefe.

## 📝 Conclusión para el IT Analyst
Tu estructura actual es una base sólida, pero al agregar **Story Points** y **Sprint ID**, transformas una lista estática en un motor de gestión ágil. Esto te permitirá decirle a tu jefe exactamente cuánto trabajo es capaz de absorber el departamento de TI por mes.
