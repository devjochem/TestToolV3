import subprocess
import re


def run_dmidecode():
    try:
        return subprocess.check_output(['sudo', 'dmidecode'], text=True)
    except subprocess.CalledProcessError as e:
        print("Failed to run dmidecode:", e)
        return ""


def get_block(output, block_name):
    blocks = output.split('\n\n')
    for block in blocks:
        if block_name in block:
            return block
    return ""


def get_serial_number(output):
    chassis = get_block(output, "Chassis Information")
    system_type = re.search(r"Type:\s*(.+)", chassis).group(1).strip().lower()
    if "desktop" in system_type:
        base_board = get_block(output, "Base Board Information")
        match = re.search(r"Serial Number:\s*(.+)", base_board)
    else:
        system_info = get_block(output, "System Information")
        match = re.search(r"Serial Number:\s*(.+)", system_info)
    return match.group(1).strip() if match else "Not found"

def get_manufacturer(output):
    chassis = get_block(output, "Chassis Information")
    system_type = re.search(r"Type:\s*(.+)", chassis).group(1).strip().lower()
    if "desktop" in system_type:
        base_board = get_block(output, "Base Board Information")
        match = re.search(r"Manufacturer:\s*(.+)", base_board)
    else:
        system_info = get_block(output, "System Information")
        match = re.search(r"Manufacturer:\s*(.+)", system_info)
    return match.group(1).strip() if match else "Not found"


def get_model(output):

    chassis = get_block(output, "Chassis Information")
    system_type = re.search(r"Type:\s*(.+)", chassis).group(1).strip().lower()
    if "desktop" in system_type:
        base_board = get_block(output, "Base Board Information")
        match = re.search(r"Product Name:\s*(.+)", base_board)
    else:
        system_info = get_block(output, "System Information")
        manufacturer = get_manufacturer(output).lower()
        if "lenovo" in manufacturer:
            # For Lenovo, use Version instead of Product Name
            match = re.search(r"Version:\s*(.+)", system_info)
            if match:
                return match.group(1).strip()
    # Default to Product Name
        match = re.search(r"Product Name:\s*(.+)", system_info)
    return match.group(1).strip() if match else "Not found"


def get_cpu_info(output):
    cpu_blocks = [blk for blk in output.split('\n\n') if "Processor Information" in blk]
    cpus = []
    for block in cpu_blocks:
        match = re.search(r"Version:\s*(.+)", block)
        if match:
            cpus.append(match.group(1).strip())
    return ", ".join(cpus) if cpus else "Not found"

def get_memory(output):
    memory_info = get_block(output, "Memory Device Mapped Address")
    match = re.search(r"Range Size:\s*(.+)", memory_info)
    return match.group(1).strip() if match else "Not found"

def get_memory_info(output):
    memory_blocks = [blk for blk in output.split('\n\n') if "Memory Device" in blk]
    total_mb = 0

    for block in memory_blocks:
        # Skip if not installed or reserved
        if "No Module Installed" in block or "Type: Reserved" in block:
            continue

        if "Size:" not in block:
            continue

        size_mb = 0
        match_mb = re.search(r"Size:\s*(\d+)\s*MB", block)
        if match_mb:
            size_mb = int(match_mb.group(1))
        else:
            match_gb = re.search(r"Size:\s*(\d+)\s*GB", block)
            if match_gb:
                size_mb = int(match_gb.group(1)) * 1024

        if 0 < size_mb < 131072:  # Ignore > 128 GB as likely bogus
            total_mb += size_mb

    return f"{total_mb} MB ({total_mb // 1024} GB)" if total_mb else "No memory found"

