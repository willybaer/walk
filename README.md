# WALK

Walk is a simple python migrations and seeds tool for postgres and mysql databases. The application is based on 'psycopg2' and mysql-connector-python to run sql commands.

## Installation
Download the this git repository and than inside the root folder of the repository.

```
pip install walk
```

Current Version
```
0.3.0
```

### Configuration

Intialize default configurations file 'walk_config.json'.

```
walk --init
```

The default walk_config.json looks like this. 

```json
{
    "test": [
        "user=postgres",
        "dbname=test",
        "adapter=postgresql | mysql"
    ],
    "dev": [
        "user=postgres",
        "dbname=dev",
        "adapter=postgresql | mysql"
    ],
    "prod": [
        "user=postgres",
        "dbname=prod",
        "password=pw",
        "adapter=postgresql | mysql"
    ]
}
```

Passing db config parameters directly to the command. The config attributes in the config file which are also included in the command paramters list will be ignored.

```
"dev": {
    "dbname=test"
}

walk -p dbname=prod -p password=pw -p adapter=postgresql -e prod

-> dbname=prod will be taken
```


For more configuration parameters look inside the documentation of the 'psycopg2' connection class. [Here](http://initd.org/psycopg/docs/module.html)

### Migrations sql file

To create a new migrations file inside the migrations folder. Use the following command. The default database environment is 'dev'.
```
walk --new test_file_name
```

### Execute migrations

To execute the migration files for the 'dev' database enviroment use the following command.
```
walk --migrate --env dev
```

### Seeds sql file

To create a new seed file inside the seeds folder. Use the following command. The default database environment is 'dev'.
```
walk --newseed test_seed_name 
```

### Execute seeds

To execute the seed files for the 'dev' database enviroment use the following command. You can also combine the seeds and the migrations. 
Migrations will be executed first so that seeds can also access current db changes.

```
walk --seed --env dev
```