import fitz
import os

pdf_path = r"C:\Users\tsotl\Downloads\JOURNALS_21001137_AIDING SYSTEM FOR VISUALLY IMPAIRED INDIVIDUALS (1).pdf"
out_dir = r"C:\Users\tsotl\aiding-system-visually-impaired\paper\figures"

doc = fitz.open(pdf_path)
img_count = 0

for page_num in range(len(doc)):
    page = doc[page_num]
    image_list = page.get_images(full=True)
    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        ext = base_image["ext"]
        img_count += 1
        fname = os.path.join(out_dir, f"fig_p{page_num+1}_{img_index+1}.{ext}")
        with open(fname, "wb") as f:
            f.write(image_bytes)
        print(f"Saved: fig_p{page_num+1}_{img_index+1}.{ext}  ({len(image_bytes)} bytes)")

print(f"\nTotal images extracted: {img_count}")
doc.close()
