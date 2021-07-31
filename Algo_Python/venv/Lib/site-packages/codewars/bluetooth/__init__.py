from datetime import datetime
import bluetooth

from codewars.logger import Logger


class Bluetooth(object):
    """This is a simple wrapper of the python package `PyBluez`.
    
    Note
    ----
    Do not forget to intstall the dependency.
    `sudo apt-get install libbluetooth-dev`
    """
    def __init__(self):
        self.__logger = Logger(appname="Bluetooth", mode="DEBUG", write=False)
        self.__logger.info("Looking for devices...")
        self.nearby_devices = bluetooth.discover_devices(duration=10, flush_cache=True, lookup_names=False)
        self.__discovering = False


    def discover(self, duration: int = 10, flush_cache: bool = True, lookup_names: bool = False):
        """Look for available bluetooth devices, returns a list with available bt adresses
        
        Parameters
        ----------
        duration
            Default: 10
            Type: int
            Description: The duration of the time to search for new devices

        flush_cach
            Default: True
            Type: bool
            Description: Flush found devices when discovering again
        
        lookup_names
            Default: False
            Type: bool
            Description: Discover the names of the devicovered devices

        Returns
        -------
        List
            Type: List
            Content: Strings
            Description: A list of BT adresses that are discovered.
            If None are discoverd the list will be empty

        Note
        ----
        When turning `lookup_adress` to True the list that returns will contain
        Tuples instead of Strings.

        """
        if self.__discovering == False: self.__discovering = True
        discovery = bluetooth.discover_devices(duration, flush_cache, lookup_names)
        if discovery: self.__discovering = False
        return discovery


    def isDiscovering(self):
        """Check if this class is currently discovering

        Returns
        -------
        Bool
            True: When this class is currently looking for devices
            False: When this class is not trying to find new devices
        """
        return self.__discovering


    def isValid(self, btAddr: str):
        """Check if a BlueTooth adress is valid
        
        Parameters
        ----------
        btAddr
            Type: String
            Description: A bluetooth adress

        Returns
        -------
        Bool
            True: When adress is valid
            False: When adress is invalid
        """
        return bluetooth.is_valid_address(btAddr)


    def information(self, btAddr: list = []):
        """Fetch information about a bluetooth adress

        Parameters
        ----------
        btAddr
            Default: []
            Type: List
            Description: List of Bluetooth adressess

        Returns
        -------
        List
            Type: List
            Content: Dict
            Description: Information for each inserted btAddr

            Dict content:
                - date : Scan run date => Str
                - adress : BT Adress => Str
                - valid : Is adress valid? => Bool

        Note
        ----
        If nothing is found this will return None
        """
        if self.nearby_devices:
            results=[]
            for adress in self.nearby_devices:
                info = {
                    "date": str(datetime.utcnow()),
                    "adress" : adress}
                if self.isValid(adress):
                    info["valid"] = True
                    info["name"] = bluetooth.lookup_name(adress)
                    results.append(info)
                del info # clean memory
            return results
        else:
            self.__logger.warning("No devices found to fetch information from")
            return None


    def scan(self):
        """Scan fetched nearby devices, when this class gets initialized it 
        scans once. This take up about 10 seconds. If no other method is declared
        this method scans the devices which where gathered while initializing.

        If however `discover` for example is used then this method will scan
        those results.

        Returns
        -------
        List
            Type: List
            Content: Same content as the method `information` returns
        """
        info = self.information(self.nearby_devices)
        # TODO expand device information
        return info


    def run_until_discovered(self, duration=10):
        """Runs until bluetooth device is discovered.
        When a device is found execute the `scan` method.

        Parameters
        ----------
        duration
            Default: 10
            Type: int
            Description: The duration of the time to search for new devices

        Note
        ----
        You can set the duration for each search in this method. You cannot
        time the duration of the full discovery. This method ONLY returns
        when a discovery has been made.

        Returns
        -------
        List
            Type: List
            Content: Same content as the method `information` returns
        """
        self.__discovering = True
        while self.__discovering:
            self.discover(duration=duration)
        return self.scan()

