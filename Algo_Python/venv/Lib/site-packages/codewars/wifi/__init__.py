from scapy.all import *
from datetime import datetime
import time

from codewars.logger import Logger


class Wifi(object):
    """
    Note
    ----
    In order to use this module u need to provide the python application the right
    permissions. Most likly sudo. This is because `scapy` makes use of your network
    card. Therefor it needs permissions.

    Warning
    -------
    The error `AttributeError: 'L2ListenSocket' object has no attribute 'ins'`
    is a reaction to the note above. Not the right permissions.
    """
    def __init__(self, iAddr="eth0"):
        """You can use `ifconfig` to find the network name.
        Something like `mon0`.
        
        Parameters
        ----------
        iAddr
            Type: String
            Default: 'eth0'
            Description: The network interface to sniff on
        """
        conf.iface = iAddr
        self.__listener = []
        self.__logger = Logger("Codewars Wifi")

    # def sniff_ssid(self, forever=False):
    #     """Sniff network for SSIDs
        
    #     Parameters
    #     ----------
    #     forever
    #         Type: bool
    #         Default: False
    #         Description: Sniff SSIDs on the network
    #         True: Scan forever, pauzes script
    #         False: Scan X amount of time

    #     Returns
    #     -------
    #     List
    #         Type: List
    #         Content: String
    #         Description: List of SSID's found while sniffing
            
    #     Note
    #     ----
    #     TODO This function still needs testing
    #     """
    #     results = []
    #     def PacketHandler(packet):
    #         if packet.haslayer(Dot11):
    #             if packet.type == 0 and packet.subtype == 8:
    #                 if packet.addr2 not in results:
    #                     results.append((packet.addr2, packet.info))
    #                     self.__logger.info("Access Point MAC: {packet.addr2} with SSID: {packet.info} ")
    #     if forever: sniff(prn=PacketHandler)
    #     else: sniff(prn=PacketHandler, count=100)
    #     return results

    
    def sniff(self, totalResults = 10):
        """Sniff Network packages on the selected `iAddr`

        Parameters
        ----------
        totalResults
            Type: Int
            Default: 10
            Description: The sniff amount.

        Returns
        -------
        List
            Type: List
            Content: `scapy.plist.PacketList`
            Description: A list of network packages adresses that are discovered.
            Limited to the amount of the `totalResults` parameter.
        """
        try:
            return [pk for pk in sniff(count=totalResults)]
        except PermissionError:
            raise OSError("Run as admin or provide the right permissions to this application in order to use the codewars wifi module")

    def sniff_forever(self, duration: int = 300):
        """Sniffs forever and stores its data in self.__listener

        Parameters
        ----------
        duration
            Type: Int
            Default: 300 # 1 second * sniff time * 1 package
            Description: Sniff until duration reached 0

        Note
        ----
        Results can be fetched from `self.sniff_history`
        """
        while duration >= 0:
            duration -= 1
            time.sleep(1)
            results = self.info(self.sniff())
            for item in results:
                if item not in self.__listener: self.__listener.append(item)
            self.__logger.info("\n".join([f"{datetime.utcnow()} - {i}" for i in self.__listener][:-1]))

    def info(self, packages = []):
        """Look for information about a package

        Parameters
        ----------
        packages
            Type: `scapy.Packet`
            Default: Empty List
            Description: A list with packages founnd with the `sniff` method.

        Returns
        -------
        List
            Type: List
            Content: Objects
            Description: Information of each package
        """
        try:
            if packages:
                return [pk.summary() for pk in packages]
            else: raise AttributeError("The list you want to sniff info from is empty!")
        except PermissionError:
            raise OSError("Run as admin or provide the right permissions to this application in order to use the codewars wifi module")
