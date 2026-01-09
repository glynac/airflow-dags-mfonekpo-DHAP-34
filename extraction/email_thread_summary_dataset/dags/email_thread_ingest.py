from airflow.sdk import dag
from pendulum import duration
from file_check import file_check
from validation import validation

@dag(
    dag_id="email_thread_ingest",
    description="DAG to ingest email thread summary dataset",
    schedule="@once",
)
def email_thread_ingest_dag():
    file_check_task = file_check()
    validation_task = validation()



    file_check_task >> validation_task

email_thread_ingest_dag()
