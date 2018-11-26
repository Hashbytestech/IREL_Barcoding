from datetime import date
from datetime import datetime
from pony.orm import *


db = Database(provider='mysql',host='localhost',user='root',passwd='mahesh@7',db='text')


class Department(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    purchase_requisition = Set('PurchaseRequisition')
    stocks = Set('Stock')


class Warehouse(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    racks = Set('Rack')


class Rack(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    warehouse = Required(Warehouse)
    shelfs = Set('Shelf')


class Shelf(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    barcode = Required(str)
    rack = Required(Rack)
    stocks = Set('Stock')


class PurchaseRequisition(db.Entity):
    id = PrimaryKey(int, auto=True)
    products = Set('Product')
    department = Required(Department)
    capital_or_revenue=Required(str)
    indent_no=Optional(int)
    indentor_name=Required(str)
    indentor_designation=Requireds(str)
    purpose_of_procurement=Required(text)
    nature_of_indent=Optional(str)
    section_code=Optional(int)
    count = Required(int)
    fullfilled_or_not = Required(bool, default=False)
    fullfilled_date = Optional(datetime)
    stocks = Set('Stock')


class Stock(db.Entity):
    id = PrimaryKey(int, auto=True)
    product = Required('Product')
    Unity_of_measurement=Optional(str)
    lrd=Optinal(date)
    lid=Optinal(date)
    value=Optinal(float)
    bal_value=Optinal(float)
    barcode = Required(str)
    shelf = Required(Shelf)
    purchase_order = Required(PurchaseRequisition)
    expiry_date = Required(date)
    issued_or_not = Required(bool, default=False)
    issued_to = Optional(Department)
    issued_date = Required(datetime)


class Product(db.Entity):
    id = PrimaryKey(int, auto=True)
    product_code=Required(int)
    name = Required(str)
    purchase_orders = Set(PurchaseRequisition)
    stocks = Set(Stock)


set_sql_debug(True)
db.generate_mapping(create_tables=True)
