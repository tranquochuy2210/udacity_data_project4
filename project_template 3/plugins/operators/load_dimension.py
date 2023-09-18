from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from helpers import SqlQueries

class LoadDimensionOperator(BaseOperator):
    final_table_sql_switcher  = {
        "user":SqlQueries.user_table_insert,
        "song": SqlQueries.song_table_insert,
        "artist": SqlQueries.artist_table_insert,
        "time": SqlQueries.time_table_insert
    }
    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                table = '',
                redshift_conn_id = '',
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.table = table
        self.redshift_conn_id = redshift_conn_id

    def execute(self, context):
        sql_query = LoadDimensionOperator.final_table_sql_switcher[self.table]
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        redshift.run(sql_query)
