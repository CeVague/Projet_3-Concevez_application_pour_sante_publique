import pandas as pd
import numpy as np
import re
from wordcloud import WordCloud
import seaborn as sns
import matplotlib.pyplot as plt

class DataSet:
    def __init__(self, data, categorie):
        self.data = data
        self.categorie = categorie
        
    def make_dataset(data, categorie):
        if categorie == 'cat':
            return DataSetCat(data)
        elif categorie == 'txt':
            return DataSetTxt(data)
  
    def histogram(self):
        print("Pas définit pour cette classe")

    def camembert(self):
        print("Pas définit pour cette classe")


class DataSetCat(DataSet):
    def __init__(self, data):
        self.data = pd.Series(data)
        self.categorie = 'cat'
  
    def histogram(self, limit=None):
        tmp = self.data.value_counts()
    
        if limit is not None:
            tmp = tmp[:limit]
        
        return sns.displot(tmp, shrink=.8)

    def camembert(self, limit=None, palette='bright'):
        tmp = self.data.value_counts()
    
        if limit is not None:
            tmp = tmp[:limit]

        palette_color = sns.color_palette(palette)

        return plt.pie(tmp.values, labels=tmp.index, colors=palette_color, autopct='%.0f%%')


class DataSetTxt(DataSet):    
    def __init__(self, data):
        self.data = data
        self.categorie = 'txt'
        self.norm = None
  
    def normalise(self):
        if self.norm is None:
            # convert to lower case
            norm = self.data.lower()
            # remove numbers
            norm = re.sub(r'\d+','',norm)
            # remove all punctuation except words and space
            norm = re.sub(r'[^\w\s]','', norm)
            norm = re.sub(r'\s',' ', norm)
            # remove white spaces
            norm = norm.strip()
            norm = re.sub(r'\ +',' ',norm)
            #Stopword
            norm = re.sub(r' (g|mg|à|la|le|les|au|the|a|et|and|l|kg|de|des|aux) ','',norm)
            norm = re.sub(r' (of|in|trace|traces|contain|contains|less|more|en) ','',norm)
            self.norm = norm
        return self
    
    def wordcloud(self, *arg, **args):
        return WordCloud(*arg, **args).generate(self.norm if self.norm is not None else self.data)

    def camembert():
        print("Pas définit pour cette classe")
    