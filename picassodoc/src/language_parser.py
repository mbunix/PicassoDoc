import ast
import re

class LanguageParser:
    def __init__(self, code, language):
        self.code = code
        self.language = language

    def parse(self):
        if self.language.lower() == 'python':
            return self.parse_python()
        elif self.language.lower() == 'javascript':
            return self.parse_javascript()
        else:
            raise NotImplementedError(f"Parsing for {self.language} is not implemented yet.")

    def parse_python(self):
        """Parse the Python code to extract classes and functions."""
        tree = ast.parse(self.code)
        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        return {
            "classes": classes,
            "functions": functions
        }

    def parse_javascript(self):
        """Parse the JavaScript code to extract function names."""
        # This simple regex matches function declarations in JavaScript.
        # It doesn't account for ES6 arrow functions or other ways to define functions.
        functions = re.findall(r'function\s+(\w+)\s*\(', self.code)
        # For a more comprehensive solution, consider integrating with a JavaScript parsing library.
        return {
            "functions": functions
        }
