import os
import shutil

from reproject import reproject_interp
from reproject.hips import reproject_to_hips

if os.path.exists("GLIMPSE_hips"):
    shutil.rmtree("GLIMPSE_hips")

reproject_to_hips(
    "GLM_33000+0000_mosaic_I4.fits",
    output_directory="GLIMPSE_hips",
    reproject_function=reproject_interp,
    coord_system_out="equatorial",
    threads=True,
    level=6,
    properties={"hips_pixel_cut": "-5 100"},
)
