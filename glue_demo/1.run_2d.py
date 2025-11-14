from glue_astronomy.data.hips import HiPSData
from glue.core import DataCollection
from glue_qt.app.application import GlueApplication

d1 = HiPSData("https://alasky.cds.unistra.fr/2MASS/K/", label="2MASS K")
d2 = HiPSData("https://alasky.cds.unistra.fr/WISE/W1/", label="Wise 1")
d3 = HiPSData("http://cade.irap.omp.eu/documents/Ancillary/4Aladin/IRIS_2/", label="IRAS 25")
dc = DataCollection([d1, d2, d3])
ga = GlueApplication(dc)
ga.load_data("../reproject_demo_2d/GLM_33000+0000_mosaic_I4.fits")
ga.start(maximized=False)
