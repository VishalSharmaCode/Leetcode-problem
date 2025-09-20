class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.cols = 26  # 'A' to 'Z'
        # use dictionary {(row, col): value}
        self.cells = {}

    def _parse_cell(self, cell: str):
        """Convert cell like 'A1' -> (row, col) zero-indexed"""
        col = ord(cell[0]) - ord('A')  # map A->0, B->1 ...
        row = int(cell[1:]) - 1        # make 0-indexed
        return (row, col)

    def setCell(self, cell: str, value: int) -> None:
        row, col = self._parse_cell(cell)
        self.cells[(row, col)] = value

    def resetCell(self, cell: str) -> None:
        row, col = self._parse_cell(cell)
        if (row, col) in self.cells:
            del self.cells[(row, col)]

    def _get_cell_value(self, token: str) -> int:
        """Return value for a cell or integer literal"""
        if token[0].isalpha():  # It's a cell reference
            row, col = self._parse_cell(token)
            return self.cells.get((row, col), 0)
        else:  # It's a literal number
            return int(token)

    def getValue(self, formula: str) -> int:
        # Formula format: "=X+Y"
        parts = formula[1:].split("+")  # remove '='
        return sum(self._get_cell_value(token) for token in parts)