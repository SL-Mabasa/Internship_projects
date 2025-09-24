from django.db import migrations

def load_initial_products(apps, schema_editor):
    Product = apps.get_model('duties', 'Product')
    products = [
        ("Concrete", "10MPa", 1500, "Standard concrete for general use."),
        ("Concrete", "15MPa", 2000, "Slightly stronger, suitable for light construction."),
        ("Concrete", "20MPa", 2500, "Medium strength concrete for structural use."),
        ("Concrete", "25MPa", 3000, "High strength concrete for heavy-duty structures."),
        ("Hemp Concrete", "50MPa", 5500, "Specialized eco-friendly hemp concrete."),
    ]
    for name, strength, price, desc in products:
        Product.objects.create(name=name, strength=strength, price=price, description=desc)

class Migration(migrations.Migration):

    dependencies = [
        ('duties', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_products),
    ]
