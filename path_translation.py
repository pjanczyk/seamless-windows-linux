windows_drives = ["C"]


def windows_to_linux(path: str):
    if path[0] in windows_drives and path[1] == ':':
        drive = path[0]
        rest = path[2:]
        return '/' + drive.lower() + rest.replace('\\', '/')
    else:
        raise RuntimeError("Unsupported path", path)
