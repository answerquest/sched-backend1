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

## Binary

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

First line is to remove the virtual env in case you have created it once already and are doing this again.
