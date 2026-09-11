# -*- coding: utf-8 -*-
"""Flatten the photographed certificate pages: remove the paper/shadow
background, lift the text, crop to the sheet."""
import os
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps

SRC = 'assets/certs/hires'
DST = 'assets/certs/clean'
os.makedirs(DST, exist_ok=True)

NAMES = ['cert_1_hawes_01jul2024', 'cert_2_pang_07aug2024',
         'cert_3_hawes_11aug2024', 'cert_4_hawes_08sep2024']

# the two free-text lines in Part B that narrate the workplace, in the
# coordinates of the cleaned and cropped sheet
REDACT = {
    'cert_1_hawes_01jul2024': [(624, 646, 942, 700), (650, 724, 1678, 782)],
    'cert_2_pang_07aug2024':  [(646, 658, 950, 732), (686, 734, 1548, 814)],
    'cert_3_hawes_11aug2024': [(576, 766, 870, 816), (600, 841, 1502, 892)],
    'cert_4_hawes_08sep2024': [(734, 856, 1038, 922), (770, 941, 1678, 1022)],
}


def background(im, small_w=520, mx=7, blur=9):
    """Estimate the paper tone: dilate away the ink, then smooth."""
    w, h = im.size
    sm = im.resize((small_w, max(1, int(h * small_w / w))), Image.BILINEAR)
    sm = sm.filter(ImageFilter.MaxFilter(mx))
    sm = sm.filter(ImageFilter.GaussianBlur(blur))
    return sm.resize((w, h), Image.BICUBIC)


def levels(im, black, white, gamma=1.0):
    lut = []
    for v in range(256):
        t = (v - black) / float(white - black)
        t = 0.0 if t < 0 else (1.0 if t > 1 else t)
        lut.append(int(round((t ** gamma) * 255)))
    return im.point(lut)


def sheet_box(im, pad=14):
    """Bounding box of everything that is not the flat white surround."""
    mask = im.point(lambda v: 255 if v < 238 else 0)
    mask = mask.filter(ImageFilter.MaxFilter(9))
    bb = mask.getbbox()
    if not bb:
        return (0, 0) + im.size
    w, h = im.size
    return (max(0, bb[0] - pad), max(0, bb[1] - pad),
            min(w, bb[2] + pad), min(h, bb[3] + pad))


for n in NAMES:
    im = Image.open(os.path.join(SRC, n + '_raw.png')).convert('L')
    # strip the bundle footer line printed at the foot of the page
    w0, h0 = im.size
    im.paste(255, (0, h0 - 130, w0, h0))
    bg = background(im)
    # divide out the paper: white where the sheet is bare, dark where ink sits
    flat = ImageChops.invert(ImageChops.subtract(bg, im))
    flat = levels(flat, 118, 232, gamma=1.28)
    flat = ImageOps.autocontrast(flat, cutoff=(0.02, 0.0))
    flat = flat.filter(ImageFilter.UnsharpMask(radius=1.6, percent=95, threshold=3))
    flat = flat.crop(sheet_box(flat))
    d = ImageDraw.Draw(flat)
    for box in REDACT[n]:
        d.rectangle(box, fill=0)
    flat.save(os.path.join(DST, n + '.png'))
    print(n, flat.size)
