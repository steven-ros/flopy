import shutil
import os
import numpy as np
import flopy
from flopy.export.vtk import Vtk

cpth = os.path.join('temp', 't050')
# delete the directory if it exists
if os.path.isdir(cpth):
    shutil.rmtree(cpth)
# make the directory
os.makedirs(cpth)


def test_vtkoutput():

    ml = flopy.modflow.Modflow()
    dis = flopy.modflow.ModflowDis(ml, nlay=3, nrow=3, ncol=3, top=0,
                                   botm=[-1., -2., -3.])
    ibound = np.ones((3, 3, 3), dtype=np.int)
    ibound[0, 1, 1] = 0
    bas = flopy.modflow.ModflowBas(ml, ibound=ibound)

    fvtkout = os.path.join(cpth, 'test.vtu')
    vtkfile = Vtk(fvtkout, ml)
    vtkfile.write(ibound_filter=True)


if __name__ == '__main__':
    test_vtkoutput()
