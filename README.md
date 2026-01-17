# Maya Python Collection Scripts

A curated collection of Python scripts for Autodesk Maya to streamline common 3D workflows and automate repetitive tasks.

## 📋 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Scripts](#scripts)
  - [Utilities](#utilities)
  - [Export Tools](#export-tools)
  - [Material Creation](#material-creation)
  - [Fun Scripts](#fun-scripts)
- [Installation](#installation)
- [Usage](#usage)
- [Author](#author)

## 🎯 Overview

This repository contains a collection of Maya Python scripts I've developed and used in my Maya workflow. These scripts help with various tasks including object management, batch exporting, material creation, and more.

## 📁 Repository Structure

```
maya-python-collection-scripts/
├── scripts/
│   ├── utilities/          # Utility scripts for Maya scene management
│   ├── export/             # Export and batch processing tools
│   ├── materials/          # Material creation and management
│   └── fun/                # Entertainment scripts
├── assets/                 # Media assets for scripts
└── README.md
```

## 🛠️ Scripts

### Utilities

#### `delete_hidden.py`
Deletes all hidden objects in the Maya outliner with a single command.

**Features:**
- Removes all invisible transform nodes
- Cleans up hidden geometry quickly
- Simple one-click execution

**Usage:**
1. Load script into Maya Script Editor (Python tab)
2. Execute the script
3. All hidden objects will be deleted

**Location:** `scripts/utilities/delete_hidden.py`

---

#### `character_caps.py`
Converts object names from lowercase to uppercase for selected objects.

**Features:**
- Batch rename selected objects
- Converts all characters to uppercase
- Prints before/after names for verification

**Usage:**
1. Load script into Maya Script Editor (Python tab)
2. Select objects in the outliner
3. Execute the script
4. All selected objects will be renamed to uppercase

**Location:** `scripts/utilities/character_caps.py`

---

### Export Tools

#### `export_selection_multiple.py`
Exports each selected object to its own Maya ASCII (.ma) file with an intuitive UI.

**Features:**
- User-friendly interface with file browser
- Batch export multiple objects
- Each object exports with its own name
- File path selection with browse button

**Usage:**
1. Load script into Maya Script Editor (Python tab)
2. Select all objects you want to export
3. Execute the script
4. UI will appear - choose export path
5. Click "Export all selected"
6. Each object will be saved as a separate .ma file

**Location:** `scripts/export/export_selection_multiple.py`

---

### Material Creation

#### `create_material.py`
Creates dual-shader materials optimized for both playblast and Arnold rendering workflows.

**Features:**
- Creates Blinn shader (pb_prefix) for fast playblast previews
- Creates aiStandardSurface shader (s_prefix) for Arnold rendering
- Automatically connects both to a shading group
- Clean UI with keyboard support (Numpad Enter)

**Workflow:**
- `pb_` prefix = Blinn material (playblast)
- `s_` prefix = aiStandardSurface material (Arnold)
- Both materials connected to the same shading group

**Usage:**
1. Load script into Maya Script Editor (Python tab)
2. Execute the script
3. UI window will appear
4. Type material name
5. Press "Apply" or hit Numpad Enter
6. Materials will be created and connected automatically

**Location:** `scripts/materials/create_material.py`

---

### Fun Scripts

#### `uiiaiuiiai.py`
A fun prank script that displays an image preview with a surprise video.

**Features:**
- UI with image preview
- Plays video when clicking "Close"
- Customizable image and video paths

**Note:** Update the paths in the script to point to your own image and video files.

**Location:** `scripts/fun/uiiaiuiiai.py`

---

## 📥 Installation

1. Clone this repository:
```bash
git clone https://github.com/muhammadli3d/maya-python-collection-scripts.git
```

2. Navigate to the scripts directory and choose the script you need.

## 🚀 Usage

### General Instructions

**For all scripts:**

1. Open Autodesk Maya
2. Open the Script Editor (Windows > General Editors > Script Editor)
3. Click the Python tab
4. Open and copy the desired script content
5. Paste into the Script Editor
6. Execute the script (Ctrl+Enter or press the Execute button)

**Tip:** You can save frequently used scripts to your Maya shelf for quick access:
- Select the script code in the Script Editor
- Middle-mouse drag to your shelf
- Click the shelf button anytime to run the script

## 👤 Author

**Muhammad Li3D**
- GitHub: [@muhammadli3d](https://github.com/muhammadli3d)

## 📝 License

Feel free to use and modify these scripts for your own projects.

---

**Note:** These scripts were developed for personal use in Maya production workflows. Always test scripts in a safe environment before using them on production files.
