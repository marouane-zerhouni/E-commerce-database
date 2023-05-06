from faker import Faker
import faker_commerce
from datetime import datetime

f = Faker()
f.add_provider(faker_commerce.Provider)

product = [
    {'id' : f.unique.random_int(min=100000, max=999999), 
     'name' : f.unique.ecommerce_name(),
     'desc' : f.paragraph(nb_sentences = 2),
     'SKU' : f.unique.bothify(text='??-???-###', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
     'category_id' : f.unique.random_int(min=100, max=999),
     'inventory_id' : f.unique.random_int(min=1, max=2500),
     'price' : int("".join(filter(str.isdigit, f.pricetag()))),
     'discount_id' : 0,
     'created_at' : f.date_time_between_dates(datetime_start=datetime.datetime(2022, 1, 1, 00, 00, 00), datetime_end = datetime.now()),
     'modified_at' : f.date_time_between_dates(datetime_start=product["created_at"], datetime_end = datetime.now()),
     'deleted_at' : f.date_time_between_dates(datetime_start=product["created_at"], datetime_end = datetime.now())
     } 
     for x in range(500)]

print(product)