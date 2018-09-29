import os
import sys
import time
import zipfile
import shutil

from urllib import request


start_time = None
def reporthook(blocknum, blocksize, totalsize):
    speed = (blocknum * blocksize) / (time.time() - start_time)
    # speed_str = " Speed: %.2f" % speed
    speed_str = 'Speed: ' + str(int(speed / 1024)) + 'KB/s'
    recv_size = blocknum * blocksize

    # display process
    size_str = 'Received: ' + str(int(recv_size / 1024)) + 'KB, '
    sys.stdout.write(size_str + speed_str)
    sys.stdout.flush()
    sys.stdout.write('\r')


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return None


def get_config_path():
    path = find('.HA_VERSION', '/')
    if not path:
        return None
    path = path[:len(path) - 11]
    print("Home Assistant configuration path found: %s", path)
    return path


def uninstall_old(path):
    print("Uninstall molohub old version...")
    path += '/custom_components/molohub'
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass


def download_file():
    global start_time
    print("Downloading file...")
    save_path = 'molohub-master.zip'
    url = 'https://codeload.github.com/haoctopus/molohub/zip/master'

    start_time = time.time()
    request.urlretrieve(url, save_path, reporthook)
    print('')


def extract_file():
    print("Extracting file...")
    try:
        shutil.rmtree('temp/')
    except FileNotFoundError:
        pass
    with zipfile.ZipFile("molohub-master.zip", 'r') as f:
        for file in f.namelist():
            f.extract(file, "temp/")


def copy_file(path):
    print("Copying file...")
    path += '/custom_components/molohub'
    frompath = 'temp/molohub-master/molohub'
    shutil.copytree(frompath, path)


def configurate(path):
    print("Configurating...")
    path += '/configuration.yaml'
    shutil.copy(path, path + '.bak')
    file_str = open(path, 'r').read()
    if 'molohub:' in file_str:
        return
    with open(path, 'a') as f:
        f.write('\nmolohub:\n')


def delete_file():
    delete_list = ['auto_install.py', 'molohub-master.zip', 'temp/']
    for item in delete_list:
        try:
            shutil.rmtree(item)
        except Exception:
            pass
        try:
            os.remove(item)
        except Exception:
            pass


if __name__ == '__main__':
    path = get_config_path()
    if not path:
        print("Error finding Home Assistant configuration path!")
        print("Install failed.")
        exit(0)

    uninstall_old(path)
    download_file()
    extract_file()
    copy_file(path)
    configurate(path)
    delete_file()

    print("Successfully installed.")
    print("configuration.yaml has copied to configuration.yaml.bak")
    print("For any questions, please contact us:")
    print("  - Email:   octopus201806@gmail.com")
    print("  - QQGroup: 598514359")
