from reproject import reproject_interp
from reproject.hips import hips_as_dask_array

from astropy.io import fits

array, wcs = hips_as_dask_array("https://alasky.cds.unistra.fr/2MASS/K/", level=7)

header = fits.getheader("GLM_33000+0000_mosaic_I4.fits")
header['NAXIS1'] = 1000
header['NAXIS2'] = 1000

final_array, final_footprint = reproject_interp((array, wcs), header)

fits.writeto('reprojected.fits', final_array, overwrite=True)
