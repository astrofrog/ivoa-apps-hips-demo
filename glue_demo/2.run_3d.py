from glue_astronomy.data.hips import HiPSData
from glue.core import DataCollection
from glue_qt.app.application import GlueApplication

d = HiPSData("https://alasky.cds.unistra.fr/GALFAHI/GALFAHI-Narrow-DR2-3D/", label="GALFA")
dc = DataCollection([d])
ga = GlueApplication(dc)
ga.start(maximized=False)
