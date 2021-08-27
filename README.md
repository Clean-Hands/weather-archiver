# weather-archiver
Requests weather data from weather.gov from the specified latitude and longitude and saves the information as a .json file, along with the given image.

## Usage
You can run the program in Command Prompt or PowerShell and pass the latitude and longitude to get the current weather for the specified location.
The layout is `weather.py [latitude] [longitude]`, with an example execution looking like this: `weather.py 40.730610 -73.935242`.

If nothing is passed, it will default to latitude: `44.918355000000076`, longitude: `-93.32269499999995`, also known as Minneapolis, MN.

If you would like the weather dumps to be stored in a location other than the directory `weather.py` is in, you can pass a third argument with the desired destination. With this third argument added, the layout looks like `weather.py [latitude] [longitude] [location]`, and an example execution looks something like this: `weather.py 40.730610 -73.935242 C:\Users\ExampleUser\Desktop`.

If there are spaces anywhere in the path, the path needs to be in quotes, as shown here: `weather.py 40.730610 -73.935242 "C:\Users\Example User\Desktop"`.

## Loading Data

[weather-loader](https://github.com/Clean-Hands/weather-loader) can be used to load data downloaded by the weather-archiver.
