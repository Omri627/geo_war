# geo_war
uvicorn apis.geo_war_api:app

# db_settings.json
the file `db_settings.json` should reside in root folder in the path `db/db_settings.json`
example of format:
`{
  "host": "127.0.0.1",
  "port": "3306",
  "user": "root",
  "password": "12345",
  "database": "geo_data",
  "pool_size": 12
}`
