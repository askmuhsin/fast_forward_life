# fast_forward_life
imagine you could index all the information you consume digitally, and then all your future consumptions are optimized accordingly.
fast_forward_life wants to do just that for you.

### proof of concept dataset
https://docs.google.com/spreadsheets/d/1LIaC2KyH6AksUuBLusgr23xQMMM1BT6BmtFpnFbga-Q/edit?usp=sharing    
`fast_forward_life/datasets/paper_reader_demo/example_papers.csv`

```
## create a venv and install dependencies
python3 -m venv ffl_env
source ./ffl_env/bin/activate
pip install -r requirements.txt

## run the jina indexer
python app.py index

## deploy the jina search api
python app.py search


## start the demo app (not complete)
cd ./demo_app
./up
```

You can test the search api by running the following command -- 
```
curl -v -POST -H "Content-type: application/json" -d '{"top_k": 2, "data":[" The MNIST database of handwritten digits has a training set of 60,000 examples, and a test set of 10,000 examples."]}' 'http://localhost:65481/api/search'
```


Demo page is not complete atm...
![Demo page](https://github.com/askmuhsin/fast_forward_life/blob/master/elems/demo_page.png)
