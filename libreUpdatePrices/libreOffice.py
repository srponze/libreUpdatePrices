from typing import List, Any

import ezodf


class LibreOffice:

    def __init__(self, officePath: str):
        self.ods = ezodf.opendoc(officePath)
        self.ods.backup = False
        self.sheet = self.ods.sheets[0]

    def l(self, letter):
        return ord(letter.upper()) - 65

    def saveOds(self):
        self.ods.save()

    def getData(self, start: int, end: int, column: str) -> List[Any]:
        listData = []
        start -= 1
        for row in range(start, end):
            data = self.sheet[row, self.l(column)].value
            if data is not None:
                listData.append(data)
        return listData

    def getDatum(self, row: int, column: str) -> Any:
        row -= 1
        data = self.sheet[row, self.l(column)].value
        return data

    def setData(self, listData: List[Any], start: int, column: str) -> None:
        start -= 1
        for row, data in enumerate(listData, start=start):
            self.sheet[row, self.l(column)].set_value(data)

    def setDatum(self, data: Any, row: int, column: str) -> None:
        row -= 1
        self.sheet[row, self.l(column)].set_value(data)
