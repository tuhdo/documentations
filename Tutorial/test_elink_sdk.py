from elink_sdk import elink

if __name__ == '__main__':
    """
    the script will create a new connection to ELinkKVM at ip address : 10.42.0.2
    """
    elink.newConnection('10.42.0.2')
