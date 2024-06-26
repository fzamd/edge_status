import argparse
import json
import re
import subprocess
import urllib2

from urllib import quote


def ping_destination_through_interface(config):
    ttl_regex = r'time=(.*) ms'
    ttl = None
    interface_string = ''
    if config.get('interface'):
        interface_string = '-I %s' % config['interface']

    command_string = 'sudo ping %s %s -c 1' % (interface_string, config['destination'])

    proc = subprocess.Popen(command_string.split(), stdout=subprocess.PIPE)

    for line in proc.stdout:
        match = re.search(ttl_regex, line)
        if match != None:
            ttl = match.group(1)
            break

    return ttl


def push_ttl_to_status_registry(ttl, config):
    if config.get('status_url'):
        contents = urllib2.urlopen(config['status_url'] + ttl).read()
    else:
        raise Exception('Status url missing from config!')


def run():
    parser = argparse.ArgumentParser(description='Checks the interface status and response time against a destination server ip')
    parser.add_argument('-c', '--config', required=True, help='Path to config file')

    args = parser.parse_args()

    with open(args.config, 'r') as f:
        config = json.load(f)

        ttl = ping_destination_through_interface(config)
        if ttl:
            push_ttl_to_status_registry(ttl, config)


if __name__ == '__main__':
    run()
