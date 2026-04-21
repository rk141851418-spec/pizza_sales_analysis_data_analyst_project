import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename = 'logs/employee_info.db.log',
    level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    filemode = 'a'
)

engine = create_engine('sqlite:/// pizza_sales_analysis.db')

def ingest_db(df,table_name,engine):
    df.to_sql(table_name,con = engine,if_exists = 'replace',index = False)
def load_raw_data():
    for file in os.listdir('data'):
        start = time.time()
        if '.csv' in file:
             df = pd.read_csv('data/'+file)
             logging.info(f' ingesting:{file} in db')
             ingest_db(df,file[:-4],engine)
    end = time.time()
    total_time = (end - start)/60
    logging.info('ingestion complete')
    logging.info(f'\n total time taken :{total_time}minutes')

if __name__ == '__main__':
    load_raw_data()