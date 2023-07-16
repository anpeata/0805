from moz_sql_parser import parse

# Define an example SQL query
sql_query = "SELECT * FROM users WHERE age > 18"

# Parse the SQL query and convert it to a JSON-like structure
parsed_query = parse(sql_query)

# Print the parsed query
print(parsed_query)

# Access the components of the parsed query
select_clause = parsed_query['select']
from_clause = parsed_query['from']
where_clause = parsed_query['where']

# Print the components of the parsed query
print(select_clause)
print(from_clause)
print(where_clause)