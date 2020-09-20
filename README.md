# fast_forward_life
imagine you could index all the information you consume digitally, and then all your future consumptions are optimized accordingly.
fast_forward_life wants to do just that for you.
All the information you consume digitally gets indexed so you don't have to repeatedly watch, read, or listen to the same piece of information.

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

# Project description
Imagine the number of times you have read or watched the same information over and over while trying to research a new topic, or while catching up on news.
What if the information you consume digitally (podcasts, videos, blogs, articles) gets chunked into bytes of information and indexed into a repository. It is as if a digital extension to your memory!
Now every time you decide to read a new paper, or watch a youtube video, or listen to that podcast on the latest diet, the media gets screened and the information bytes are searched on your personal memory repo to see if it is redundant to you or not.

This idealized version of the project needs time and effort to build, but I personally believe it has a lot of utility. it is like the opposite of recommendation, but as far as the technicalities go it is almost the same problem. 

For this hackathon, I just focused on one facet of this problem, which is dealing with technical papers, or articles. I can't list the number of times I have read about primitive data types like floats and string every time I try to learn a new programming language. It makes perfect sense for the authors to assume the reader is a beginner, but the information is redundant tome personally. This is my motivation to build a solution like this.

The ability of JINA to run a scalable streaming server for indexing data and searching data along with the advancement in feature extractors and classifiers can make this a reality. There are challenges like how to build an interface for the thousands of media platforms out there (youtube, arxiv, blogs, spotify, so on). But I believe that too is addressable.


Demo page is not complete atm...
![Demo page](https://github.com/askmuhsin/fast_forward_life/blob/master/elems/demo_page.png)
