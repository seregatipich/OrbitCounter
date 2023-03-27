# OrbitCounter

This is a simple script that uses NASA's open data to draw an orbit of ISS around Earth. The data was obtained from https://data.nasa.gov/browse?q=ISS+COORDS.

## Installation

To run this script on your computer, follow these steps:

1. Clone the repository using the command
```
git clone git@github.com:seregatipich/OrbitCounter.git
``` 
2. Navigate to the application directory using the command
```
cd OrbitCounter
``` 
3. Create virtual environment
```
python -m venv venv
```
4. Activate virtual environment
```
source venv/Scripts/activate
```
or
```
source venv/bin/activate
```
5. Install the dependencies from requirements.txt
```
pip install -r requirements.txt
```

## Usage

1. Run the application using the command
```
python main.py
```
2. After the script processes the ISS orbit data, it will output the 3D model of ISS's orbit.

## License

This project is licensed under the MIT License. You are free to use it in your projects.
