#### Create ENV with export
``` bash
cd $BASE_PATH
conda env export > environment.yml
```
#### Flask run env
``` bash
conda activate flask
flask run --host $HOST_SERVER --port $PORT
```