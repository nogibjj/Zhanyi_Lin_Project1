from cmd import PROMPT
import click
import querydb
# build  click commands for query directly
# build a click group
@click.group()
def cli():
#    """A simple CLI to query a SQL database"""
    "do something"


# build  click commands for query directly
@cli.command("WHO_WOULD_WIN")

@click.option('--team1', default="Portugal", help='Number of greetings.')
@click.option('--team2', default="China", help='Number of greetings.')
def cli_query(team1, team2):
    """Input two teams for historical matches"""
    click.echo(team1)
    print(team2)
    querydb.querydb("select * from matches where team1 = ‘%s’ and team2 = ‘%s’” % (team1, team2)")

# build click commands for creating a new empty table
#@cli.command()
#@click.option("--table_name", default="new_table", help="Table name to create")
#@click.option("--columns", default="col1 INT, col2 STRING", help="Columns to create(enter: colname1 coltype1, colname2 coltype2,...etc)")
#def cli_create_table(table_name, columns):
#    """Create a new empty table"""

#    querydb.querydb(f"CREATE TABLE {table_name} ({columns})")
    #return querydb.querydb("SELECT * FROM default.historical_matches_csv LIMIT 2;")

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