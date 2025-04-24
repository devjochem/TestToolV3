from PySide6.QtDBus import QDBusConnection, QDBusInterface, QDBusArgument
from PySide6.QtCore import QCoreApplication


class UPowerManager:
    def __init__(self):
        self.UPOWER_NAME = "org.freedesktop.UPower"
        self.UPOWER_PATH = "/org/freedesktop/UPower"
        self.DBUS_PROPERTIES = "org.freedesktop.DBus.Properties"
        self.BUS = QDBusConnection.systemBus()

    def enumerate_devices(self):
        upower_iface = QDBusInterface(
            self.UPOWER_NAME,
            self.UPOWER_PATH,
            self.UPOWER_NAME,
            self.BUS
        )

        reply = upower_iface.call("EnumerateDevices")
        if reply.errorName():
            print("D-Bus Error:", reply.errorMessage())
            return []

        if not reply.arguments():
            return []

        # Proper handling of QDBusArgument array response
        dbus_arg = reply.arguments()[0]
        if not isinstance(dbus_arg, QDBusArgument):
            return []

        devices = []
        dbus_arg.beginArray()
        while not dbus_arg.atEnd():
            item = dbus_arg.asVariant()
            if hasattr(item, 'path'):  # QDBusObjectPath
                devices.append(item.path())
            else:
                # For non-object path items, try to get the value
                try:
                    devices.append(str(item.variant()))
                except AttributeError:
                    devices.append(str(item))
        dbus_arg.endArray()

        return devices

    def get_device_property(self, device_path, property_name):
        props_iface = QDBusInterface(
            self.UPOWER_NAME,
            device_path,
            self.DBUS_PROPERTIES,
            self.BUS
        )

        reply = props_iface.call("Get", "org.freedesktop.UPower.Device", property_name)
        if reply.errorName():
            print(f"Error getting {property_name}:", reply.errorMessage())
            return None

        if not reply.arguments():
            return None

        # Proper unwrapping of QDBusVariant
        result = reply.arguments()[0]
        while hasattr(result, 'variant'):
            result = result.variant()

        return result

    def print_battery_info(self, device_path):
        properties = {
            "Vendor": ("Charge Level", lambda x: f"{x}"),
            "Model": ("Charge Level", lambda x: f"{x}"),
            "Percentage": ("Charge Level", lambda x: f"{float(x):.1f}%"),
            "Capacity": ("Health", lambda x: f"{float(x):.1f}%"),
            "State": ("Status", lambda x: {
                1: "Charging",
                2: "Discharging",
                4: "Fully charged",
                0: "Unknown"
            }.get(int(x), f"Unknown ({x})")),
            "TimeToEmpty": ("Time remaining", lambda x: f"{int(x) // 60} minutes" if int(x) > 0 else "Calculating..."),
            "Energy": ("Current energy", lambda x: f"{float(x):.2f} Wh"),
            "EnergyFull": ("Full capacity", lambda x: f"{float(x):.2f} Wh"),
            "EnergyFullDesign": ("Full design", lambda x: f"{float(x):.2f} Wh"),
            "Voltage": ("Voltage", lambda x: f"{float(x):.3f} V"),
            "EnergyRate": ("Charge rate", lambda x: f"{float(x):.3f} W")
        }

        data = {}
        for prop, (desc, formatter) in properties.items():
            value = self.get_device_property(device_path, prop)
            if value is not None:
                try:
                    #print(f"{desc}: {formatter(value)}")
                    data[prop] = formatter(value)
                except (ValueError, TypeError) as e:
                    print(f"{desc}: [Error: {str(e)}]")
                    return None
        return data
