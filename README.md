# Gaussian RealTime Parse 

Gaussian RealTime Parse is a suite of Python scripts to ease the
post-processing of Gaussian Real-Time TDDFT and Ehrenfest dynamics output.

## Installation

### Dependencies

 * numpy
 * matplotlib
 * scipy
 * future

The easiest way to make sure you have these dependencies is to run
`$ pip install -r requirements.txt --user`

### Instructions

Assuming you have all the dependencies, clone the repo:
`$ git clone https://github.com/awild82/lrspectrum.git`

`setup.py` can be run the following ways:
 1. `$ python setup.py install --user`
 2. `$ ./setup.py install --user`
 3. `$ python3 setup.py install --user`
 4. `$ python2 setup.py install --user`

The first option should work regardless of platform, and is the recommended
installation option.

The second option assumes you have a python interpreter installed at
`/bin/python`. The module will be installed on that interpreter.

The third and fourth options are for python 3 or 2 specific installations.

Of course, if a system-wide installation is desired, omit the `--user` flag from
the previous instructions. 

## Quickstart

You'll probably get a better idea of what you can do just opening up some of
the scripts, but here is a basic workflow.

Say you have a RT-TDDFT output file called `rt.log`.

If you want to extract the z-dipole moment and plot it as a function of time.
You can do so like this:

```
from rtspectrum import RealTime
import matplotlib.pylot as plt

rt = RealTime('rt.log')
plt.plot(rt.time,rt.electricDipole.z)
plt.savefig('dipole.pdf')

```

This would plot the time-oscillating z-electric dipole moment
(`electricDipole.z`) as a function of time (`time`) in au. Then it saves it to
a PDF called `dipole.pdf`.

Pretty simple.

You can even plot spectra if you perturbed your system properly. Say you gave a
Cadmium atom an x-type electric delta perturbation, and saved the output in
`cd.log`.

Then this script should do the trick.

```
from rtspectrum import Spectra

cd = Spectra(x='cd.log')
cd.plot(save='cd.pdf')

```

Now you're done! You have the fourier transformed x-dipole moment (the
"spectra") saved to file `cd.pdf`.

## License

Gaussian realtime parse is licensed under the MIT license. See
[LICENSE](https://github.com/awild82/gaussian_realtime_parse/blob/master/LICENSE)
for more information.
