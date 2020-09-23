# VirtualEnv Workflow
https://docs.python.org/3/library/venv.html

## Developer Steps 

1.  Create a new virtual environment inside the directory
    <code>python3 -m venv dirname</code>
2. add .gitignore <br>in the dirname and place * in that file to not have any of the files tracked int his folder    
3. Activate virtual enivornment</br>
    <code>source dirname/bin/activate </code>      
    You know it worked if you terminal changes to the name of the virtual environment
4. Install libraries that your code will require. </br>
    I'll install https://pypi.org/project/pyfiglet/0.7/
    Write your own code
5. Freeze and create requirements.txt
    Once all your coding is complete and you are ready to share your code do this step.<br>

    <code>pip freeze > requirements.txt</code>
6. Deactivate <br>
    <code>deactivate</code>

## User

1. Clone the repo locally
2. Complete Steps 1, 2 and 3<br>
Make sure you have a virtual enivornment before doing the next step. If you don't the libraries will install globally.

3. Install required libraries <br>
<code>pip3 install -r requirements.txt</code>
4. Run python file 

5. Decativate the virtualenv <br>
<code>deactivate</code>
