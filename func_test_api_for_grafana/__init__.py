import json
import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = [
        {'Block_1': {'install': True,
                     'build': False,
                     'l2_test': False}},
        {'Block_2': {'install': False,
                     'build': False,
                     'l2_test': False}},
        {'Block_3': {'install': False,
                     'build': False,
                     'l2_test': False}},
        {'Block_4': {'install': False,
                     'build': False,
                     'l2_test': False}}
    ]

    func.HttpResponse.mimetype = 'application/json'
    func.HttpResponse.charset = 'utf-8'
    return func.HttpResponse(json.dumps(data), status_code=200, mimetype='application/json', charset='utf-8')
