
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str, visited=None) -> int | str:
        if visited is None:
            visited = set()
        
        if cell in visited:
            return '#Circular'
        
        visited.add(cell)
        value = self.get(cell)
        
        # Check if the value is a valid integer
        if value.isdigit():
            return int(value)
        
        # Check if the value is a valid float, which should return #Error
        try:
            float(value)
            return '#Error'
        except ValueError:
            pass
        
        # Check if the value is a valid string enclosed in single quotes
        if value.startswith("'") and value.endswith("'"):
            return value[1:-1]
        
        # Check if the value is a formula starting with "='"
        if value.startswith("='"):
            content = value[2:]
            # Check if the content is a valid integer
            if content.isdigit():
                return int(content)
            # If the content is a valid string enclosed in single quotes
            if content.startswith("'") and content.endswith("'"):
                return content[1:-1]
            # If neither, return #Error
            return '#Error'
        
        # Check if the value is a cell reference or formula starting with "="
        if value.startswith("="):
            expression = value[1:]
            # If it's a cell reference
            if expression in self._cells:
                return self.evaluate(expression, visited)
            
            # Replace cell references in the expression with their evaluated values
            for ref in self._cells:
                if ref in expression:
                    ref_value = self.evaluate(ref, visited)
                    if isinstance(ref_value, int):
                        expression = expression.replace(ref, str(ref_value))
                    else:
                        return '#Error'
            
            # Check if it's a simple arithmetic expression
            try:
                result = eval(expression, {"__builtins__": {}})
                if isinstance(result, int):
                    return result
                else:
                    return '#Error'
            except:
                return '#Error'
        
        # If none of the above conditions are met, return #Error
        return '#Error'

