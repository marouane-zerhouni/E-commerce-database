from faker import Faker
import faker_commerce
from datetime import datetime
import random

f = Faker()
r = random
f.add_provider(faker_commerce.Provider)

product_category = [
    {
        "id": f.unique.random_int(min=100, max=999), 
        "name": f.unique.ecommerce_category(), 
        "desc": f.paragraph(nb_sentences=2), 
        "created_at": f.date_time_between_dates(
            datetime_start=datetime(2022,1,1,00,00,00), datetime_end=datetime.now()
        ),
        "modified_at": 0,
        "deleted_at": 0
    }
    for x in range(10)
]

for n in product_category:
    c = n["created_at"]
    n["modified_at"] = random.choices(
        [c, f.date_time_between_dates(datetime_start=c, datetime_end=datetime.now())],
        weights=[0.75, 0.25],
    )
    n["modified_at"] = n["modified_at"][0]
    m = n["modified_at"]
    n["deleted_at"] = random.choices(
        [m, f.date_time_between_dates(datetime_start=m, datetime_end=datetime.now())],
        weights=[0.8795, 0.005],
    )
    n["deleted_at"] = n["deleted_at"][0]

product_inventory = [
    {
        "id": f.unique.random_int(min=1, max=2500), 
        "quantity": f.random_int(min=0, max=1000), 
        "created_at": f.date_time_between_dates(
            datetime_start=datetime(2022,1,1,00,00,00), datetime_end=datetime.now()
        ),
        "modified_at": 0,
        "deleted_at": 0
    }
    for x in range(500)
]

for n in product_inventory:
    c = n["created_at"]
    n["modified_at"] = random.choices(
        [c, f.date_time_between_dates(datetime_start=c, datetime_end=datetime.now())],
        weights=[0.75, 0.25],
    )
    n["modified_at"] = n["modified_at"][0]
    m = n["modified_at"]
    n["deleted_at"] = random.choices(
        [m, f.date_time_between_dates(datetime_start=m, datetime_end=datetime.now())],
        weights=[0.8795, 0.005],
    )
    n["deleted_at"] = n["deleted_at"][0]

discount = [
    {
        "id": f.unique.random_int(min=100, max=999), 
        "name": f.unique.word(), 
        "desc": f.paragraph(nb_sentences=2), 
        "dicount_percent": r.random(),
        "active": f.pybool(truth_probability=22),
        "created_at": f.date_time_between_dates(
            datetime_start=datetime(2022,1,1,00,00,00), datetime_end=datetime.now()
        ),
        "modified_at": 0,
        "deleted_at": 0
    }
]

for n in discount:
    c = n["created_at"]
    n["modified_at"] = random.choices(
        [c, f.date_time_between_dates(datetime_start=c, datetime_end=datetime.now())],
        weights=[0.75, 0.25],
    )
    n["modified_at"] = n["modified_at"][0]
    m = n["modified_at"]
    n["deleted_at"] = random.choices(
        [m, f.date_time_between_dates(datetime_start=m, datetime_end=datetime.now())],
        weights=[0.8795, 0.005],
    )
    n["deleted_at"] = n["deleted_at"][0]

product = [
    {
        "id": f.unique.random_int(min=100000, max=999999),
        "name": f.unique.ecommerce_name(),
        "desc": f.paragraph(nb_sentences=2),
        "SKU": f.unique.bothify(
            text="??-???-###", letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ),
        "category_id": product_category[r.randint(0,9)]["id"],
        "inventory_id": product_inventory[r.randint(0,499)]["id"],
        "price": int("".join(filter(str.isdigit, f.pricetag()))),
        "discount_id": 0,
        "created_at": f.date_time_between_dates(
            datetime_start=datetime(2022, 1, 1, 00, 00, 00), datetime_end=datetime.now()
        ),
        "modified_at": 0,
        "deleted_at": 0,
    }
    for x in range(500)
]

for n in product:
    c = n["created_at"]
    n["modified_at"] = random.choices(
        [c, f.date_time_between_dates(datetime_start=c, datetime_end=datetime.now())],
        weights=[0.75, 0.25],
    )
    n["modified_at"] = n["modified_at"][0]
    m = n["modified_at"]
    n["deleted_at"] = random.choices(
        [m, f.date_time_between_dates(datetime_start=m, datetime_end=datetime.now())],
        weights=[0.8795, 0.005],
    )
    n["deleted_at"] = n["deleted_at"][0]



