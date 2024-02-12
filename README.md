# ENGY502
Example and homework problem involving fastsim.

## Installing Needed Software
### Code Editor
The example code should be able to run in any major code editing software (e.g. Visual Studio Code,
Spyder, PyCharm), but NREL recommends [Visual Studio Code (VS
Code)](https://code.visualstudio.com/).  Install VS Code, and add the following plugins:
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [PyLance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)

### Python Installation
You can install Python in either of two ways:
- [Anaconda Python Distribution](https://www.anaconda.com/download/) or
  [Miniconda](https://docs.anaconda.com/free/miniconda/index.html) -- Anaconda/Miniconda seems to
  work better on Windows
- [Python 3.10](https://www.python.org/downloads/release/python-31011/) -- this works pretty well on
  Mac.  For Mac or Windows, click the link to obtain an appropriate installer.  For Mac, if you have
  [Homebrew](https://brew.sh/), you can instead use `brew install python3.10`.  For linux, run `sudo
  apt install python3.10`, `sudo dnf install python3.10`, or whatever works for your linux
  distribution.  

## Setting up your local environment
1. Place the project folder containing this readme anywhere you like (e.g. `c:\Users\<your username>\Documents\ENGY502\fastsim-hw\`)
1. Within the project folder you created above, create and activate a python enviroment (make sure
   to be consistent with the method you used to install python above):
    - Anaconda
        1. Open Anaconda Powershell Prompt or your Mac/linux terminal and run `conda create --name=engy502-env python=3.10`
        1. Activate the environment: `conda activate engy502-env`
        1. Install the dependencies: `pip install -r requirements.txt`
        1. After finishing this assigment, you can delete the environment with `conda env remove --name engy502-env` from within the same folder
    - Python3.10
        1. Open your preferred terminal environment, and run `python3.10 -m venv engy502-env`
        1. Run `source engy502-env/bin/activate` (may differ on Windows) to activate the enviroment
        1. Install dependencies: `pip install -r requirements.txt`
        1. After finishing this assignment, run `rm -rf engy502-env` to remove the enviroment

## Running the example 
Open VS Code in the project folder (whatever folder you created in step one of [Setting up your
local environment](#setting-up-your-local-environment)).  Open [example.py](example.py) as a VS Code
tab.  Click on the first line, and type `<Ctrl>+<Shift>+P` (`<Cmd>+<Shift>+P` on Mac) then type
`jupyter: run all cells` to run all of the notebook cells (marked by `# %%`) in an interactive
terminal.
