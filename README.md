# nlp
A python project for the course of Language Technology/NLP. Using the data gathered by some custom made crawlers made with [scrapy](https://scrapy.org/) for various news portals, and the [nltk](https://www.nltk.org/) module, we create a vector space representation of out collection and an inverted index. Ultimately, the 2 basic functionalities are:  
* relevant article search, based on the tf-idf metric regarding the search query keywords
* categorization of a text by looking at the top features (frequency-wise) of it's content
