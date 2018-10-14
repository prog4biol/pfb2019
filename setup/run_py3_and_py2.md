This is how you can run multiple versions of python on your system. 

Please substitute py3.6 for the most up to date python version and py2.7.13 for the most current py2 version.


- download and install python 3 from anaconda https://www.anaconda.com/download/#macos
- `conda create -n py3.6`
- `conda search python`
-  locate the most recent version of python 2. At this writing it was 2.7.13
- `conda create -n py2.7.13 python=2.7.13`

now you can "activate" either python3 or python2 by typing"
  - `source activate py2.7.13` for python 2
  - `source activate py3.6` for python 3

and deactivate by typing
- `source deactivate` for each

Make sure to activate python3
- `source activate py3.6`

set up your mirror or "channel" for downloading packages
- `conda config --add channels bioconda`
- `conda config --add channels anaconda`

search for a package
- `conda search biopython`

install a package
- ` conda install -n py3.6 biopython=1.70`

To list your environments
`conda info --envs`

If the package you want to install is not found by the `conda search` or the most recent version is not present and you need to install with pip
- `source activate py3.6`
- `pip install package`
