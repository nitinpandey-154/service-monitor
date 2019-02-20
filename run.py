import argparse
import os
import json
from monitoring.lib.factory import get_factory_method


def get_commandline_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', required=True, help="Path of configuration json file")
    args = vars(parser.parse_args())
    return args


def read_file_contents(file_path):
    if not os.path.exists(file_path):
        # logger.error("The file-path %s does not exist. Exiting!" % file_path)
        raise Exception("File - %s not found " % file_path)
    with open(file_path) as file_reader:
        return json.load(file_reader)


def start_monitoring(input_config):
    status_dictionary = {}
    for service in input_config['services']:
        arguments = input_config['services'][service]
        method = get_factory_method(arguments['type'])
        status = method(**arguments)
        status_dictionary[service] = status
    return status_dictionary


if __name__ == '__main__':
    args = get_commandline_args()
    config = read_file_contents(args['config'])
    print start_monitoring(config)
