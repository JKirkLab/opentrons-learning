# windows setup

In order to work with the opentrons robot, it is recommended you have:
 1. python 
 2. git
 3. opentrons app
 4. vscode *(optional)*
 5. conda  *(optional)*

Both vscode and conda are optional and can be replaced by other code editors and package managers, but they are highly recommended. 

# Steps 

## Python 

### 1. Check if you have python installed by opening up windows powershell
```bash 
python --version
```
If the above command returns something, you have python installed. If not, go to https://www.python.org/downloads/

### 2. Verify Installation -- Run this in powershell
 
```bash
python --version
```
You should see something like Python 3.10.x.


## git

git is our primary version control system. 

### 1. Check if you have git installed

```bash
git --version
```

If that does not return anything, go to https://git-scm.com/downloads

### 2. Verify your git installation 

```bash
git --version
```

## opentrons app

This is the app that allows for protocol uploads to the robot 

### 1. Download the opentrons app through the following link 
https://opentrons.com/ot-app

## VS Code

This is not necessarily the code editor that you need to use, but the one I am most used to using. Any code editor will suffice. 

### 1. Download VS Code through the following link
https://code.visualstudio.com/download

## Conda

Conda is a package and environment management system. It is technically not necessary, but makes things much more convenient. 
Miniconda is a lightweight version of anaconda, and will serve our purposes just fine. 
#### 1. Download miniconda through the following link

https://www.anaconda.com/download/success

Make sure to check "Add Miniconda to my PATH" when prompted! 
Additionally, if you're on windows please use anaconda prompt instead of powershell once installed. 

