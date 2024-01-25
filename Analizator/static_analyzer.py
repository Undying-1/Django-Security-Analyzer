import ast

def static_analyze_code(code):
    # Парсинг исходного кода в абстрактное синтаксическое дерево (AST)
    tree = ast.parse(code)

    # Обход AST для выявления потенциальных уязвимостей
    vulnerabilities = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute):
                attribute_name = node.func.attr.lower()
                if attribute_name == 'eval' or attribute_name.endswith('.py'):
                    vulnerabilities.append(node)

    return vulnerabilities


def get_source_code(file_path):
    with open(file_path, "r") as file:
        source_code = file.read()
    return source_code

def parse_source_code(source_code):
    try:
        ast_tree = ast.parse(source_code)
        return ast_tree
    except SyntaxError as e:
        print(f"Error parsing source code: {e}")
        return None

# Example usage
file_path = "D:/Projects/Django/Code_V2/root/settings.py"
source_code = get_source_code(file_path)

vulnerabilities = static_analyze_code(source_code)

if vulnerabilities:
    print("Найдены потенциальные уязвимости:")
    for vulnerability in vulnerabilities:
        print(vulnerability)
else:
    print("Уязвимостей не обнаружено")