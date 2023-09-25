import ast, re
import astunparse
import difflib

# Read the code from "action.py"
def auto_correct(source_path,target_path):
    with open(source_path, "r") as f:
        source_code = f.read()

    # Replace variables with dots
    def replace_dotted_vars(match):
        return match.group(1).replace('.', '')
    source_code = re.sub(r'def act', 'def___act___', source_code)

    # 然后进行您的其他替换
    source_code = re.sub(r'\b([\w\.]+)\b', replace_dotted_vars, source_code)
    source_code = re.sub(r'(\w) (\d+)', r'\1\2', source_code)
    source_code = re.sub(r'(\w) (\w)', r'\1\2', source_code)

    # 最后恢复`def act`
    source_code = source_code.replace('def___act___', 'def act')


    # Function to find the closest match in a list
    def closest_match(target, options):
        return difflib.get_close_matches(target, options, n=1, cutoff=0)[0]

    # Extract object variable names before "registry"
    variables_before_registry = []
    for node in ast.walk(ast.parse(source_code)):
        if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) for target in node.targets):
            for target in node.targets:
                if isinstance(target, ast.Name) and 'registry' in ast.dump(node.value):
                    variables_before_registry.append(target.id)

    # Define the valid list
    valid_list = ["robot", "env", "camera"] + variables_before_registry
    valid_func_list = ["donothing", "registry", "MoveBot", "EasyGrasp", "EasyDrop", "cook", "burn", "freeze", "heat", "open", "close", "fold", "unfold", "toggle_on", "toggle_off"]

    # Modify the AST to replace invalid variable names and function names
    class RenameVars(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            for arg in node.args.args:
                if arg.arg not in valid_list:
                    print(f"Changing function parameter '{arg.arg}' to '{closest_match(arg.arg, valid_list)}'")
                    arg.arg = closest_match(arg.arg, valid_list)
            self.generic_visit(node)
            return node

        def visit_Name(self, node):
            self.generic_visit(node)
            if isinstance(node.ctx, ast.Load):
                # Ensure that it's not a function name
                if not (isinstance(node.parent, ast.Call) and node.parent.func is node):
                    if node.id not in valid_list:
                        print(f"Changing variable '{node.id}' to '{closest_match(node.id, valid_list)}'")
                        node.id = closest_match(node.id, valid_list)
                # If it is a function name, validate against valid_func_list
                elif isinstance(node.parent, ast.Call) and node.parent.func is node:
                    if node.id not in valid_func_list:
                        print(f"Changing function name '{node.id}' to '{closest_match(node.id, valid_func_list)}'")
                        node.id = closest_match(node.id, valid_func_list)
            return node

    # Parse the source code
    parsed_code = ast.parse(source_code)

    # Assign parent nodes for each AST node
    for node in ast.walk(parsed_code):
        for child in ast.iter_child_nodes(node):
            child.parent = node

    # Modify the AST
    transformer = RenameVars()
    transformer.visit(parsed_code)

    # Convert the modified AST back to source code
    new_code = astunparse.unparse(parsed_code)

    # Save the modified code to "new.py"
    with open(target_path, "w") as f:
        f.write(new_code)
if __name__=="__main__":
    auto_correct("/shared/liushuai/OmniGibson/evaluation/choiszt.py","/shared/liushuai/OmniGibson/evaluation/choiszt1.py")