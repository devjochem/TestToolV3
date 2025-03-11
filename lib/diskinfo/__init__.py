#
#    Package `diskinfo`
#    Peter Sulyok (C) 2022-2024.
#
from lib.diskinfo.disksmart import DiskSmartData, SmartAttribute, NvmeAttributes
from lib.diskinfo.disktype import DiskType
from lib.diskinfo.partition import Partition
from lib.diskinfo.disk import Disk
from lib.diskinfo.diskinfo import DiskInfo

__all__ = ["DiskType", "Partition", "DiskSmartData", "SmartAttribute", "NvmeAttributes", "Disk", "DiskInfo",
           "_read_file", "_read_udev_property", "_read_udev_path", "size_in_hrf", "time_in_hrf"]

from lib.diskinfo.utils import _read_file, _read_udev_property, _read_udev_path, size_in_hrf, time_in_hrf
