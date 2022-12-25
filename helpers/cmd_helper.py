import signal
from os import popen
from pathlib import Path
from time import sleep
from subprocess import Popen
import parver
from parver import Version
from psutil import pids, pid_exists
from polling2 import poll
from psutil import net_connections

from helpers.network_helpers import is_port_open


def get_android_adb_device():
    lines = popen('adb devices').readlines()
    devices = [cur_line for cur_line in lines if cur_line.strip().endswith('device')]
    assert len(devices) == 1, f'current implementation supports a single device to be connected: {devices}'
    return devices[0].split('\t')[0]


def get_ios_udid():
    devices = popen('idevice_id -l').readlines()
    assert len(devices) == 1, f'current implementation supports a single device to be connected: {devices}'
    return devices[0].strip()


def get_ios_name():
    devices = popen('idevicename').readlines()
    assert len(devices) == 1, f'current implementation supports a single device to be connected: {devices}'
    return devices[0].strip()


def get_ios_version():
    devices = popen('ideviceinfo | grep ProductVersion').readlines()
    assert len(devices) == 1, f'current implementation supports a single device to be connected: {devices}'
    return devices[0].split(':')[1].strip()

def freeze_requirements():
    pythons = popen('python -m pip freeze').readlines()
    outpath = (Path(__file__).parent / Path('../reqs_freezed.txt')).resolve()
    with open(outpath, 'w') as fp:
        fp.writelines(pythons)

def get_appium_version():
    verstr = ''.join(popen('~/.npm-packages/bin/appium --version').readlines())
    try:
        Version.parse(verstr)
    except parver.ParseError:
        raise Exception(f'appium version is not installed. Use: npm install -g appium && npm install -g appium-doctor')

def start_appium() -> Popen:
    default_appium_port = 4723
    appium_path = popen('which appium').read().strip()
    proc = None
    try:
        proc = Popen(appium_path, start_new_session=True)
        poll(target=lambda: pid_exists(proc.pid),
             timeout=10,
             step=1.0)

        poll(target=lambda: is_port_open('0.0.0.0', default_appium_port),
             timeout=20,
             step=1.0)
    except:
        kill_appium(proc)

    return proc

def kill_appium(proc: Popen) -> None:
    if proc is None:
        return
    # proc.kill()
    assert pid_exists(proc.pid), 'the process is expected to still exist before terminating it'
    proc.send_signal(signal.SIGTERM)

    poll(target=lambda: proc.communicate(),
         check_success=lambda target_result: not pid_exists(proc.pid),
         timeout=30,
         step=1.0)

if __name__ == '__main__':
    appium_path = popen('which appium').read().strip()
    proc = None
    try:
        # proc = Popen('/home/student/.npm-packages/bin/appium', start_new_session = True)
        proc = Popen(appium_path, start_new_session = True)
        poll(target=lambda: pid_exists(proc.pid),
             timeout=10,
             step=1.0)

        poll(target=lambda: is_port_open('0.0.0.0', 4723),
             timeout=20,
             step=1.0)

        sleep(3)
        print('sleep end', proc.pid, proc.returncode)
    finally:
        # proc.kill()
        assert pid_exists(proc.pid), 'the process is expected to still exist before terminating it'
        proc.send_signal(signal.SIGTERM)
        # sleep(3)
        print('the end', proc.pid, proc.returncode)
        # proc.communicate()

        poll(target=lambda: proc.communicate(),
             check_success=lambda target_result: not pid_exists(proc.pid),
             timeout=30,
             step=1.0)
