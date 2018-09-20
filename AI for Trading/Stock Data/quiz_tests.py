from collections import OrderedDict
import pandas as pd
from tests import project_test, assert_output


@project_test
def test_csv_to_close(fn):
    tickers = ['A', 'B', 'C']
    dates = ['2017-09-22', '2017-09-25', '2017-09-26', '2017-09-27', '2017-09-28']

    fn_inputs = {
        'csv_filepath': 'prices_2017_09_22_2017-09-28.csv',
        'field_names': ['ticker', 'date', 'open', 'high', 'low', 'close', 'volume', 'adj_close', 'adj_volume']}
    fn_correct_outputs = OrderedDict([
        (
            'close',
            pd.DataFrame(
                [
                    [151.89000000, 148.50000000, 59.23000000],
                    [150.55000000, 144.57000000, 60.10000000],
                    [153.14000000, 145.40000000, 58.00000000],
                    [154.23000000, 146.43000000, 58.21000000],
                    [153.28000000, 146.83000000, 56.92000000]],
                dates, tickers))])

    assert_output(fn, fn_inputs, fn_correct_outputs)
