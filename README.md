# WALK

Walk is a simple python migrations tool for postgres databases. The application is based on 'psycopg2' to run sql commands.

## Installation
Download the this git repository and than inside the root folder of the repository.

```
pip3 install -e .
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
        "dbname=test"
    ],
    "dev": [
        "user=postgres",
        "dbname=dev"
    ],
    "prod": [
        "user=postgres",
        "dbname=prod",
        "password=pw"
    ]
}
```

Passing db config parameters directly to the command. The config attributes in the config file which are also included in the command paramters list will be ignored.

```
"dev": {
    "dbname=test"
}

walk -p dbname=prod -p password=pw -e dev

-> dbname=prod will be taken
```


For more configuration parameters look inside the documentation of the 'psycopg2' connection class. [Here](http://initd.org/psycopg/docs/module.html)

### Migrations sql file

To create a new migrations file inside the migrations folder. Use the following command. The default datbase environment is 'dev'.
```
walk --new test_file_name --env dev
```

### Execute migrations

To execute the migration files for the 'dev' database enviroment use the following command.
```
walk --migrate --env dev
```