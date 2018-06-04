import sys
import argparse
import logging
import os
import util.loggerinitializer as utl
from util import ssh_manip

# Initialize log object
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
utl.initialize_logger(os.getcwd(), logger)


def main():
    parser = argparse.ArgumentParser(description="A tool to connect to a remote server")

    parser.add_argument('-c', '--credentials', action='store', help='A config file. See <<config.ini.template>>')

    parser.add_argument('--command', action='store', type=str, help='A command to be run in the remote server')

    args = parser.parse_args()


    credentials = ssh_manip.get_credentials(args.credentials, logger)

    client = ssh_manip.connect_to_client(credentials, logger)

    ssh_manip.run_command(client, args.command)



if __name__ == '__main__':
    main()