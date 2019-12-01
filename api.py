import requests
import pandas as pd


url_tables = 'http://opendata.1212.mn/api/Itms?type=json'
url_data = 'http://opendata.1212.mn/api/Data?type=json'
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}


def get_tables(out_type='df', header=header):
    """
    Get a list of tables available
    """
    response = requests.get(url_tables, header)

    if response.status_code == 200:
        print('Success!')
        tables_json = response.json()
        tables_json = [table for table in tables_json if table is not None]
        tables_df = pd.DataFrame(tables_json)

        if out_type == 'df':
            return tables_df
        elif out_type == 'json':
            return tables_json
        else:
            return None
    else:
        print('Not Found.')
    
    
def search_table(df, search_string):
    """
    Search tables
    """
    columns = ['tbl_id', 'tbl_eng_nm', 'tbl_nm']
    idx_eng = df[df['tbl_eng_nm'].str.contains(search_string)].index
    idx_mng = df[df['tbl_nm'].str.contains(search_string)].index
    
    
    idx = set(idx_eng.to_list() + idx_mng.to_list())
    
    results_df = df.loc[list(idx), columns]
    print('--------------------\nSearch results: ')
    for idx, row in enumerate(results_df):
        print('\n', results_df.iloc[idx, :])


def get_data(table_id = 'DT_NSO_0500_004V1'):
    params = {'tbl_id': 'DT_NSO_0500_004V1'}
    response = requests.post(url_data, params, header)

    if response.status_code == 200:
        tables_json = response.json()


