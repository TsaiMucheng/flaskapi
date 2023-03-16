### CORS Experiment
* api1 CORS trigger
* api2 no CORS

#### Manual set ENV
``` bash
conda create -n flask python=3.9 flask=2.2.3
```
#### Export ENV
``` bash
conda activate flask
conda env export > environment.yml
```
#### Flask run env
``` bash
conda activate flask
cd $BASE_PATH
flask run --host $HOST_SERVER --port $PORT
```