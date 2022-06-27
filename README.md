# Kafka producer

## Installing dependencies
```bash
poetry install
```

## Run (localy)
This script will create random messages using Faker with 3 parameters:
* BROKER URL
* TOPIC NAME
* QUANTITY MESSAGES to be produced

```bash
poetry run producer PLAINTEXT://127.0.0.1:9092 com.google.sample.purchases 1000
```

## Purchase message (sample)

```json
{
   "username":"maxwellhannah",
   "currency":"EUR",
   "amount":146107,
   "clean_username":"maxwellhannah"
}
```