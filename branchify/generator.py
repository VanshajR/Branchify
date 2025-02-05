import os
from pathlib import Path

class FolderStructureGenerator:
    DEFAULT_IGNORE = {
        'directories': [
            'node_modules', 'venv', '.git', '__pycache__', 'env',
            '.vscode', '.idea', '.svn', '.DS_Store', '.mypy_cache',
            '.pytest_cache', '__snapshots__'
        ],
        'patterns': [
            '*.pyc', '*.swp', '*.swo', '*.toml', '*.lock', '*.log', '*.yaml',
            '*.rst', '*.ini', '*.cfg', '*.out', '*.env', '*.git', '*.gitignore'
        ],
        'file_limit': 15
    }

    def __init__(self, root_dir=None, ignores=None, includes=None):
        try:
            self.root_dir = Path(root_dir or Path.cwd()).resolve()
            if not self.root_dir.is_dir():
                raise ValueError(f"Invalid directory: {self.root_dir}")
        except Exception as e:
            raise RuntimeError(f"Error initializing generator: {e}")

        self.ignores = ignores or {}
        self.includes = includes or {}
        self.output = []
        self._setup_filters()

    def _setup_filters(self):
        """Sets up the ignored and explicitly included directories and file patterns."""
        self.ignored_dirs = set(self.DEFAULT_IGNORE['directories'])
        self.ignored_patterns = set(self.DEFAULT_IGNORE['patterns'])
        
        # Apply user-provided ignores
        self.ignored_dirs.update(self.ignores.get('directories', []))
        self.ignored_patterns.update(self.ignores.get('patterns', []))
        
        # Apply user-provided includes (removing from ignore lists)
        self.included_dirs = set(self.includes.get('directories', []))
        self.included_patterns = set(self.includes.get('patterns', []))
        
        self.file_limit = self.ignores.get('file_limit', self.DEFAULT_IGNORE['file_limit'])

    def _should_ignore(self, path):
        """Determines if a path should be ignored based on ignore and include rules."""
        if path.is_dir():
            return path.name in self.ignored_dirs and path.name not in self.included_dirs
        if any(path.match(pattern) for pattern in self.ignored_patterns):
            return not any(path.match(pattern) for pattern in self.included_patterns)
        return False

    def _format_files(self, files):
        """Limits file output if necessary."""
        if len(files) <= self.file_limit:
            return files
        return files[:self.file_limit] + ['...']

    def _walk_dir(self, current_dir, prefix='', is_last=False):
        """Recursively walks through directories and builds the folder structure."""
        try:
            entries = sorted(os.scandir(current_dir), key=lambda e: e.name)
            entries = [e for e in entries if not self._should_ignore(Path(e.path))]
        except PermissionError:
            self.output.append(f"{prefix}└── [ACCESS DENIED]")
            return
        except Exception as e:
            self.output.append(f"{prefix}└── [ERROR: {e}]")
            return

        dirs = [e for e in entries if e.is_dir()]
        files = [e.name for e in entries if e.is_file()]
        formatted_files = self._format_files(files)

        total_entries = len(dirs) + len(formatted_files)

        for i, directory in enumerate(dirs):
            path = Path(directory.path)
            is_last_dir = (i == len(dirs) - 1) and not formatted_files  # Last directory and no files after

            connector = '└── ' if is_last_dir else '├── '
            next_prefix = prefix + ('    ' if is_last else '│   ')

            self.output.append(f"{prefix}{connector}{path.name}/")
            self._walk_dir(path, next_prefix, is_last_dir)

        for i, file in enumerate(formatted_files):
            connector = '└── ' if i == len(formatted_files) - 1 else '├── '
            self.output.append(f"{prefix}{connector}{file}")


    def generate(self):
        """Generates and returns the folder structure."""
        self.output = [f"{self.root_dir.name}/"]
        self._walk_dir(self.root_dir)
        return '\n'.join(self.output)
