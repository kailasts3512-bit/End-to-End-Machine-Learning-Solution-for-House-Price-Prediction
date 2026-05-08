# API Reference

## POST /predict

### Description
Predicts house prices.

### Request Example

```json
{
    "area": 1200,
    "bedrooms": 3,
    "bathrooms": 2,
    "age": 5,
    "location": "City Center",
    "property_type": "Apartment"
}



Response Example


---

# scripts/train_model.py

```python
from src.model_training import train_model

print('Training Model...')
