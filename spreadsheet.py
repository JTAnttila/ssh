
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
        
        # Check if the value is a cell reference starting with "="
        if value.startswith("="):
            referenced_cell = value[1:]
            return self.evaluate(referenced_cell, visited)
        
        # If none of the above conditions are met, return #Error
        return '#Error'

