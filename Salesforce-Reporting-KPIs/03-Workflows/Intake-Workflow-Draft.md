---
title: Intake Workflow Draft (As-Is)
tags: [mermaid, workflow, intakes, process]
---

# Current Workflow Drafts

This is a preliminary flowchart. Update this diagram based on your discoveries after interviewing Gema and Mayra.

## General Intake and Reporting Process

```mermaid
graph TD
    A[Client arrives at Casa Familiar] --> B{Service Required?}
    
    B -->|Immigration / Procedures| C[Social Services - Gema]
    B -->|Financial Services| D[FOC - Mayra]
    
    C --> E[Capture Intake in Salesforce - Built by Cloud Care]
    D --> E
    
    E --> F{Dashboard Ready in Salesforce?}
    F -->|Yes| G[Direct KPI Visualization]
    F -->|No| H[Manual Export to Excel/CSV from Salesforce]
    
    H --> I[Manual Data Processing/Cleaning]
    I --> J[Report Generation for Management]
    
    G --> K[Salesforce Dashboard generates Reports/KPIs automatically]
    
    classDef ss fill:#ffe6f2,stroke:#ff66b2,stroke-width:2px;
    classDef foc fill:#e6f2ff,stroke:#66b2ff,stroke-width:2px;
    classDef IT fill:#e6ffe6,stroke:#66ff66,stroke-width:2px;
    classDef pain fill:#ffe6e6,stroke:#ff4c4c,stroke-width:2px,stroke-dasharray: 5 5;
    
    class C ss;
    class D foc;
    class G,K IT;
    class H,I,J pain;
```

### Automation Analysis:
Steps marked with dashed borders (manual export & processing) are our **Pain Points**. As an IT Analyst, this is where we introduce "Low-Code" solutions:
- **Bash/Python scripts** to process exported CSVs.
- **Power Automate** to move data from Salesforce to SharePoint/Excel automatically.
