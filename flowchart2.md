# Project Creation and Modification - Flowchart

A simplified flowchart for creating projects with classes and modifying existing projects by managing classes and images.

---

## Project Creation and Modification Flowchart

```mermaid
flowchart TB
    Start([User Accesses System]) --> MainMenu{Select Operation}
    
    %% PROJECT CREATION
    MainMenu -->|Create Project| CreateProject[Create New Project]
    CreateProject --> Auth1[User Authentication]
    Auth1 --> Form1[Enter Project Details]
    Form1 --> Validate1[Validate Data]
    Validate1 --> SaveProject[(Save Project)]
    SaveProject --> ClassOption{Add Classes?}
    
    ClassOption -->|Yes| ClassSource{Class Source?}
    ClassOption -->|No| ProjectCreated[Project Created]
    
    ClassSource -->|Existing| SelectExisting[Select from Other Projects]
    ClassSource -->|New| CreateNew[Create New Classes]
    
    SelectExisting --> SelectClasses1[Select Classes to Import]
    SelectClasses1 --> SaveClasses1[(Save Classes)]
    
    CreateNew --> FormNew[Enter Class Details]
    FormNew --> ValidateNew[Validate Format]
    ValidateNew --> SaveClasses2[(Save Classes)]
    
    SaveClasses1 --> ProjectCreated
    SaveClasses2 --> ProjectCreated
    
    %% MODIFY EXISTING PROJECT - ADD CLASS
    MainMenu -->|Modify Project| ModifyMenu{Operation?}
    ModifyMenu -->|Add Class| AddClass[Add Class]
    AddClass --> SelectProject2[Select Project]
    SelectProject2 --> ClassSource2{Class Source?}
    
    ClassSource2 -->|Existing| SelectExisting2[Select from Another Project]
    ClassSource2 -->|New| CreateNew2[Create New Class]
    
    SelectExisting2 --> SaveClass1[(Save Class)]
    CreateNew2 --> FormNew2[Enter Details]
    FormNew2 --> SaveClass2[(Save Class)]
    
    SaveClass1 --> ClassAdded[Class Added]
    SaveClass2 --> ClassAdded
    
    %% MODIFY EXISTING PROJECT - ADD IMAGES TO NEW CLASS
    ModifyMenu -->|Add Images to New Class| AddImagesNewClass[Add Images to New Class]
    AddImagesNewClass --> SelectProject6[Select Project]
    SelectProject6 --> CreateNewClass6[Create New Class]
    CreateNewClass6 --> SaveNewClass6[(Save New Class)]
    SaveNewClass6 --> LoadImages6[Load Unclassified Images]
    LoadImages6 --> SelectImages6[Select Images]
    SelectImages6 --> ConfirmAdd6[Confirm]
    ConfirmAdd6 --> SaveImages6[(Save Images to Class)]
    SaveImages6 --> MoveFiles6[Move Image Files]
    MoveFiles6 --> ImagesAdded[Images Added to New Class]
    
    %% MODIFY EXISTING PROJECT - REMOVE CLASS
    ModifyMenu -->|Remove Class| RemoveClass[Remove Class]
    RemoveClass --> SelectProject3[Select Project]
    SelectProject3 --> SelectClass3[Select Class]
    SelectClass3 --> CheckImages3{Has Images?}
    CheckImages3 -->|Yes| Warning3[Show Warning]
    CheckImages3 -->|No| Confirm3[Confirm]
    Warning3 --> Confirm3
    Confirm3 --> UserConfirm3{Confirm?}
    UserConfirm3 -->|No| Cancel3[Cancel]
    UserConfirm3 -->|Yes| DeleteClass3[(Remove Class)]
    DeleteClass3 --> ClassRemoved[Class Removed]
    
    %% MODIFY EXISTING PROJECT - MOVE IMAGES
    ModifyMenu -->|Move Images| MoveImages[Move Images]
    MoveImages --> SelectProject4[Select Project]
    SelectProject4 --> SelectSourceClass4[Select Source Class]
    SelectSourceClass4 --> DisplayImages4[Display Images]
    DisplayImages4 --> SelectImages4[Select Images]
    SelectImages4 --> SelectTargetClass4[Select Target Class]
    SelectTargetClass4 --> ConfirmMove4[Confirm]
    ConfirmMove4 --> UpdateImages4[(Update Classifications)]
    UpdateImages4 --> MoveFiles4[Move Files]
    MoveFiles4 --> ImagesMoved[Images Moved]
    
    %% MODIFY EXISTING PROJECT - DELETE IMAGES
    ModifyMenu -->|Delete Images| DeleteImages[Delete Images]
    DeleteImages --> SelectProject5[Select Project]
    SelectProject5 --> SelectClass5[Select Class]
    SelectClass5 --> DisplayImages5[Display Images]
    DisplayImages5 --> SelectImages5[Select Images]
    SelectImages5 --> ConfirmDelete5[Confirm]
    ConfirmDelete5 --> UserConfirm5{Confirm?}
    UserConfirm5 -->|No| Cancel5[Cancel]
    UserConfirm5 -->|Yes| DeleteImages5[(Delete Images)]
    DeleteImages5 --> ImagesDeleted[Images Deleted]
    
    ProjectCreated --> Start
    ClassAdded --> Start
    ImagesAdded --> Start
    ClassRemoved --> Start
    ImagesMoved --> Start
    ImagesDeleted --> Start
    Cancel3 --> Start
    Cancel5 --> Start
    
    %% Styling - Simple Black and White
    style Start fill:#ffffff,stroke:#000000,stroke-width:2px
    style MainMenu fill:#f5f5f5,stroke:#000000,stroke-width:2px
    style ModifyMenu fill:#f5f5f5,stroke:#000000,stroke-width:2px
    style ClassOption fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style ClassSource fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style ClassSource2 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style CheckImages3 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style UserConfirm3 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style UserConfirm5 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    
    style ProjectCreated fill:#ffffff,stroke:#000000,stroke-width:2px
    style ClassAdded fill:#ffffff,stroke:#000000,stroke-width:2px
    style ImagesAdded fill:#ffffff,stroke:#000000,stroke-width:2px
    style ClassRemoved fill:#ffffff,stroke:#000000,stroke-width:2px
    style ImagesMoved fill:#ffffff,stroke:#000000,stroke-width:2px
    style ImagesDeleted fill:#ffffff,stroke:#000000,stroke-width:2px
    
    style SaveProject fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style SaveClasses1 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style SaveClasses2 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style SaveClass1 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style SaveClass2 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style SaveNewClass6 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style SaveImages6 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style DeleteClass3 fill:#d3d3d3,stroke:#000000,stroke-width:2px
    style UpdateImages4 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style DeleteImages5 fill:#d3d3d3,stroke:#000000,stroke-width:2px
    
    style Warning3 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style Cancel3 fill:#f5f5f5,stroke:#000000,stroke-width:2px
    style Cancel5 fill:#f5f5f5,stroke:#000000,stroke-width:2px
```

