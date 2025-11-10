# Project Creation and Modification - Flowchart

A simplified flowchart for creating projects with classes and modifying existing projects by managing classes and images.

---

## Project Creation and Modification Flowchart

```mermaid
flowchart TB
    Start([User Accesses System]) --> MainMenu{Select Operation}
    
    %% PROJECT CREATION
    MainMenu -->|1. Create Project| CreateProject[Create New Project]
    CreateProject --> Auth1[User Authentication]
    Auth1 --> Form1[Enter Project Details<br/>code, title, description,<br/>POC info, location, dates]
    Form1 --> Validate1[Validate Project Data]
    Validate1 --> SaveProject[(Save Project to Database)]
    SaveProject --> ClassOption{Add Classes<br/>to Project?}
    
    ClassOption -->|Yes| ClassSource{Class Source?}
    ClassOption -->|No| ProjectCreated[Project Created<br/>No Classes]
    
    ClassSource -->|Existing Classes| SelectExisting[Select Existing Classes<br/>from Other Projects]
    ClassSource -->|New Classes| CreateNew[Create New Classes]
    
    SelectExisting --> LoadExisting[Load Classes from<br/>Selected Project]
    LoadExisting --> SelectClasses1[Select Classes to Import]
    SelectClasses1 --> ValidateExisting[Validate Selected Classes]
    ValidateExisting --> SaveClasses1[(Save Classes to Database<br/>INSERT INTO class_details)]
    
    CreateNew --> FormNew[Enter New Class Details<br/>class_name, formatted_name,<br/>description]
    FormNew --> ValidateNew[Validate Format<br/>& Check Model Compatibility]
    ValidateNew --> SaveClasses2[(Save Classes to Database<br/>INSERT INTO class_details)]
    
    SaveClasses1 --> ProjectCreated
    SaveClasses2 --> ProjectCreated
    
    %% MODIFY EXISTING PROJECT - ADD CLASS
    MainMenu -->|2. Modify Project| ModifyMenu{Modification<br/>Operation?}
    ModifyMenu -->|Add Class| AddClass[Add Class to Project]
    AddClass --> SelectProject2[Select Existing Project]
    SelectProject2 --> ClassSource2{Class Source?}
    
    ClassSource2 -->|Existing| SelectExisting2[Select Existing Class<br/>from Another Project]
    ClassSource2 -->|New| CreateNew2[Create New Class]
    
    SelectExisting2 --> ImportClass[Import Class to Project]
    ImportClass --> SaveClass1[(Save Class to Database)]
    
    CreateNew2 --> FormNew2[Enter Class Details]
    FormNew2 --> ValidateNew2[Validate & Check Model]
    ValidateNew2 --> SaveClass2[(Save Class to Database)]
    
    SaveClass1 --> ClassAdded[Class Added to Project]
    SaveClass2 --> ClassAdded
    
    %% MODIFY EXISTING PROJECT - REMOVE CLASS
    ModifyMenu -->|Remove Class| RemoveClass[Remove Class from Project]
    RemoveClass --> SelectProject3[Select Existing Project]
    SelectProject3 --> LoadClasses3[Load Project Classes]
    LoadClasses3 --> SelectClass3[Select Class to Remove]
    SelectClass3 --> CheckImages3{Class Has<br/>Images?}
    CheckImages3 -->|Yes| Warning3[Warning: Class has images<br/>Removing class will leave<br/>images unclassified]
    CheckImages3 -->|No| Confirm3[Confirm Removal]
    Warning3 --> Confirm3
    Confirm3 --> UserConfirm3{User Confirms?}
    UserConfirm3 -->|No| Cancel3[Cancel]
    UserConfirm3 -->|Yes| DeleteClass3[(Delete Class from Database<br/>DELETE FROM class_details)]
    DeleteClass3 --> ClassRemoved[Class Removed]
    
    %% MODIFY EXISTING PROJECT - MOVE IMAGES
    ModifyMenu -->|Move Images| MoveImages[Move Images Between Classes]
    MoveImages --> SelectProject4[Select Existing Project]
    SelectProject4 --> LoadImages4[Load Images from Project]
    LoadImages4 --> SelectSourceClass4[Select Source Class]
    SelectSourceClass4 --> DisplayImages4[Display Images in Source Class]
    DisplayImages4 --> SelectImages4[Select Images to Move]
    SelectImages4 --> SelectTargetClass4[Select Target Class<br/>or Create New]
    SelectTargetClass4 --> ConfirmMove4[Confirm Move Operation]
    ConfirmMove4 --> UpdateDB4[(Update Database<br/>UPDATE image_data<br/>SET class_name = target)]
    UpdateDB4 --> MoveFiles4[Move Image Files<br/>Source Folder → Target Folder]
    MoveFiles4 --> ImagesMoved[Images Moved Successfully]
    
    %% MODIFY EXISTING PROJECT - DELETE IMAGES
    ModifyMenu -->|Delete Images| DeleteImages[Delete Images]
    DeleteImages --> SelectProject5[Select Existing Project]
    SelectProject5 --> LoadImages5[Load Images from Project]
    LoadImages5 --> SelectClass5[Select Class]
    SelectClass5 --> DisplayImages5[Display Images in Class]
    DisplayImages5 --> SelectImages5[Select Images to Delete]
    SelectImages5 --> ConfirmDelete5[Confirm Deletion]
    ConfirmDelete5 --> UserConfirm5{User Confirms?}
    UserConfirm5 -->|No| Cancel5[Cancel]
    UserConfirm5 -->|Yes| DeleteDB5[(Delete from Database<br/>DELETE FROM image_data)]
    DeleteDB5 --> DeleteFiles5[Delete Image Files<br/>from File System]
    DeleteFiles5 --> ImagesDeleted[Images Deleted]
    
    ProjectCreated --> Start
    ClassAdded --> Start
    ClassRemoved --> Start
    ImagesMoved --> Start
    ImagesDeleted --> Start
    Cancel3 --> Start
    Cancel5 --> Start
    
    %% Styling - Black and White
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
    style ClassRemoved fill:#ffffff,stroke:#000000,stroke-width:2px
    style ImagesMoved fill:#ffffff,stroke:#000000,stroke-width:2px
    style ImagesDeleted fill:#ffffff,stroke:#000000,stroke-width:2px
    
    style SaveProject fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style SaveClasses1 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style SaveClasses2 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style SaveClass1 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style SaveClass2 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style DeleteClass3 fill:#d3d3d3,stroke:#000000,stroke-width:2px
    style UpdateDB4 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style DeleteDB5 fill:#d3d3d3,stroke:#000000,stroke-width:2px
    
    style Warning3 fill:#e8e8e8,stroke:#000000,stroke-width:2px
    style Cancel3 fill:#f5f5f5,stroke:#000000,stroke-width:2px
    style Cancel5 fill:#f5f5f5,stroke:#000000,stroke-width:2px
```

