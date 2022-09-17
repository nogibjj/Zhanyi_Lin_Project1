from cmd import PROMPT
import click
import querydb
# build  click commands for query directly
# build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL database"""


# build  click commands for query directly
@cli.command()
@click.option(
    "--query",
    default="SELECT * FROM default.diabetes LIMIT 2",
    help="SQL query to execute",
)
def cli_query(query):
    """Execute a SQL query"""
    querydb.querydb(query)

# build click commands for creating a new empty table
@cli.command()
@click.option("--table_name", default="new_table", help="Table name to create")
@click.option("--columns", default="col1 INT, col2 STRING", help="Columns to create(enter: colname1 coltype1, colname2 coltype2,...etc)")
def cli_create_table(table_name, columns):
    """Create a new empty table"""

    #querydb.querydb(f"CREATE TABLE {table_name} ({columns})")
    querydb.querydb("SELECT * FROM default.diabetes LIMIT 2")

# build click commands for inserting data into a table
#@cli.command()
#@click.option("--table", required = True, prompt = "Enter table name", help="Table name to insert data")
#@click.option("--data", required = True, prompt = "Enter data" ,help="Data to insert(enter a data list:(col1, col2), (col1, col2)")
#@click.option("--rows",default=3, prompt="Max Number of rows to return",help="Number of rows to return",type=int)
#def cli_insert_data(table, data, rows):
#    pass
#    """Insert data into a table"""
#    insertdb(table, data, rows)




# run the CLI
if __name__ == "__main__":
    cli()