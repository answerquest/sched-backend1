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