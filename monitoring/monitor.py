import sys
import argparse
import os
import monitoring

def get_commandline_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', required=True, help="Path of configuration json file")
    args = vars(parser.parse_args())
    return args


def read_file_contents(file_path):
    if not os.path.exists(file_path):
        # logger.error("The file-path %s does not exist. Exiting!" % file_path)
        raise Exception("File - %s not found " % file_path)


if __name__ == '__main__':
    args = get_commandline_args()
    print args
