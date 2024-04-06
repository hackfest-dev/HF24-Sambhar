from website.models import Inventory, Category, Units  # Import your SQLAlchemy models
from  website import db,create_app  # Import your SQLAlchemy database object

app = create_app()

with app.app_context():
# Create sample entries for Category and Units tables
    category1 = Category(category_name='Raw-Materials')
    category2 = Category(category_name='Finished-products')

    units1 = Units(unit_name='Kg')
    units2 = Units(unit_name='L')

    db.session.add_all([category1, category2, units1, units2, ])
    db.session.commit()

    # Create sample entries for Inventory table
    inventory1 = Inventory(item_id="ITEM00",item_name='Rice', item_category=category1.category_id, units=units1.unit_id,current_stock=200,default_price=50,regular_selling_price=60,regular_buying_price=45,mrp=70,dealer_price=55,distributor_price=57,tax=2.5,item_type="Buy",hsn_code="rice123",min_stock_level=100,max_stock_level=300 )
    inventory2 = Inventory(item_id="ITEM01",item_name='Rice', item_category=category2.category_id, units=units2.unit_id,current_stock=400,default_price=60,regular_selling_price=70,regular_buying_price=55,mrp=80,dealer_price=65,distributor_price=77,tax=2.5,item_type="Buy",hsn_code="oil123",min_stock_level=100,max_stock_level=300 )

    # Add sample entries to the session
    db.session.add_all([inventory1, inventory2])

    # Commit the changes to the database
    db.session.commit()
