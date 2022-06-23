# Kafka producer

## Run (localy)

```bash
python main.py PLAINTEXT://127.0.0.1:9092 com.google.sample.purchases
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