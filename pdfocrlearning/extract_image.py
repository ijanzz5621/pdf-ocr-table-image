import fitz
import PIL.Image
import io

def start():
    pdf = fitz.open("data/sample.pdf")

    counter = 1

    for i in range(len(pdf)):
        page = pdf[i]
        images = page.get_images()
        for image in images:
            base_img = pdf.extract_image(image[0])
            #print(base_img["width"])
            image_data = base_img["image"]
            img = PIL.Image.open(io.BytesIO(image_data))
            ext = base_img["ext"]
            img.save(open(f"results/image{counter}.{ext}", "wb"))
            counter += 1