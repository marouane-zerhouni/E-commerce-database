from faker import Faker
import faker_commerce

f = Faker()
f.add_provider(faker_commerce.Provider)

product = [
    {'id' : f.unique.random_int(min=100000, max=999999), 
     'name' : f.unique.ecommerce_name(),
     'desc' : f.paragraph(nb_sentences = 2),
     'SKU' : f.unique.bothify(text='??-???-###', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
     'category_id' : f.unique.random_int(min=100, max=999),
     'inventory_id' : f.unique.random_int(min=1, max=2500),
     } 
     for x in range(500)]

print(product)