#!/usr/bin/env python
import sys
import subprocess
from kubernetes import client, config


config.load_kube_config()


def get_pod(pod_name, namespace):
    api_instance = client.CoreV1Api()
    pods = api_instance.list_namespaced_pod(namespace)
    for pod in pods.items:
        if pod.metadata.name == pod_name:
            print('Start watching pod/' + pod.metadata.name)
            return pod
    print('Resource not found')


def execute_command(args):
    cmd = args
    print('Executing: ' + ' '.join(str(e) for e in cmd))
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Error executing command: {cmd}")
        print(f"Error message: {stderr.decode('utf-8')}")
    else:
        print(stdout.decode('utf-8'))


def main():
    if len(sys.argv) < 3:
        print('Usage: kubectl ids POD_NAME NAMESPACE')
        return

    pod_name = sys.argv[1]
    namespace = sys.argv[2]
    if get_pod(pod_name, namespace):
        execute_command(['kubectl', 'sniff', pod_name, '-n', namespace, '-o', '/nfs/pcap/nginx.pcap'])


if __name__ == '__main__':
    main()
