from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from lib.systemspecs import Specs


def create_table_pdf(filename, customer_name, specdatas, diskdatas ,testdatas, visualdatas):
    # Set up the document
    doc = SimpleDocTemplate(filename, pagesize=LETTER)
    elements = []
    styles = getSampleStyleSheet()
    centered_style = ParagraphStyle(
        name="Centered",
        parent=styles["Normal"],
        alignment=TA_CENTER
    )

    # Title
    title = Paragraph("Jochem's TestTool Report", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Testers name

    customer_info = Paragraph(f"<b>Naam Tester:</b> {customer_name}", centered_style)
    elements.append(customer_info)
    elements.append(Spacer(1, 12))

    # Table data (header + items)
    specdata = [["", ""]]
    diskdata = [["Type", "Schijf","Grootte"]]
    testdata = [["Test", "Resultaat"]]
    visualdata = [["Onderdeel", "Resultaat"]]

    # Populate table rows
    for item in specdatas:

        if item[0] == "GPU's":
            specdata.append(["Gpu's", item[1]])
            if len(item) > 2:
                for gpu in item[2:]:
                    specdata.append(["", gpu])
        else:
            part, result = item
            specdata.append([part, result])


    for item in diskdatas:
        t, name, size = item
        diskdata.append([t ,name, size])

    # Populate table rows
    for item in testdatas:
        if item[0] == "Batterij Health":
            testdata.append(["Batterij Health", item[1]])
            if len(item) > 2:
                for bat in item[2:]:
                    testdata.append(["", bat])
        else:
            test, result = item
            testdata.append([test, result])

    # Populate table rows
    for item in visualdatas:
        check, result = item
        visualdata.append([check, result])

    # Create table
    spectable = Table(specdata, colWidths=[100, 500, 60, 80, 80])
    spectable.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (2, 1), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
    ]))

    # Create table
    disktable = Table(diskdata, colWidths=[40, 500, 60, 80, 80])
    disktable.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (2, 1), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
    ]))

    # Create table
    testtable = Table(testdata, colWidths=[100, 500, 60, 80, 80])
    testtable.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (2, 1), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
    ]))

    # Create table
    visualtable = Table(visualdata, colWidths=[100, 500, 60, 80, 80])
    visualtable.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (2, 1), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
    ]))

    elements.append(spectable)
    elements.append(Spacer(1, 12))
    elements.append(disktable)
    elements.append(Spacer(1, 12))
    elements.append(testtable)
    elements.append(Spacer(1, 12))
    elements.append(visualtable)

    # Build PDF
    doc.build(elements)


def createspecs():

    key_map = {
        "vendor": "Merk",
        "model": "Model",
        "serial": "Serial",
        "ram": "Ram",
        "resolution": "Resolutie",
        "gpu": "GPU's"
    }

    systemspec = []

    for key, label in key_map.items():
        value = Specs().getSpecs().get(key, "Not tested")

        # Handle empty lists, None, or empty strings
        if not value:
            value = "Not detected"
        elif isinstance(value, list):
            value = ", ".join(str(v) for v in value) if value else "Not detected"

        systemspec.append((label, value))

    disks = []
    data = Specs().getSpecs().get("disks")
    for disk in data:
        disks.append((disk['type'], disk['model'], f"{disk['size_gb']} GB"))
    return systemspec, disks

def format_test_data(data):

    key_map_test = {
        "LCD": "Scherm",
        "KB": "Keyboard",
        "CAM": "Camera",
        "AUDIO": "Geluid",
        "BAT": "Batterij Health"
    }

    finaldata = []

    for key, label in key_map_test.items():
        value = data.get(key, "Not tested")
        if key == "AUDIO":
            speakers = "Goed" if value['LEFT_SPEAKER'] and value['RIGHT_SPEAKER'] else "Kapot"
            finaldata.append([label, speakers])
            finaldata.append(["Microfoon", "Goed" if value['MIC'] else "Kapot"])
        else:
            # Handle empty lists, None, or empty strings
            if not value:
                value = "Not detected"
            elif isinstance(value, list):
                value = ", ".join(str(v) for v in value) if value else "Not detected"

            finaldata.append((label, value))

    key_map_visual = {
        "back": "Backcover",
        "bezel": "Bezel",
        "side": "Zijkanten",
        "bot": "Bottomcover",
    }

    visual = []
    for key, label in key_map_visual.items():
        value = data['VISUAL'][key]

        # Handle empty lists, None, or empty strings
        if not value:
            value = "Not tested"
        elif isinstance(value, list):
            value = ", ".join(str(v) for v in value) if value else "Not tested"

        visual.append((label, value))
    return finaldata, visual

def generate_report(name ,data):

    print(data)
    testdata, visualdata = format_test_data(data)

    specs, disks = createspecs()

    print(testdata)
    print(visualdata)

    create_table_pdf("data.pdf", name, specs, disks, testdata, visualdata)

# Example usage
test = [
    ("Toetsenbord", "Not tested"),
    ("Scherm", "Not tested"),
    ("Camera", "Not tested"),
    ("Geluid", "Not tested"),
    ("Batterij Health", "Not detected")
]

visual = [
    ("Achterkant Scherm", "Not checked"),
    ("Bezel", "Not checked"),
    ("Palmrest", "Not checked"),
    ("Zijkanten", "Not checked"),
    ("Onderkant", "Not checked")
]