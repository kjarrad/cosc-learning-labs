#!/usr/bin/env python2.7

# Copyright 2015 Cisco Systems, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

''' Sample usage of function 'basics.topology.mount'.

    Print the function's documentation then apply the function to any one device that is configured and not mounted.
'''

from __future__ import print_function
import pydoc
import settings
from basics import topology

def mount_device(device_name):
    """Mount a single device by inserting in the NETCONF topology."""
    device_config = settings.config['network_device'][device_name]
    print('device_mount(' + device_name, *device_config.values(), sep=', ', end=')\n')
    topology.mount(
        device_name,
        device_config['address'],
        device_config['port'],
        device_config['username'],
        device_config['password'])

def main():
    print(pydoc.plain(pydoc.render_doc(topology.mount)))
    try:
        device_name = topology.unmounted_nodes()[0]
        mount_device(device_name)
    except IndexError:
        print('All configured devices are mounted. Demonstration cancelled.')

if __name__ == "__main__":
    main()