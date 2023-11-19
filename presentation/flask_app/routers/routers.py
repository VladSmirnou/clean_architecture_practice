from flask import Blueprint, request


calculator_bprint: Blueprint = Blueprint('calculator_bprint', __name__)

# Как я понял, когда я делаю API, то у меня нету модуля View,
# т.к. нечего рендерить по факту. Поэтому DS с данными можно
# просто вернуть с презентера.


@calculator_bprint.route('/calculate_result', methods=['POST'])
def calculate_result() -> dict:
    resp: dict = calculator_bprint.controller.process_data(
        request.get_json()
    )
    return resp


@calculator_bprint.route('/calculate_result_and_save', methods=['POST'])
def calculate_result_and_save() -> dict:
    resp: dict = calculator_bprint.controller.process_data(
        request.get_json()
    )
    return resp


@calculator_bprint.route('/retrieve_prev_calculations', methods=['POST'])
def retrieve_prev_calculations() -> dict:
    resp: dict = calculator_bprint.controller.process_data(
        request.get_json()
    )
    return resp
