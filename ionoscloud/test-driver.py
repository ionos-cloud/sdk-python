#!/usr/bin/env python

import sys
import json
import importlib
import os
import re

module_names_to_import = [
  'ionoscloud',
  'ionoscloud_autoscaling',
  'ionoscloud_dbaas_postgres',
]

for module_name in module_names_to_import:
  try:
      ionoscloud = importlib.import_module(module_name)
      break
  except ImportError:
      pass

def get_request_classes():
    classes = []
    for key in dir(ionoscloud.api):
        structure = getattr(ionoscloud.api, key)
        if isinstance(structure, type):
            classes.append(structure)
    return classes


def get_class_and_method(operation):
    classes = get_request_classes()
    searched_method = '%s_with_http_info' % re.sub(r'(?<!^)(?=[A-Z])', '_', operation).lower()
    for request_class in classes:
        method_list = {func: getattr(request_class, func) for func in dir(request_class) if callable(getattr(request_class, func))}
        for method_name, method in method_list.items():
            # camelcase to underscore for python standard
            if method_name == searched_method:
                return request_class, method
    return None, None


if __name__ == "__main__":
    configuration = ionoscloud.Configuration(
        username=os.environ.get('IONOS_USERNAME'),
        password=os.environ.get('IONOS_PASSWORD'),
    )
    api_client = ionoscloud.ApiClient(configuration)

    input = sys.stdin.readlines()
    testing_data = json.loads(input[0])

    operation = testing_data['operation']
    params = {re.sub(r'(?<!^)(?=[A-Z])', '_', p['name']).lower(): p['value'] for p in testing_data.get('params', [])}

    try:
        if operation == 'waitForRequest':
            request_id = re.search('/requests/([-A-Fa-f0-9]+)/', params['request']).group(1)
            api_client.wait_for_completion(request_id)
            sys.stdout.write(json.dumps({}))
        else:
            classApi, method = get_class_and_method(operation)
            return_data, status_code, response_headers = method(classApi(api_client), **params)
            response_headers = dict(map(lambda x: (x[0], x[1].split(",")), dict(response_headers).items()))

            return_data = api_client.sanitize_for_serialization(return_data)

            sys.stdout.write(json.dumps({
                "result": return_data,
                "httpResponse": {
                    "statusCode": status_code,
                    "headers": response_headers,
                    "body": return_data,
                }
            }))
    except ionoscloud.exceptions.ApiException as e:
        sys.stdout.write(json.dumps({
            "result": 'ApiException occured',
            "httpResponse": {
                "statusCode": e.status,
                "headers": dict(e.headers),
                "body": e.body,
            },
            "error": e.body,
        }))
    except Exception as e:
        sys.stdout.write(json.dumps({
            "result": 'GeneralException occured',
            "httpResponse": {
                "statusCode": None,
                "headers": None,
                "body": str(e),
            },
            "error": str(e),
        }))