---

## Operation Explanations

### 1. Create Project with Classes

**What it does**: Creates a new research project and optionally adds classes to it.

**Key Steps**:
1. User authentication required
2. Enter project details
3. System validates data
4. Project is saved
5. **Optional**: Add classes to the project
   - **Existing Classes**: Import from another project
   - **New Classes**: Create new classes with details

**Use Case**: Setting up a new research project with classes.

---

### 2. Modify Existing Project - Add Class

**What it does**: Adds a new class to an existing project.

**Key Steps**:
1. Select the project
2. Choose to import existing class or create new class
3. If importing: Select class from another project
4. If creating: Enter class details
5. Class is saved to project

**Use Case**: Adding new species or categories to an ongoing project.

---

### 3. Modify Existing Project - Add Images to New Class

**What it does**: Creates a new class and adds selected images to it.

**Key Steps**:
1. Select the project
2. Create a new class with details
3. New class is saved
4. System loads unclassified images
5. User selects images to add to the new class
6. User confirms
7. Images are saved to the new class
8. Image files are moved to the new class folder

**Use Case**: 
- Creating a new class for images that don't fit existing categories
- Organizing unclassified images into a new category
- Adding a newly discovered species with existing images

---

### 4. Modify Existing Project - Remove Class

**What it does**: Removes a class definition from an existing project.

**Key Steps**:
1. Select the project
2. Select the class to remove
3. System checks if class has images
4. If images exist, warning is shown
5. User confirms removal
6. Class is removed
7. **Note**: Images remain but become unclassified

**Use Case**: Removing classes that are no longer relevant or needed.

**Important**: Removing a class does NOT delete images - they remain but need to be reclassified.

---

### 5. Modify Existing Project - Move Images

**What it does**: Moves images from one class to another within the same project.

**Key Steps**:
1. Select the project
2. Select source class
3. Display images in source class
4. Select images to move
5. Select target class
6. Confirm move operation
7. Update image classifications
8. Move image files to target folder

**Use Case**: Correcting misclassified images or reorganizing images into different classes.

---

### 6. Modify Existing Project - Delete Images

**What it does**: Permanently removes images from the project.

**Key Steps**:
1. Select the project
2. Select the class
3. Display images in class
4. Select images to delete
5. Confirm deletion
6. Images are deleted

**Use Case**: Removing poor quality images or images that don't meet standards.

**Important**: This operation is permanent and cannot be undone.

---

## Quick Reference

| Operation | Purpose | Reversible? | Affects Images? |
|-----------|---------|-------------|------------------|
| **Create Project** | Start new research project | Yes (can update) | No |
| **Add Class** | Add class to existing project | Yes (can remove) | No |
| **Add Images to New Class** | Create class and add images | Yes (can remove) | Yes (moves files) |
| **Remove Class** | Remove class from project | No | No (but images need reclassification) |
| **Move Images** | Reclassify images to different class | Yes (can move back) | Yes (moves files) |
| **Delete Images** | Permanently remove images | No | Yes (deletes files) |

---

## Common Workflows

### Workflow 1: Setting Up a New Project
1. **Create Project** with project details
2. **Add Classes** - either import from existing project or create new ones
3. Start classifying images

### Workflow 2: Correcting Classifications
1. **Move Images** from incorrect class to correct class
2. If needed, **Add Class** for new category
3. If class becomes empty, **Remove Class**

### Workflow 3: Cleaning Up Project
1. **Delete Images** that are poor quality or not relevant
2. **Move Images** to consolidate similar classes
3. **Remove Class** for classes that are no longer needed

### Workflow 4: Expanding Project
1. **Add Class** for newly discovered species
2. **Move Images** from unclassified or other classes to new class
3. Continue classification work

---

## Important Notes

### Class Management
- Classes are project-specific - same class name can exist in different projects
- Removing a class does NOT delete images - only removes the class definition
- Images in a removed class become unclassified and need to be reclassified

### Image Management
- Moving images updates both database and file system
- Deleting images permanently removes them from both database and file system
- Always confirm before deleting images - this cannot be undone

### Data Integrity
- All operations maintain consistency between database and file system
- File organization: `project/year/month/class_name/image.png`
- Operations are logged for audit purposes

---

This flowchart provides a clear overview of project creation and modification operations for managing classes and images.

