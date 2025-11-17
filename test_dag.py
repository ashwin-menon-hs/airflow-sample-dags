from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def print_test_message(**kwargs):
    conf = kwargs['dag_run'].conf
    message = conf.get("message", "this is a DAG used for Airflow validation")
    print(f"message from user => {message}")

@dag(
    start_date=datetime(2025, 7, 1),
    schedule_interval=timedelta(minutes=15),
    catchup=False,
    tags=['test_operation', 'git_sync_test'],
)
def test_dag():
    test_dag_operation = PythonOperator(
        task_id='test_dag_operation',
        python_callable=print_test_message
    )
    test_dag_operation
test_dag()
