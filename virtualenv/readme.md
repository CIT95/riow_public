Mac Install

Step 1: install 
    pip3 install virtualenv
Step 2: make a directory for your code that needs external libraries
    mkdir nameofdir (virtualenv)
    change into that directory
Step 3: Create a new virtual environment inside the directory
    virtualenv venv --python=python3
Step 4: Activate virtual enivornment
    source venv/bin/activate      
    You know it worked if you terminal changes to the name of the virtual environment
Step 5: Install libraries that your code will require
    I'll install https://pypi.org/project/pyfiglet/0.7/
Step 6: Freeze and create requirements.txt
    pip freeze > requirements.txt
Step 6: Deactivate 
    deactivate
