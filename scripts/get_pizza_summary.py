import pandas as pd
from sqlalchemy import create_engine
import logging
import time
from ingestion import ingest_db   # first script

logging.basicConfig(
    filename='logs/get_pizza_summary.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

# --------------------------------------------------
# Create Final Analytical Table
# --------------------------------------------------
def create_pizza_summary(conn):
    '''
    Creating final analytical dataset by joining all tables
    '''
    logging.info('Starting SQL query to create pizza table')

    pizza = pd.read_sql_query("""
        SELECT 
            o.order_id,
            pt.name,
            pt.category,
            p.size,
            SUM(od.quantity) AS quantity,
            SUM(p.price * od.quantity) AS revenue,
            o.date,
            o.time
        FROM pizza_types pt 
        JOIN pizzas p ON pt.pizza_type_id = p.pizza_type_id
        JOIN order_details od ON p.pizza_id = od.pizza_id
        JOIN orders o ON od.order_id = o.order_id
        GROUP BY o.order_id, pt.name, pt.category, p.size, o.date, o.time
    """, conn)

    logging.info('Pizza table created successfully')
    return pizza


# --------------------------------------------------
# Data Cleaning
# --------------------------------------------------
def clean_data(pizza):
    logging.info('Cleaning dataset...')

    pizza['date'] = pd.to_datetime(pizza['date'])
    pizza['time'] = pd.to_datetime(pizza['time'], format='%H:%M:%S')

    pizza['month_name'] = pizza['date'].dt.month_name()
    pizza['hour'] = pizza['time'].dt.hour
    pizza['weekday'] = pizza['date'].dt.day_name()

    pizza = pizza.drop(columns=['date', 'time'])

    logging.info('Data cleaned successfully')
    return pizza


# --------------------------------------------------
# Main Pipeline
# --------------------------------------------------
if __name__ == '__main__':
    start = time.time()

    # Create database engine (same DB as ingestion script)
    engine = create_engine("sqlite:///pizza_sales_analysis.db")
    logging.info('Pipeline started')

    pizza_df = create_pizza_summary(engine)
    cleaned_df = clean_data(pizza_df)

    # Save final table using function from first script
    ingest_db(cleaned_df, 'pizza',engine)

    end = time.time()
    total = (end - start) / 60
    logging.info(f'Total time taken: {round(total,2)} minutes')
    logging.info('Pipeline completed successfully')