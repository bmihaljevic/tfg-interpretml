import os

def print_tree(startpath, max_depth=5, prefix=''):
    for root, dirs, files in os.walk(startpath):
        depth = root[len(startpath):].count(os.sep)
        if depth >= max_depth:
            continue
        indent = '│   ' * depth
        print(f"{indent}├── {os.path.basename(root)}/")
        for f in files:
            print(f"{indent}│   └── {f}")
        dirs[:] = [d for d in dirs if not d.startswith('.')]  # opcional: ignora carpetas ocultas

print_tree('.', max_depth=5)
