#
#    Package `diskinfo`
#    Peter Sulyok (C) 2022-2024.
#
from testtool.lib.diskinfo.disksmart import DiskSmartData, SmartAttribute, NvmeAttributes
from testtool.lib.diskinfo.disktype import DiskType
from testtool.lib.diskinfo.partition import Partition
from testtool.lib.diskinfo.disk import Disk
from testtool.lib.diskinfo.diskinfo import DiskInfo

__all__ = ["DiskType", "Partition", "DiskSmartData", "SmartAttribute", "NvmeAttributes", "Disk", "DiskInfo",
           "_read_file", "_read_udev_property", "_read_udev_path", "size_in_hrf", "time_in_hrf"]

from testtool.lib.diskinfo.utils import _read_file, _read_udev_property, _read_udev_path, size_in_hrf, time_in_hrf
