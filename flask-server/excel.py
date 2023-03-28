from datetime import datetime
from typing import Dict, List, Any
from openpyxl import Workbook

def write_to_excel(**kwargs) -> str:
    wb = Workbook(write_only=True)

    for name, results in kwargs.items():
        ws = wb.create_sheet(name)       
        ws.append(list(results[0].keys()))

        for line in results:
            ws.append([str(col) for col in line.values()])

    timestamp = datetime.now().replace(microsecond=0)
    file_name = f'/tmp/caic_questionnaire_{timestamp}.xlsx'
    wb.save(file_name)

    return file_name