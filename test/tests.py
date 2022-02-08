import pytest
from fixtures.pages.data_base import GetDBData


class Test:
    row = []
    col = []
    for i in range(200):
        row.append(str(i))
    for j in range(2, 4 + 1):
        col.append(str(j))

    @pytest.mark.parametrize("row", row)
    @pytest.mark.parametrize("col", col)
    def test(self, randomazied_db, in_memory_session, session, row, col):
        new_param = GetDBData.new_db_data(row, col, in_memory_session)
        old_param = GetDBData.old_db_data(row, col, session)
        assert new_param == old_param, \
            f"\n{old_param[0]}, {old_param[1]}\n " \
            f"expected {new_param[1]}, was {old_param[1]}"
