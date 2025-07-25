from pathlib import Path
import xml.etree.ElementTree as ET

def read_raw(path: Path) -> str | None:
    data = path.read_bytes()
    if (i := data.find(b"<?xml")) != -1:
        return data[i:].decode("utf-8", "ignore")
    sig = b"<\x00?\x00x\x00m\x00l\x00"
    if (i := data.find(sig)) != -1:
        return data[i:].decode("utf-16-le", "ignore")
    return None

def extract_products(xml_text: str) -> list[dict[str, str]]:
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return []
    room = root if root.tag.lower() == "room" else root.find("Room")
    if room is None:
        return []
    products = room.find("Products")
    if products is None:
        return []
    return [
        {
            "Job": "",
            "File": "",
            "ProdName": p.attrib.get("ProdName", ""),
            "ProductDesc": p.attrib.get("ProductDesc", ""),
            "Width": p.attrib.get("Width", ""),
            "Height": p.attrib.get("Height", ""),
            "Depth": p.attrib.get("Depth", ""),
        }
        for p in products.findall("Product")
    ]
