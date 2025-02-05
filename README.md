
# Branchify 🌳📂  

**TreeViz** , which stands for Tree Visualizer, generates an ASCII folder structure from any directory. Works for Python>=3.4

## Features  
✅ Command-line Interface (CLI) & Python API  
✅ Smart Ignoring of common directories and file types  
✅ Explicit Inclusions for directories or file patterns  
✅ Configurable File Limit  

---

## Installation  
```sh
pip install branchify
```

---

## CLI Usage  

### 1️⃣ Generate a Folder Structure (Default)
```sh
branchify
```

### 2️⃣ Specify a Directory
```sh
branchify --path my_project
```

### 3️⃣ Ignore Specific Directories
```sh
branchify --ignore node_modules venv
```

### 4️⃣ Explicitly Include Some Directories or Files
```sh
branchify --include-dir logs --include-pattern '*.json'
```

### 5️⃣ Set a Custom File Limit
```sh
branchify --file-limit 5
```

### 6️⃣ Save Output to a File
```sh
branchify --output structure.txt
```

---

## Python API Usage
```python
from branchify import FolderStructureGenerator

generator = FolderStructureGenerator(root_dir="my_project", file_limit=5)
print(generator.generate())
```

With **custom ignores**:
```python
ignores = {"directories": ["build"], "patterns": ["*.log"]}
generator = FolderStructureGenerator(root_dir="my_project", ignores=ignores, file_limit=3)
print(generator.generate())
```

---

## Example Output
```txt
sample_project/
├── src/
│   ├── main.py
│   ├── utils.py
│   ├── config/
│   │   ├── settings.json
│   │   ├── defaults.yml
│   ├── __init__.py
├── README.md
└── tests/
    ├── test_main.py
    ├── test_utils.py
    └── ...
```

---

## LICENSE

This project is licensed under the **BSD 3-Clause License**

---

## Contributing
If you'd like to contribute to TreeViz, please open an issue or a pull request at the [repository](https://github.com/VanshajR/TreeViz)
