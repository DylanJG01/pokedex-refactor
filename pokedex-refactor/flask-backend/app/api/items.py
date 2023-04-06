from flask import Blueprint, redirect, request
from datetime import date
from app.models import Item, db



items_routes = Blueprint("api/items", __name__, url_prefix = "api/items")

@items_routes.route("/<id>", methods = ["PUT"])
def update_item():
    item = Item.query.filter(Item.id == request.args.get('id'))

    if item:
        item = {
            **request.args
        }

        db.session.commit()
        return item.to_dict()
    
    # return ('item not found', 404)
    return 'Item not found'


