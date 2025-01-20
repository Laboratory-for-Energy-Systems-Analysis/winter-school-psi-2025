# INSTRUCTIONS BEFORE ARRIVAL

Please follow the below instructions before arriving at the course.
If you encounter any issues, please contact us, and we will troubleshoot, so that you can arrive with everything set up on your computer.
For those arriving Sunday already at the hotel, Romain and Alvaro will also be there to have a look at anything which doesn't work. 
Please absolutely make sure that everything works, so that we can start right away on Monday with the content instead of technical troubleshooting.



# WORK ON SERVERS vs. LOCAL MACHINES

You will set up everything on your local machine, instead of us providing a consistent and working server for the duration of this course. 
Why? Because you will also not work on a nicely set up server at home, but with your own machine. Thus we don't want to create an artificial 
environment for you during the course, but give you the chance to set up everything such that you can go home and continue with the work.

> **_NOTE:_**  We however recommend to have at least 8GB of RAM on your computer, as some of the calculations can be quite memory-intensive.

# ANACONDA AND GIT

We ask the participants to download and install Anaconda (or the 
Python environments manager of your choice) and Git 
before the course:

- Anaconda: https://www.anaconda.com/products/distribution
- Git: https://git-scm.com/downloads

We recommend using homebrew to install Git on Mac:

```bash
  brew install git
```

For Windows users, you can download teh Git installer from the link above (you most likely
need the 64-bit version).

## Change the Anaconda solver

Once you have installed Anacoda on your computer, you may consider installing 
the `libmamba` solver in conda, for faster environment resolution.
Open the terminal (Anaconda terminal in Windows, or Terminal on Mac) 
and run the following commands:

```bash
  conda install -n base conda-libmamba-solver
  conda config --set solver libmamba
```

## Clone this repository

Option A: Download github desktop, click to clone a repository, and paste the link of the repository shown further below.

Option B: 
Using your Windows/Mac terminal, navigate to the folder where you want 
to store the course material.For example, you can create a folder 
called `winter-school-2025` in your `Documents` folder. To navigate to 
the `Documents` folder, you can run the following command:

```bash
  cd Documents
```

To go back to the previous folder, you can run the following command:

```bash
  cd ..
```

If you want to create a new folder, you can run the following command:

```bash
  mkdir winter-school-2025
```

Once you are in the folder of your choice, you can **clone** this Github repository 
using Git onto your computer by running the following command in your terminal:

```bash
  git clone https://github.com/Laboratory-for-Energy-Systems-Analysis/winter-school-psi-2025.git
```

You can now navigate to the `winter-school-dds-psi-2025` folder and 
access its content on your computer.

## Environments setup

When you will do exercises on your computer, you will use a number of libraries
that are not installed by default in Anaconda. To make sure you have all the
necessary libraries, we will create Anaconda **environments** for you, using
**recipes** that we have prepared.

We have prepared four recipes which install four different environments:
- `bw25_env_xxx.yaml`: it will install the `brightway` library  as well as `temporalis`
- `wurst_env_xxx.yaml`: it will install the `wurst` library and its dependencies
- `premise_env.yaml`: it will install the `premise` library and its dependencies as well as `activity-browser`
- `odym_env.yaml`: it will install the `odym` library and its dependencies

After running the recipe files, you will have four environments on your computer:
- `wurst`
- `premise`
- `bw25`
- `odym`

Here is how to install these environments:

Using your terminal, navigate to the `environments` folder of the repository:

```bash
  cd winter-school-dds-psi-2025/envs
```

Then, run the following command to create the `wurst` environment:

If you use Windows or Mac with an Intel processor:

```bash
  conda env create -f wurst_env_win64.yaml
```

If you use Mac with an M1/2/3/4 processor:

```bash
  conda env create -f wurst_env_osxARM.yaml
```

This will create a conda environment called `wurst` with all the required dependencies.

Then, run the following command to create the `premise` environment:

```bash
  conda env create -f premise_env.yaml
```

This will create a conda environment called `premise` with all the required dependencies.

Then, run the following command to create the `odym` environment:

```bash
  conda env create -f odym_env.yaml
```

This will create a conda environment called `odym` with all the required dependencies.

Finally, run the following command to create the `bw25` environment:

On Windows or Mac with an Intel processor:


```bash
  conda env create -f bw25_env_win64.yaml
```

On a Mac with an M1/2/3/4 processor:

```bash
  conda env create -f bw25_env_osxARM.yaml
```

This will create a conda environment called `bw25` with all the required dependencies.

You can check that the environments have been created by running the following command:

```bash
  conda env list
```

You should see the four environments listed in the terminal (plus the `base` environment).

You can activate an environment by running the following command:

```bash
  conda activate wurst
```

and check the installed packages by running:

```bash
  conda list
```

## Installing Activity Browser

The installation of AB is basically also simply the creation of an environment which is called "ab", and which contains the activity browser package (and all related packages required to run AB). 
Please follow the installation instructions given here: https://github.com/LCA-ActivityBrowser/activity-browser

## Ecoinvent database

Also, please acquire credentials (username and password) to 
download the [ecoinvent](https://ecoinvent.org) database. Ask the person in charge of your group/university to get these credentials. Or ask the ecoinvent support if you can't find out in-house.

We will be using the ecoinvent 3.10 cut-off database for the course.

# Code editor

We recommend using **PyCharm** or **Visual Studio Code** as an IDE (Integrated Development Environment) for the course.
Both are free (Community edition) and have a lot of features that will 
help you during the course.



