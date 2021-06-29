import json
import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    node_view = [
        {'block_name': 'block 1',
         'github_ee': 'mgcp',
         'cicd_entry_tool': 'codebuild',
         'stage_view': [{'id': 'init', 'status': 'running'},
                        {'id': 'testing', 'status': 'waiting'},
                        {'id': 'tear_down', 'status': 'stopping'}]
        },
        {'block_name': 'block 2',
         'github_ee': 'ds',
         'cicd_entry_tool': 'jenkins',
         'stage_view': [{'id': 'init', 'status': 'waiting'},
                        {'id': 'testing', 'status': 'waiting'},
                        {'id': 'tear_down', 'status': 'waiting'}]
        }
    ]

    func.HttpResponse.mimetype = 'application/json'
    func.HttpResponse.charset = 'utf-8'
    return func.HttpResponse(json.dumps(node_view), status_code=200, mimetype='application/json', charset='utf-8')
