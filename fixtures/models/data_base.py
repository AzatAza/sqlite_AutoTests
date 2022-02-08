import pytest


class TableSize:
    def __init__(self, row=None, col=None):
        self.row = row
        self.col = col
        self.table_size = self.table_size

    @pytest.mark.usefixtures(session="session")
    def table_size(self, session):
        session.execute("SELECT count() FROM Ships")
        rows_amount = session.fetchone()[0]
        session.execute("SELECT count() FROM pragma_table_info('Ships')")
        columns_amount = session.fetchone()[0]
        row = [0]
        col = [0]
        for i in range(1, rows_amount):
            row.append(str(i))
        for j in range(2, columns_amount + 1):
            col.append(str(j))
        return TableSize(row=rows_amount, col=columns_amount)
