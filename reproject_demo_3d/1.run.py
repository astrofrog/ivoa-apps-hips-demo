import os
import shutil

from reproject import reproject_interp
from reproject.hips import reproject_to_hips

if os.path.exists("VLA_NGC247_hips"):
    shutil.rmtree("VLA_NGC247_hips")

reproject_to_hips(
    "VLA_NGC247.fits",
    output_directory="VLA_NGC247_hips",
    reproject_function=reproject_interp,
    coord_system_out="equatorial",
    threads=True,
    level=6,
)
