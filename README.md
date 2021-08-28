## README

To run the program:

```
pip install tornado

python server_launch.py
```

http://localhost:5000 will open in your browser, or open in yourself.


Main code will go into "mainprog.py" in computeThis() function.

A dict "configD" will be passed to the function. It will have:
```
{
"attachment" : [uploaded file's filename],
"maxDelay": __
"maxRunning": __
"travelTime": __
}
```

In computeThis() function, append all logs to `logs` list. That will go to output. Any other metrics, summary data you want to show in frontend, pls include in the `returnD` dict.

## Windows Binary .exe creation

Run these commands

```
conda env remove -n exe
conda create -n exe python=3 --yes
activate exe
pip install pypiwin32 pyinstaller
pip install numpy pandas tornado styleframe matplotlib pycopy-bisect
pyinstaller --hidden-import pandas._libs.tslibs.timedeltas --add-data=index.html;. --clean --onefile server_launch.py
move "dist\server_launch.exe" .\
rmdir /s /q "dist" "build" "__pycache__"
```

First line is to remove the virtual env in case you have created it once already and are doing this again. Skip if doing for first time.

After running this, "server_launch.exe" should appear in the main folder. If you want to rename this, then rename the server_launch.py accordingly and change it in the pyinstaller command above.

You can distribute the generated single .exe file to end users - no need to carry anything else along.


## Getting Outputs from binary 
Due to sandboxing security features, the binary runs in a system temp folder. When the program closes, the temp folder is destroyed.

To save the outputs created in the two output folders, we're zipping them up and adding links in the webpage for user to download once the backend has done its work. So, user does not need to go to the program's folder to retrieve outputs, they can get it straight from the frontend.

We could try to make the program save the outputs in some other location, but that will most probably incur the wrath of the Windows security settings : User will experience everything on screen going dark and be shown the "are you sure.." permission screen that only admins can accept. And it'll all look very suspicious. Better to stay in line.

