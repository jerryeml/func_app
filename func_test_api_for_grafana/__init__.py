import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    data = {
        'Block_1': {'install': True,
                    'build': False,
                    'l2_test': False},
        'Block_2': {'install': False,
                    'build': False,
                    'l2_test': False},
        'Block_3': {'install': False,
                    'build': False,
                    'l2_test': False},
        'Block_4': {'install': False,
                    'build': False,
                    'l2_test': False}
    }

    if name:
        return func.HttpResponse(data, status_code=200)
    else:
        return func.HttpResponse(data, status_code=200)
