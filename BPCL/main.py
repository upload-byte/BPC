import code
import locale
import platform
import socket
import uuid


class NetworkUtils:

  @staticmethod
  def get_language():
    """1. Language APIs"""
    return locale.getdefaultlocale()[0]

  @staticmethod
  def fetch_local_connection():
    """2. Fetching Local Connection"""
    return socket.gethostname()

  @staticmethod
  def check_operating_system():
    """3. Check Operating System"""
    return f'{platform.system()} {platform.release()}'

  @staticmethod
  def find_ip_address():
    """4. Find IP Address"""
    return socket.gethostbyname(socket.gethostname())

  @staticmethod
  def find_mac_address():
    """5. Find Mac Address"""
    mac = uuid.getnode()
    return ':'.join(f'{(mac >> i) & 0xff:02x}' for i in range(40, -1, -8))

  @staticmethod
  def scripting_console():
    """6. Online Scripting Console"""
    code.interact(banner='Interactive Python Console Active')


# Dispatcher function if single 'connection' endpoint is required
def connection(option: int):
  utils = {
      1: NetworkUtils.get_language,
      2: NetworkUtils.fetch_local_connection,
      3: NetworkUtils.check_operating_system,
      4: NetworkUtils.find_ip_address,
      5: NetworkUtils.find_mac_address,
      6: NetworkUtils.scripting_console,
  }
  action = utils.get(option)
  return action() if action else 'Invalid selection'