---

## Operation Explanations

### 1. Create Project with Classes

**What it does**: Creates a new research project and optionally adds classes to it.

**Key Steps**:
1. User must be authenticated
2. Enter project details (code, title, description, POC info, location, dates)
3. System validates all project data
4. Project is saved to database
5. **Optional**: Add classes to the project
   - **Option A - Existing Classes**: Import classes from another existing project
     - Select source project
     - Choose classes to import
     - Classes are copied to the new project
   - **Option B - New Classes**: Create brand new classes
     - Enter class details (name, formatted name, description)
     - System validates format and checks model compatibility
     - New classes are created and added to the project

**Use Case**: 
- Setting up a new research project with a predefined set of classes
- Starting a project similar to an existing one (import classes)
- Creating a project with custom classes specific to your research

---

### 2. Modify Existing Project - Add Class

**What it does**: Adds a new class to an existing project.

**Key Steps**:
1. Select the existing project
2. Choose class source:
   - **Existing Class**: Import from another project
   - **New Class**: Create a new class
3. If importing: Select class from another project and import it
4. If creating: Enter class details, validate, and save
5. Class is added to the project

**Use Case**:
- Adding a newly discovered species to an ongoing project
- Importing a class from another project that's relevant
- Expanding the class list as research progresses

---

### 3. Modify Existing Project - Remove Class

**What it does**: Removes a class definition from an existing project.

**Key Steps**:
1. Select the existing project
2. System loads all classes for that project
3. Select the class to remove
4. System checks if class has images:
   - **If class has images**: Shows warning that removing the class will leave images unclassified
   - **If class has no images**: Proceeds to confirmation
5. User confirms removal
6. Class is deleted from database
7. **Note**: Images remain in the file system but become unclassified

**Use Case**:
- Removing a class that's no longer relevant
- Cleaning up unused classes
- Correcting mistakes in class setup

**Important**: Removing a class does NOT delete images - they remain but need to be reclassified.

---

### 4. Modify Existing Project - Move Images

**What it does**: Moves images from one class to another within the same project.

**Key Steps**:
1. Select the existing project
2. System loads all images from the project
3. Select the source class (class containing images to move)
4. System displays all images in that class
5. User selects specific images to move
6. User selects target class (or creates a new one)
7. User confirms the move operation
8. System updates database: changes image classifications
9. System moves physical image files from source folder to target folder

**Use Case**:
- Correcting misclassified images
- Reorganizing images into more appropriate classes
- Moving images to a newly created class
- Consolidating images from multiple classes

**Important**: This operation updates both the database and file system to maintain consistency.

---

### 5. Modify Existing Project - Delete Images

**What it does**: Permanently removes images from the project.

**Key Steps**:
1. Select the existing project
2. System loads all images from the project
3. Select the class containing images to delete
4. System displays all images in that class
5. User selects specific images to delete
6. User confirms deletion
7. System deletes image records from database
8. System deletes image files from file system

**Use Case**:
- Removing poor quality images
- Deleting images that are not plankton
- Cleaning up duplicate or erroneous images
- Removing images that don't meet quality standards

**Important**: This operation is permanent and cannot be undone. Images are deleted from both database and file system.

---

## Quick Reference

| Operation | Purpose | Reversible? | Affects Images? |
|-----------|---------|-------------|------------------|
| **Create Project** | Start new research project | Yes (can update) | No |
| **Add Class** | Add class to existing project | Yes (can remove) | No |
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

