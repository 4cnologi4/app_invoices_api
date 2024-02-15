import json

from flask import jsonify, request, Blueprint

from src.web.controllers import InvoicesController

invoices_routes = Blueprint('invoices_routes', __name__)


@invoices_routes.route('/invoices', methods=['POST'])
def get_invoices_by_date_range():
    request_body = json.dumps(request.get_json())
    date_range_dict = json.loads(request_body)
    start_date = date_range_dict["start_date"]
    end_date = date_range_dict["end_date"]
    data = InvoicesController().get_invoices_by_date_range(start_date, end_date)
    return data
