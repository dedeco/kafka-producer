# Kafka producer

## Installing dependencies
```bash
poetry install
```

## Run (localy)
This script will create random messages using Faker 
```bash
poetry run producer PLAINTEXT://127.0.0.1:9092 com.google.sample.purchases
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