from django.shortcuts import render
from django.http import HttpResponse
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
  
def function():
    df = pd.read_excel(r"D:/News-detection-master/News-detection-master/news_detector/database.xlsx") 
    comment_words = '' 
    stopwords = set(STOPWORDS) 
    for val in df.Search_Heading: 
          
        # typecaste each val to string 
        val = str(val) 
      
        # split the value 
        tokens = val.split() 
          
        # Converts each token into lowercase 
        for i in range(len(tokens)): 
            tokens[i] = tokens[i].lower() 
          
        comment_words += " ".join(tokens)+" "
      
    wordcloud = WordCloud(width = 800, height = 800, 
                    background_color ='white', 
                    stopwords = stopwords, 
                    min_font_size = 10).generate(comment_words) 
      
    # plot the WordCloud image                        
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    plt.savefig('D:/News-detection-master/News-detection-master/static/plot.jpeg')
    
    #plt.show()