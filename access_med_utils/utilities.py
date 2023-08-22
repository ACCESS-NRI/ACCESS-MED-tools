import os
import tempfile

def symlink_force(target, link_name):
    '''
    Create a symbolic link link_name pointing to target.
    Overwrites link_name if it exists.
    '''

    # os.replace() may fail if files are on different filesystems
    link_dir = os.path.dirname(link_name)

    while True:
        temp_link_name = tempfile.mktemp(dir=link_dir)
        try:
            os.symlink(target, temp_link_name)
            break
        except FileExistsError:
            pass
    try:
        os.replace(temp_link_name, link_name)
    except OSError:  # e.g. permission denied
        os.remove(temp_link_name)
        raise