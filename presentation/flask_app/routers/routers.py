from flask import Blueprint, request, jsonify, Response
from presentation.flask_app.routers.controller_objects import \
    ControllerObjectCreator
from infrastructure.flask_app.interfaces.\
    calculate_result_controller_interface import \
    CalculateResultControllerInterface
from infrastructure.flask_app.interfaces.\
    calculate_result_and_save_controller_interface import \
    CalculateResultAndSaveControllerInterface
from infrastructure.flask_app.interfaces.\
    get_saved_result_controller_interface import \
    GetSavedResultControllerInterface


calculator_bprint: Blueprint = Blueprint('calculator_bprint', __name__)

# Как я понял, когда я делаю API, то у меня нету модуля View,
# т.к. нечего рендерить по факту. Поэтому DS с данными можно
# просто вернуть с презентера. В теории у меня должен быть
# сериализатор вместо View если я делаю API.


@calculator_bprint.route('/calculate_result', methods=['POST'])
def calculate_result() -> Response:
    controller: CalculateResultControllerInterface = (
        ControllerObjectCreator.make_calc_res_contr()
    )
    resp: dict = controller.process_data(
        request.get_json()
    )
    return jsonify(resp)


@calculator_bprint.route('/calculate_result_and_save', methods=['POST'])
def calculate_result_and_save() -> Response:
    controller: CalculateResultAndSaveControllerInterface = (
        ControllerObjectCreator.make_calc_res_and_save_contr()
    )
    resp: dict = controller.process_data(
        request.get_json()
    )
    return jsonify(resp)


@calculator_bprint.route('/retrieve_prev_calculations', methods=['POST'])
def retrieve_prev_calculations() -> Response:
    controller: GetSavedResultControllerInterface = (
        ControllerObjectCreator.make_get_saved_res_contr()
    )
    resp: dict = controller.process_data(
        request.get_json()
    )
    return jsonify(resp)
