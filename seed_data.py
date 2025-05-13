from faker import Faker
from app import create_app, db
from app.models import User, Box, Product, ProductHistory
import random
from datetime import datetime, timedelta

app = create_app()
app.app_context().push()

fake = Faker()

def seed_users(n=100):
    users = []
    for _ in range(n):
        user = User(
            username=fake.unique.user_name(),
            email=fake.unique.email(),
            password=fake.password(),
            name=fake.name()
        )
        db.session.add(user)
        users.append(user)
    db.session.commit()
    return users

def seed_boxes(users, n=1000):
    boxes = []
    for _ in range(n):
        user = random.choice(users)
        box = Box(
            name=fake.word(),
            user_id=user.id
        )
        db.session.add(box)
        boxes.append(box)
    db.session.commit()
    return boxes

def seed_products(boxes, n=3000):
    products = []
    for _ in range(n):
        box = random.choice(boxes)
        product = Product(
            name=fake.word(),
            description=fake.sentence(),
            box_id=box.id
        )
        db.session.add(product)
        products.append(product)
    db.session.commit()
    return products

def seed_product_history(products, boxes):
    for product in products:
        before = random.choice(boxes + [None])
        after = product.box
        history = ProductHistory(
            product_id=product.id,
            box_id_before=before.id if before else None,
            box_id_after=after.id,
            timestamp=fake.date_time_between(start_date='-1y', end_date='now')
        )
        db.session.add(history)
    db.session.commit()

if __name__ == '__main__':
    print("Seeding users...")
    users = seed_users()
    print("Seeding boxes...")
    boxes = seed_boxes(users)
    print("Seeding products...")
    products = seed_products(boxes)
    print("Seeding product history...")
    seed_product_history(products, boxes)
    print("Datos de prueba insertados correctamente.")
