# TheArtOfPour-API

Backend API code for https://theartofpour.com

Python3 based API using eve-sqlalchemy and tensorflow

Thank you to everyone who attended my talk at this year's HomebrewCon.

I'll be working over the next few days on getting any remaining code/data deployed, as well as setting licenses and documentation.

Cheers!

Installing eve-sqlalchemy: **pip install eve-sqlalchemy**

Installing tensorflow: **pip install tensorflow**

Depending on your setup, you may also need the sqlalchemy drivers for your database.

Starting the API: **python app.py**
```
[CondaEnv] PS C:\TheArtOfPour\TheArtOfPour-API> python .\app.py
Using TensorFlow backend.
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```
 
Available endpoints

- GET /styles
- GET /yeast
- GET /hops
- GET /fermentables
- POST /test
    - REQUEST:
    ```
    {
	"yeast":"1",
	"fermentables":[
		{"id":"1","amount":"8"},
		{"id":"2","amount":"1"},
		{"id":"4","amount":"1"},
		{"id":"0","amount":"0"},
		{"id":"0","amount":"0"}
	],
	"hops":[
		{"id":"3","amount":"0.75","time":"60"},
		{"id":"3","amount":"0.5","time":"30"},
		{"id":"3","amount":"0.5","time":"5"},
		{"id":"3","amount":"0.5","time":"0"},
		{"id":"0","amount":"0","time":"0"},
		{"id":"0","amount":"0","time":"0"},
		{"id":"0","amount":"0","time":"0"},
		{"id":"0","amount":"0","time":"0"},
		{"id":"0","amount":"0","time":"0"}
	]
}
```
    - RESPONSE:
    ```
    [
    {
        "style": "stout",
        "confidence": 61.5
    },
    {
        "style": "blonde ale",
        "confidence": 0.9
    },
    {
        "style": "american pale ale",
        "confidence": 2.4
    },
    {
        "style": "porter",
        "confidence": 4.8
    },
    {
        "style": "wheat beer",
        "confidence": 0.2
    },
    {
        "style": "imperial ipa",
        "confidence": 4.1
    },
    {
        "style": "american ipa",
        "confidence": 4.1
    },
    {
        "style": "brown ale",
        "confidence": 4.1
    },
    {
        "style": "saison",
        "confidence": 0.1
    },
    {
        "style": "kölsch/cream ale",
        "confidence": 0.2
    },
    {
        "style": "pilsner/bock",
        "confidence": 0.1
    },
    {
        "style": "american amber ale",
        "confidence": 3
    },
    {
        "style": "bitter",
        "confidence": 1.1
    },
    {
        "style": "specialty beer",
        "confidence": 13.3
    }
]
```

In progress
* GET /stats : querydsl based, freeform filter endpoint

@todo
* Make ingredient dimensions dynamic (crop to model inputs or allow ui to request)