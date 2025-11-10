# Simple Project and Class Management Flowchart

A simplified flowchart for project creation, class merging, sub-classing, and model retraining.

---

## Simple Flowchart

```mermaid
flowchart TB
    Start([Start]) --> MainMenu{Select Operation}
    
    %% PROJECT CREATION
    MainMenu -->|Create Project| CreateProject[Create Project]
    CreateProject --> EnterDetails[Enter Project Details]
    EnterDetails --> SaveProject[(Save Project)]
    SaveProject --> SelectClasses{Select Classes}
    
    SelectClasses -->|Existing| ImportClasses[Import Classes<br/>from Other Projects]
    SelectClasses -->|New| CreateNewClass[Create New Class<br/>Name + 4+ Images]
    
    ImportClasses --> EditClasses[Edit Classes]
    EditClasses --> ProjectComplete[Project Created]
    
    CreateNewClass --> SaveNewClass[(Save Class)]
    SaveNewClass --> ProjectComplete
    
    ProjectComplete --> RetrainModel[Retrain Model]
    
    %% CLASS MERGING
    MainMenu -->|Merge Classes| MergeClasses[Merge Classes]
    MergeClasses --> SelectProject[Select Project]
    SelectProject --> SelectSources[Select 2+ Source Classes]
    SelectSources --> SelectTarget[Select Target Class]
    SelectTarget --> ConfirmMerge[Confirm Merge]
    ConfirmMerge --> UpdateDB[(Update Database<br/>& Move Files)]
    UpdateDB --> RemoveSources[(Remove Source Classes)]
    RemoveSources --> RetrainModel
    
    %% SUB-CLASSING
    MainMenu -->|Split Class| SplitClass[Split Class]
    SplitClass --> SelectProject
    SelectProject --> SelectSource[Select Source Class]
    SelectSource --> SelectImages[Select Images to Split]
    SelectImages --> EnterNewName[Enter New Class Name]
    EnterNewName --> CheckImages{Has 4+<br/>Images?}
    CheckImages -->|No| AddMoreImages[Add More Images]
    AddMoreImages --> CheckImages
    CheckImages -->|Yes| SaveNewClassSplit[(Save New Class)]
    SaveNewClassSplit --> UpdateDB2[(Update Database<br/>& Move Files)]
    UpdateDB2 --> RetrainModel
    
    %% ADD NEW CLASS
    MainMenu -->|Add Class| AddClass[Add Class]
    AddClass --> SelectProject
    SelectProject --> EnterClass[Enter Class Name]
    EnterClass --> AddImages[Add 4+ Images]
    AddImages --> SaveClass[(Save Class)]
    SaveClass --> RetrainModel
    
    RetrainModel --> End([End])
    
    %% Styling - Simple Black and White
    style Start fill:#ffffff,stroke:#000000,stroke-width:2px
    style MainMenu fill:#f5f5f5,stroke:#000000,stroke-width:2px
    style SelectClasses fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style CheckImages fill:#e8e8e8,stroke:#000000,stroke-width:2px
    
    style ProjectComplete fill:#ffffff,stroke:#000000,stroke-width:2px
    style End fill:#ffffff,stroke:#000000,stroke-width:2px
    
    style SaveProject fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style SaveNewClass fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style SaveNewClassSplit fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style SaveClass fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style UpdateDB fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style UpdateDB2 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style RemoveSources fill:#d3d3d3,stroke:#000000,stroke-width:2px
    
    style RetrainModel fill:#e8e8e8,stroke:#000000,stroke-width:2px
```

---

## Operation Explanations

### 1. Create Project

**What it does**: Creates a new project with classes.

**Steps**:
1. Enter project details → Save project
2. Choose classes:
   - **Import existing** classes from other projects (can edit)
   - **Create new** class (name + minimum 4 images)
3. **Model is retrained** automatically

---

### 2. Merge Classes

**What it does**: Combines multiple classes into one.

**Steps**:
1. Select project
2. Select 2+ source classes
3. Select target class
4. Confirm → System updates database & moves files
5. Source classes removed
6. **Model is retrained** automatically

---

### 3. Split Class

**What it does**: Splits images from one class into a new class with different name.

**Steps**:
1. Select project
2. Select source class
3. Select images to split
4. Enter new class name (different from source)
5. Ensure 4+ images selected (add more if needed)
6. Save new class → System updates database & moves files
7. **Model is retrained** automatically

**Example**: Split "chaetoceros" → Create "chaetoceros_didymus"

---

### 4. Add Class

**What it does**: Adds a new class to existing project.

**Steps**:
1. Select project
2. Enter class name
3. Add minimum 4 images
4. Save class
5. **Model is retrained** automatically

---

## Key Points

### Classes and Model Relationship

**Question**: Do classes need to be in the model to be visible in the web UI?

**Answer**: 
- **Classes can exist in the UI without being in the model**
- Classes not in the model will appear in the web UI but require **manual classification**
- The model will only auto-classify images to classes it was trained on
- **After model retraining**, new classes are incorporated and can be auto-classified

### Model Retraining

**When model is retrained**:
- After project creation with new classes
- After merging classes
- After sub-classing (splitting)
- After adding new classes

**What happens during retraining**:
- New model incorporates all current classes
- Model learns from all available training images
- New classes become available for auto-classification
- Previous model is kept for reference

### Image Requirements

- **Minimum 4 images required** for any new class
- This ensures sufficient training data for model retraining
- Images are automatically organized into proper folder structure

### Automatic File Organization

All operations automatically handle image file storage:
- Files organized by: `project/year/month/class_name/`
- No manual file management needed
- System maintains consistency between database and file system

---

## Quick Reference

| Operation | Minimum Images | Model Retraining | Auto-Classification |
|-----------|----------------|------------------|---------------------|
| **Create Project** | 4 per new class | Yes | After retraining |
| **Merge Classes** | N/A | Yes | After retraining |
| **Sub-Class** | 4 for new class | Yes | After retraining |
| **Add Class** | 4 required | Yes | After retraining |

---

## Workflow Summary

All operations follow this pattern:
- Perform operation → System handles files automatically → **Retrain Model**

**Key Rules**:
- New classes require minimum 4 images
- All file operations are automatic
- Model retraining happens automatically after any change

---

This simplified flowchart focuses on the core operations with automatic file management and model retraining.

