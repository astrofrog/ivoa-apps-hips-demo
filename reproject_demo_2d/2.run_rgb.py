import os
import shutil

from reproject import reproject_interp
from reproject.hips import reproject_to_hips

if os.path.exists("heic1502a_hips"):
    shutil.rmtree("heic1502a_hips")

reproject_to_hips(
    "heic1502a.jpg",
    output_directory="heic1502a_hips",
    reproject_function=reproject_interp,
    coord_system_out="equatorial",
    threads=True,
)
