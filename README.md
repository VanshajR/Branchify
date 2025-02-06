
# Branchify Documentation 📂  

**Branchify** generates an ASCII folder structure from any directory. Works for Python>=3.8

## Features  
✅ Command-line Interface (CLI) & Python API  
✅ Smart Ignoring of common directories and file types  
✅ Explicit Inclusions and Exclusions for directories or file patterns  
✅ Configurable File Limit (Depth) of the tree

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

### 3️⃣ Ignore Specific Directories and Files
```sh
branchify --ignore node_modules venv --ignore-patterns '*.wav'
```

### 4️⃣ Explicitly Include Some Directories or Files
```sh
branchify --include-dir logs --include-pattern '*.json'
```

### 5️⃣ Set a Custom File Limit
```sh
branchify --depth 5
```

### 6️⃣ Save Output to a File
```sh
branchify --output structure.txt
```

### 7️⃣ Update Branchify to the latest version
```sh
branchify --update
```

---

## Python API Usage

```python
from branchify.generator import FolderStructureGenerator

# Define customization options for the generator
ignores = {
    'directories': ['node_modules', 'venv', '.git', '__pycache__'],  # Custom directories to ignore
    'ignore_patterns': ['*.log', '*.tmp', '*.bak'],  # Custom file patterns to ignore
}

includes = {
    'directories': ['src', 'assets'],  # Directories to explicitly include
    'patterns': ['*.py', '*.js'],  # File patterns to explicitly include
}

# Custom file limit
file_limit = 25

# Initialize the FolderStructureGenerator with custom parameters
generator = FolderStructureGenerator(
    root_dir="/path/to/root",  # Set the root directory to start from
    ignores=ignores,  # Pass the custom ignores
    includes=includes,  # Pass the custom includes
)

# Override the default file limit
generator.file_limit = file_limit

# Generate and display the folder structure
print(generator.generate())

# Output the generated folder structure
print("Generated Folder Structure:")
print(structure)
```
---
## Default Ignored Files and Directories

The `FolderStructureGenerator` class comes with predefined settings that ignore certain files and directories when generating the folder structure. These settings can be customized by passing specific arguments during instantiation, but the default ignores are as follows:

### Ignored Directories

The following directories are ignored by default:

- **`node_modules`**: A directory commonly found in JavaScript projects, containing installed packages.
- **`venv`**: A directory for Python virtual environments, which typically contains installed dependencies.
- **`.git`**: The Git version control directory, containing internal Git configurations and histories.
- **`__pycache__`**: A directory that stores Python bytecode files.
- **`env`**: Another directory often used for Python virtual environments.
- **`.vscode`**: The Visual Studio Code workspace settings folder.
- **`.idea`**: The directory used by JetBrains IDEs (such as IntelliJ IDEA, PyCharm) for project-specific settings.
- **`.svn`**: The Subversion version control directory, used for managing source code versions.
- **`.DS_Store`**: A system file used by macOS to store folder-specific settings, typically hidden.
- **`.mypy_cache`**: A directory used by MyPy (a static type checker for Python) to store cached information.
- **`.pytest_cache`**: A directory used by pytest to cache results of tests to speed up repeated test runs.
- **`__snapshots__`**: A directory often used for storing test snapshots in JavaScript or other testing frameworks.

### Ignored File Patterns

The following file patterns are ignored by default:

- **`*.pyc`**: Compiled Python files.
- **`*.swp` and `*.swo`**: Temporary swap files created by text editors (like Vim).
- **`*.toml`**: TOML files, typically used for configuration (e.g., `pyproject.toml`).
- **`*.lock`**: Lock files, used by package managers (e.g., `package-lock.json`, `Pipfile.lock`).
- **`*.log`**: Log files, often generated for debugging or runtime information.
- **`*.yaml`**: YAML files, often used for configuration (e.g., `docker-compose.yaml`).
- **`*.rst`**: ReStructuredText files, used for documentation.
- **`*.ini`**: Configuration files using the INI format.
- **`*.cfg`**: Another configuration file type.
- **`*.out`**: Output files, often generated during builds or testing.
- **`*.git` and `*.gitignore`**: Git-related files and directories used for version control management.

### `file_limit` and Its Functionality

The `file_limit` is a setting within the `FolderStructureGenerator` class that restricts the number of files shown in the generated folder structure for a given directory. It can be modified within the cli with the `--depth` flag.

By default, the `file_limit` is set to **15**. This means that if a directory contains more than 15 files, only the first 15 files will be displayed, and the rest will be represented by an ellipsis (`...`) at the end of the list.

This limit is applied as follows:
- If a directory contains 15 or fewer files, all files will be shown.
- If a directory contains more than 15 files, only the first 15 will be displayed, and the rest will be omitted to keep the output concise.

---
## Sample Usage

![Branchify Demo](https://res.cloudinary.com/dnciaoigz/image/upload/v1738837524/Branchify_Demo_fu1byp.gif)

---

## Example Output
```txt
Pneumonia_Detection/
├── .devcontainer/
│   └── devcontainer.json
├── app/
│   └── app.py
├── images_test/
│   ├── IM-0368-0001.jpeg
│   ├── NORMAL2-IM-0401-0001.jpeg
│   ├── NORMAL2-IM-0775-0001.jpeg
│   ├── NORMAL2-IM-1319-0001.jpeg
│   ├── NORMAL2-IM-1326-0001.jpeg
│   ├── person1712_bacteria_4529.jpeg
│   ├── person1729_bacteria_4557.jpeg
│   ├── person466_bacteria_1987.jpeg
│   ├── person630_bacteria_2512.jpeg
│   └── person896_virus_1548.jpeg
├── models/
│   ├── cnn_model.h5
│   ├── logistic_regression_model.pkl
│   └── pca_transformer.pkl
├── notebooks/
│   └── pneumonia_detection.ipynb
├── LICENSE
├── README.md
└── requirements.txt
```

---

## LICENSE

This project is licensed under the **BSD License**

---

## Contributing
If you'd like to contribute to Branchify, please open an issue or a pull request at the [repository](https://github.com/VanshajR/Branchify), and if you find it helpful, do consider starring the repository!
