xx:q!
# SQL - Introduction

This was my first project in which I began to work with SQL and relational
databases. I began practicing introductory data definition and data
manipulation language, making subqueries, and using functions.

## Usage

* Scripts `3-list_tables.sql` forward take the database to query from as a MySQL
command line argument.

```
$ cat 3-list_tables.sql | mysql -h localhost -u root -p mysql
```

* Tasks 101-103 query from a database provided by Holberton School.

## Tasks

* **List databases**
  * `0-list_databases.sql`: MySQL script that lists all databases.

* **Create a database**
  * `1-create_database.sql`: MySQL script that creates the database
`hbtn_0c_0`.

* **Delete a database**
  * `2-remove_databases.sql`: MySQL script that deletes the database
`hbtn_0c_0`.

* **List tables**
  * `3-list_tables.sql`: MySQL script that lists all tables.

* **First table**
  * `4-first_table.sql`: MySQL script that creates a table `first_table`.
  * Description:
    * `id`: INT
    * `name`: VARCHAR(256)

* **Full description**
  * `5-full_table.sql`: MySQL script that prints the full description of the
table `first_table`.

* **List all in table**
  * `6-list_values.sql`: MySQL script that lists all rows of the table
`first_table`.

* **First add**
  * `7-insert_value.sql`: MySQL script that inserts a new row in the table
`first_table`.
  * Description:
    * `id` = `89`
    * `name` = `Holberton School`

* **Count 89**
  * `8-count_89.sql`: MySQL script that displays the number records with `id =
89` in the table `first_table`.

* **Full creation**
  * `9-full_creation.sql`: MySQL script that creates and fills a table
`second_table`.
  * Description:
    * `id`: INT
    * `name`: VARCHAR(256)
    * `score`: INT
  * Records:
    * `id` = 1, `name` = "John", `score` = 10
    * `id` = 2, `name` = "Alex", `score` = 3
    * `id` = 3, `name` = "Bob", `score` = 14
    * `id` = 4, `name` = "George", `score` = 8

* **List by best**
  * `10-top_score.sql`: MySQL script that lists the `score` and `name` of all
records of the table `second_table` in order of descending `score`.

* **Select the best**
  * `11-best_score.sql`: MySQL script that lists the `score` and `name` of all
records with a `score >= 10` in the table `second_table` in order of descending
score.

* **Cheating is bad**
  * `12-no_cheating.sql`: MySQL script that updates the score of Bob to 10
the table `second_table`.

* **Score too low**
  * `13-change_class.sql`: MySQL script that removes all records with a
`score <= 5` in the table `second_table`.

* **Average**
  * `14-average.sql`: MySQL script that computes the average `score` of all
records in the table `second_table`.

* **Number by score**
  * `15-groups.sql`: MySQL script that lists the `score` and number of records
with the same score in the table `second_table` in order of descending count.

* **Say my name**
  * `16-no_link.sql`: MySQL script that lists the `score` and `name` of all
records in the table `second_table` in order of descending `score`.
  * Does not display rows without a `name` value.

* **Go to UTF8**
  * `100-move_to_utf8.sql`: MySQL script that converts the `hbtn_0c_0`
database to UTF8.

* **Temperatures #0**
  * `101-avg_temperatures.sql`: MySQL script that displays the average
temperature (Fahrenheit) by city in descending order.

* **Temperatures #1**
  * `102-top_city.sql`: MySQL script that displays the three cities with the
highest average temperature from July to August in descending order.

* **Temperature #2**
  * `103-max_state.sql`: MySQL script that displays the max temperature of each
state in order of state name.
