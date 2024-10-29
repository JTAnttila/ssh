
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> int | str:
        value = self.get(cell)
        if value.isdigit():
            return int(value)
        try:
            float(value)
            return '#Error'
        except ValueError:
            if value.startswith("'") and value.endswith("'"):
                return value[1:-1]
            elif value.startswith("='"):
                content = value[2:]
                if content.isdigit():
                    return int(content)
                return content
            return '#Error'

