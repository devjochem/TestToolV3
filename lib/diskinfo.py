import json
import logging
import subprocess


class Disks:
    def __init__(self):
        self.disks = []
        self.logger = logging.getLogger()
        self.getData()


    def getData(self):
        try:
            result = subprocess.run(
                ['lsblk', '-b', '-J', '-o', 'NAME,TYPE,TRAN,RM,SIZE,MODEL,VENDOR'],
                capture_output=True,
                text=True,
                check=True
            )
            data = json.loads(result.stdout)

            for device in data.get('blockdevices', []):
                name = device.get('name') or ''
                dtype = device.get('type') or ''
                tran = device.get('tran') or ''
                rm = device.get('rm', False)
                size = device.get('size')
                model = (device.get('model') or '').strip()

                # Skip invalid or irrelevant devices
                if dtype != 'disk':
                    continue
                if name.startswith(('loop', 'zram')):
                    continue
                if tran == 'usb':
                    continue
                if rm:
                    continue
                if size is None:
                    continue  # Size is required

                # Determine if SSD or HDD
                rotational_path = f"/sys/block/{name}/queue/rotational"
                try:
                    with open(rotational_path, 'r') as f:
                        rotational = f.read().strip()
                        device_type = 'HDD' if rotational == '1' else 'SSD'
                except Exception:
                    device_type = 'Unknown'

                self.disks.append({
                    'path': f"/dev/{name}",
                    'size_gb': round(int(size) / (1024 ** 3), 2),
                    'model': model or 'Unknown',
                    'type': device_type
                })

            return self.disks

        except subprocess.CalledProcessError as e:
            self.logger.error(f"lsblk failed: {e}")
            return []
        except json.JSONDecodeError:
            self.logger.error("Failed to parse lsblk output")
            return []
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
            return []

    def get(self):
        return self.disks
