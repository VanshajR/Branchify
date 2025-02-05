import argparse
import subprocess
import sys
from pathlib import Path
from .generator import FolderStructureGenerator

def main():
    parser = argparse.ArgumentParser(description='Generate ASCII folder structure')
    parser.add_argument('-p', '--path', type=str, help='Root directory path (default: current directory)')
    parser.add_argument('-i', '--ignore', nargs='+', help='Directories to ignore')
    parser.add_argument('-o', '--output', type=str, help='Output file path')
    parser.add_argument('--include-dir', nargs='+', help='Directories to explicitly include')
    parser.add_argument('--include-pattern', nargs='+', help='File patterns to explicitly include')
    parser.add_argument('--update', action='store_true', help='Update branchify package')

    args = parser.parse_args()

    if args.update:
        try:
            print("Updating branchify package...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'branchify', '--upgrade'])
            print("Branchify package updated successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error updating branchify package: {e}")
        sys.exit(0)

    try:
        ignores = {'directories': args.ignore} if args.ignore else None
        includes = {
            'directories': args.include_dir or [],
            'patterns': args.include_pattern or []
        }

        generator = FolderStructureGenerator(root_dir=args.path, ignores=ignores, includes=includes)
        structure = generator.generate()

        if args.output:
            try:
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write(structure)
            except Exception as e:
                print(f"Error writing to file: {e}")
        else:
            print(structure)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
