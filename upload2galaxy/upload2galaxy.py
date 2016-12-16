#!/usr/bin/env python3
#version 1.0
#author: Ricardo Lebron
#email: rlebron@ugr.es

import argparse, os, bioblend.galaxy, logging

FORMAT = '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig(format = FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

parser = argparse.ArgumentParser(prog = 'upload2galaxy', description = 'Upload a File to a Galaxy Server')
parser.add_argument('-u', '--url', help = 'URL of a Galaxy Server', type = str, action = 'store', default = 'https://usegalaxy.org')
parser.add_argument('-k', '--key', help = 'API Key of your Galaxy Account', type = str, action = 'store', required = True)
parser.add_argument('-i', '--input', help = 'Path of the File to Upload', type = str, action = 'store', required = True)
parser.add_argument('-n', '--name', help = 'Name of the Galaxy History to be created', type = str, action = 'store', default = 'MethFlow')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

if not os.path.exists(args.input):
    logger.critical("{i} does not exist.".format(i = args.input))
    raise SystemExit
else:
    if not os.path.isfile(args.input):
        logger.critical("{i} is not a file.".format(i = args.input))
        raise SystemExit
    else:
        if not os.access(args.input, os.R_OK):
            logger.critical("You do not have permission to read the file: {i}".format(i = args.input))
            raise SystemExit

gi = bioblend.galaxy.GalaxyInstance(url = args.url, key = args.key)

galaxyHistory = bioblend.galaxy.histories.HistoryClient(gi).create_history(name = args.name)

tools = bioblend.galaxy.tools.ToolClient(gi)

logger.info('Uploading file {i} to the Galaxy server {u}'.format(i = args.input, u = args.url))
try:
    tools.upload_file(args.input, galaxyHistory['id'])
except:
    logger.error('Unable to upload the file. Check your connection and your credentials and try again.')
else:
    logger.info('File uploaded successfully.')
