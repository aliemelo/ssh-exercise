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

    parser = argparse.ArgumentParser(description="A tool to copy files to and from a remote server")

    parser.add_argument('-c', '--credentials', action='store', help='A config file. See <<config.ini.template>>')



    subparsers = parser.add_subparsers(title='subcommands', description='valid commands', help='Use copy_file.py {'
                                                                                               'subcommand} -h for '
                                                                                               'help with each '
                                                                                               'subcommand')
    # subcommand put
    parser_put = subparsers.add_parser('put', help='Send files to remote server')

    parser_put.add_argument('--src', action='store', dest='src_put',help='The path of the file to be copied')

    parser_put.add_argument('--dest', action='store', dest='dest_put',help='The path to where the file should be '
                                                                           'copied to in the remote server')

    # subcommand get
    parser_get = subparsers.add_parser('get', help='Send files to remote server')

    parser_get.add_argument('--src', action='store', dest='src_get', help='The path of the file to be copied')

    parser_get.add_argument('--dest', action='store', dest='dest_get', help='The path to where the file should be '
                                                                            'copied to in the local machine')

    args = parser.parse_args()



    credentials =ssh_manip.get_credentials(args.credentials, logger)

    sftp = ssh_manip.connect_to_client_copy(credentials, logger)

    if hasattr(args, 'src_put'):
        ssh_manip.copy_file_to_server(sftp, args.src_put, args.dest_put, logger)

    if hasattr(args, 'dest_get'):
        ssh_manip.get_file_from_server(sftp, args.src_get, args.dest_get, logger)


if __name__ == '__main__':
    main()