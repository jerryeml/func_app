import logging

import azure.functions as func
from azure.cli.core import get_default_cli


def az_cli(args):
    cli = get_default_cli()
    cli.invoke(args)

    if cli.result.result:
        return cli.result.result

    elif cli.result.error:
        raise cli.result.error
    
    return True


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

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:

        # This will raise error because signal only works in main thread

        # command = ['artifacts', 'universal', 'download', '--organization', 'https://dev.azure.com/infinite-wars/',
        #            '--feed', 'infinite-wars', '--name', 'data-l2-testing-case-v1.0.1776', '--version', '1.0.0',
        #            '--path', '.']
        # a = az_cli(command)
        # logging.info(f"a return {a}")

        command = ['lab', 'get', '-g', 'rg-testing-env-lab', '--name', 'dtl-aladdin-test']
        test = az_cli(command)
        logging.info(f"test return {test}")

        logging.info("123456")

        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
