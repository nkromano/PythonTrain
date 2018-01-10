import platform
import winreg
def get_registry_product_id(product_name):
    handle = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    bit_capacity = platform.architecture()
    if '64' in bit_capacity[0]:
        TZKEYNAME = r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    else:
        TZKEYNAME = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
    tzkey = winreg.OpenKey(handle, TZKEYNAME)
    for i in range(winreg.QueryInfoKey(tzkey)[0]):
        subkey = winreg.EnumKey(tzkey, i)
        sub = winreg.OpenKey(tzkey, subkey)
        try:
            info = winreg.QueryValueEx(sub, 'DisplayName')
            if info[0] == product_name:
                return subkey
        except:
          continue