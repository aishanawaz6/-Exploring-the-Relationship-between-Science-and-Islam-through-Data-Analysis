#!/usr/bin/env python
# coding: utf-8

# #  Aisha Nawaz 

# ## Project Title: Exploring the Relationship between Science & Islam through Data Analysis
# 
# ## Project Overview:
# ### The purpose of this project is to investigate & uncover insights into the relationship between science & Islam by applying data analysis techniques. By analyzing relevant data sources, we aim to identify patterns, correlations, and intersections between scientific knowledge and Islamic teachings.

# ## Objectives:

# ## Step 1 Data Collection: 
# ### Gather data from reputable sources that encompass scientific discoveries & Islamic teachings, ensuring diversity & accuracy.
# 

# In[1]:


#NOTE: I manually extracted data from several websites
# Creating a dictionary to store the manually collected dataset
dataset={
    #A ID for every entry in the table
    "Entry Number":[1,2,3,4,5,None,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,21,22], 
    
    #Description of the entry if its an Islamic Teaching
    "Description Islamic Teaching" :[
                "Do the unbelievers not see that the heavens and the earth were joined together before we separated them, and that We brought all living things into existence from water? Why do they still not believe in God? (21:30)",
                "“We created the heavens with Our strength and power, and constantly expand them”. (51:47)",
                "It is Allah who raised the heavens without any pillars that you see, and then presided over the Throne. He disposed the sun and the moon, each moving for a specified term. He directs the command, [and] elaborates the signs that you may be certain of encountering your Lord.(13:2).",
                "“There is in truth for you a lesson in your animals and flocks. We give you to drink a pure milk derived from that which is contained in their bodies, from the merging of what is held in their intestines with blood. The drinking of that is then made easy for those who drink it.” (16:66).",
                "“Do they not look at the earth, where we created the plants in pairs”. (26:7).",
                "-",
                "-",
                "-",
                "Muslims believe that God is the creator of all things, and that God is all-powerful and all-knowing. God has no offspring, no race, no gender, no body, and is unaffected by the characteristics of human life.",
                "Muslims believe that on the Day of Judgment, humans will be judged for their actions in this life; those who followed God’s guidance will be rewarded with paradise; those who rejected God’s guidance will be punished with hell.",
                "And indeed, We created humankind from an extract of clay, then placed each human as a sperm-drop in a secure place, then We developed the drop into a clinging clot of blood, then developed the clot into a lump of flesh, then developed the lump into bones, then clothed the bones with flesh, then We brought it into being as a new creation. So Blessed is Allah, the Best of Creators. THE QURAN (23:12-14)", 
                "-",
                None,
                "And your Lord inspired the bees: “Make your homes in the mountains, the trees, and in what people construct, and feed from the flower of any fruit you please and follow the ways your Lord has made easy for you.” From their bellies comes forth liquid of varying colors, in which there is healing for people. Surely in this is a sign for those who reflect.",
                "-",
                "Whomever Allah desires to guide, He opens his breast to Islam, and whomever He desires to lead astray, He makes his breast narrow and straitened as if he were climbing to a height. Thus does Allah lay [spiritual] defilement on those who do not have faith",
                "And We send the fertilizing winds and send down water from the sky providing it for you to drink and you are not maintainers of its resources.",
                None,
                None,
                'Blessed is He who appointed houses in the sky and set in it a lamp and a shining moon.',
                'Quran states “he released the two seas, meeting [side by side], between them, is a barrier [so] neither of them transgresses.”',
                'Quran states, \' We shall send those who reject our revelations to the (hell) fire. When their skins have been burned away, we shall replace them with new ones so that they may continue to feel the pain.\' This passage clearly suggests that we feel pain because of our skin.',
                'Quran states “he released the two seas, meeting [side by side], between them, is a barrier [so] neither of them transgresses.”',
                'Quran states, \' We shall send those who reject our revelations to the (hell) fire. When their skins have been burned away, we shall replace them with new ones so that they may continue to feel the pain.\' This passage clearly suggests that we feel pain because of our skin.',
                    ],
    
    #Description of the entry if its an Scientific Discovery
    "Description Scientific Discovery" :[
                "All scientific circles in the world today agree that the planets were originally composed of a mass of Sodium gas and that first the heavens and the earth were joined together as a single entity and then they separated from each other.",
                "One of the most subtle discoveries in science concerns the expansion of universe, its tendency constantly to extend its boundaries. This was something completely unknown to the human being until the last century.",
                "We know that before the time of Newton, that great scientific personality, no one was aware of the force of gravity. Newton proved that the falling of objects to earth, the rotation of the moon and the Venus, the motion of the planets, and other instances of attraction are all subject to the single law, the law of universal gravity.",
                "The substances that ensure the general nutrition of the body come from chemical transformations which occur along the length of the digestive tract. These substances come from the contents of the intestine. On arrival in the intestine at the appropriate stage of chemical transformation, they pass through its wall and towards the systemic circulation (of blood). This very precise concept is the result of the discoveries made in the chemistry and physiology of the digestive system.",
                "It is only recently that researchers have come aware of insemination in plants and learned that every living being including plants comes into existence as the result of the merging of a male and female parts.",
                "No such Scientific Discovery",
                "Music Can Also Assist Surgeons To Perform Better During Surgery",
                "Music Can Decrease Anxiety Related To Maths Tests",
                "-",
                "-",
                "the process of conception wherein the sperm sits in the uterus, and how it then develops into an embryo and then into a shapeless lump, before developing bony structures and covering it with flesh. These stages were not well-considered and studied until around the 17th century shortly after the invention of the microscope, and further confirmed with ultrasound technology in the 1950s. ", 
                "description",
                None,
                "It was scientifically discovered later that the worker bees in the act of collecting nectar are females. Records don’t seem to have recognized worker bees as entirely female until some time around the 1800s. ",
                "The discovery of resveratrol in wine, a natural compound with antioxidant properties, has sparked scientific interest due to its potential health benefits, such as activating longevity-associated genes and promoting cardiovascular health. However, further research is ongoing to fully understand its effects.",
                "It is infact a highly common place reflection on the discomfort experienced at high altitude, which increases the higher one climbs",
                "There is an role and operation of an important factor in the bringing of things to fruition: the wind",
                None,
                None,
                'It is known that the sun is a star that generates intense heat and light by its internal combustion, and that the moon which does not give off light itself, merely reflects the light received from the sun.',
                'The meeting of two oceans is termed conflux. When two seas meet, their waters retain individual properties like temperature, color, and density. At a point of conflux, one can see two different water bodies running side by side. ',
                'For a long time, it was believed that the sense of feeling and pain is because of the brain. But, a scientific study recently found out that our skin features pain receptors due to which we feel pain and agony.',
                'The meeting of two oceans is termed conflux. When two seas meet, their waters retain individual properties like temperature, color, and density. At a point of conflux, one can see two different water bodies running side by side. ',
                'For a long time, it was believed that the sense of feeling and pain is because of the brain. But, a scientific study recently found out that our skin features pain receptors due to which we feel pain and agony.',
                    ],
    
    #Heading of the entry
    "Heading"         :[
                        "The Earth and Heavens were Joined Together",
                        "Expansion of Universe",
                        "Force of Gravity",
                        "Production of Milk in Animals",
                        "In Pairs",
                        "Towards Earth",
                        "Music & Surgery",
                        "Music & Anxiety",
                        "Belief in the Oneness of God",
                        "Belief in the Day of Judgment",
                        "Embryology",
                        'Humans Addiction',
                         None,
                        'Female Bees Ingesting Nectar To Produce Honey',
                        'Reservatrol in Red Wine',
                        'High Altitdue',
                        'Role of Wind',
                         None,
                        'Environment & its effects',
                        'Light in the Moon is merely a Reflection ',
                        'Oceanic Division mentions',
                        'Pain Receptors in Quran',
                        'Oceanic Division mentions',
                        'Pain Receptors in Quran',
                       ], 
    
    #Main Category of content
    "Category":[
             'Cosmology and Science',
             'Cosmology and Science',
             'Cosmology and Science',
             'Biology and Physiology',
             'Biology and Physiology',
             'Natural Phenomena and Science',
             'Music',
             'Music',
             'Religious Beliefs',
             'Religious Beliefs',
             'Biology and Physiology',
              None,
             'Religious Beliefs',
             'Biology and Physiology',
             'Natural Phenomena and Science',
             'Natural Phenomena and Science',
             'Natural Phenomena and Science',
             'Cosmology and Science',
             'Cosmology and Science',
             'Natural Phenomena and Science',
             'Natural Phenomena and Science',
             'Biology and Physiology',
             'Natural Phenomena and Science',
             'Biology and Physiology',               
    ],
    #Tells if it is a scientific discovery, Islamic Teaching or both
    "Type"       :[
                   "Scientific Discovery & Islamic Teaching",
                   "Scientific Discovery & Islamic Teaching",
                   "Scientific Discovery & Islamic Teaching",
                   "Scientific Discovery & Islamic Teaching",
                   "Scientific Discovery & Islamic Teaching",
                   "-",
                   "Scientific Discovery",
                   "Scientific Discovery",
                   "Islamic Teaching",
                   "Islamic Teaching",
                   "Scientific Discovery & Islamic Teaching",
                   "Islamic Teaching",
                   "Scientific Discovery",
                   "Scientific Discovery & Islamic Teaching",
                   "Scientific Discovery",
                   "Scientific Discovery & Islamic Teaching",
                   "Scientific Discovery & Islamic Teaching",
                   "Islamic Teaching",
                   "Islamic Teaching",
                   "Scientific Discovery & Islamic Teaching",
                   "Scientific Discovery & Islamic Teaching",
                   "Scientific Discovery & Islamic Teaching",
                   "Scientific Discovery & Islamic Teaching",
                   "Scientific Discovery & Islamic Teaching",
                     ], 
    
    #Tells the webiste from which the piece of information was taken
    "Source URL"      :[
                   "https://www.al-islam.org/authenticity-quran-shaykh-muslim-bhanji/some-brief-examples-scientific-data-quran",
                   "https://www.al-islam.org/authenticity-quran-shaykh-muslim-bhanji/some-brief-examples-scientific-data-quran",
                   "https://www.al-islam.org/authenticity-quran-shaykh-muslim-bhanji/some-brief-examples-scientific-data-quran",
                   "https://www.al-islam.org/authenticity-quran-shaykh-muslim-bhanji/some-brief-examples-scientific-data-quran",
                   "https://www.al-islam.org/authenticity-quran-shaykh-muslim-bhanji/some-brief-examples-scientific-data-quran",
                   "https://www.al-islam.org/authenticity-quran-shaykh-muslim-bhanji/some-brief-examples-scientific-data-quran",
                   "https://mixdownmag.com.au/news/music/incredible-scientific-discoveries-about-music-in-2015/",
                   "https://mixdownmag.com.au/news/music/incredible-scientific-discoveries-about-music-in-2015/",
                   "https://sites.udel.edu/msadelaware/six-major-beliefs-in-islam/",
                   "https://sites.udel.edu/msadelaware/six-major-beliefs-in-islam/",
                   "https://muslimgirl.com/13-scientific-discoveries-mentioned-in-the-quran/",
                   "https://muslimgirl.com/13-scientific-discoveries-mentioned-in-the-quran/",
                   "https://muslimgirl.com/13-scientific-discoveries-mentioned-in-the-quran/",
                   "https://muslimgirl.com/13-scientific-discoveries-mentioned-in-the-quran/",
                   "https://ods.od.nih.gov/",
                   "https://www.al-islam.org/authenticity-quran-shaykh-muslim-bhanji/some-brief-examples-scientific-data-quran",
                   "https://www.al-islam.org/authenticity-quran-shaykh-muslim-bhanji/some-brief-examples-scientific-data-quran",
                   "https://www.al-islam.org/quran/surah/15/al-hijr/ayat/22",
                    None,
                   "https://www.al-islam.org/authenticity-quran-shaykh-muslim-bhanji/some-brief-examples-scientific-data-quran",
                   "https://zamzam.com/blog/scientific-facts-in-quran/",
                   "https://zamzam.com/blog/scientific-facts-in-quran/",
                   "https://zamzam.com/blog/scientific-facts-in-quran/",
                   "https://zamzam.com/blog/scientific-facts-in-quran/",
                       ], 
}


# In[2]:


# Converting the manually made dataset into a dataframe
import pandas as pd
DF=pd.DataFrame(dataset)
DF.sample(5) #preview of dataset created


# In[4]:


# Saving the dataset as csv file for later use
DF.to_csv('DATASET.csv',index=False)


# ## Step 2 Data Preprocessing: 
# ### Clean, organize, & harmonize the collected data to ensure consistency & suitability for analysis.
# 

# In[5]:


DATA=pd.read_csv('DATASET.csv')
# Cleaning the data
DATA.isnull().sum() #Counting null values


# In[6]:


DATA.dropna(inplace=True) # Dropping null values
DATA.isnull().sum()       #Verifying removal of null values


# In[7]:


duplicates=DATA.duplicated() #Checking for duplicates
DATA[duplicates]


# In[8]:


DATA.drop_duplicates(inplace=True)  # Removing Duplicates
duplicates2=DATA.duplicated()       # Checking for duplicates again to confirm removal
DATA[duplicates2]                   # Should print nothing


# In[10]:


# Organzing & Harmonzing the data to ease analysis
def getNameOnly(data):
    tokens=data.split('/')
    return tokens[2]

DATA['Source Name']=DATA['Source URL'].apply(getNameOnly) #Basically stores the source name in a more clear way
DATA.head()


# In[12]:


# Removing Stop Words & Punctaions in descriptions & Heading columns to ensure correct and helpful analysis of data
from collections import Counter
import nltk
from nltk.corpus import stopwords

stopWords = set(stopwords.words('english'))

def cleanDATA(data):
        # Converting to string type each description in dataset
        descriptionSTR = str(data)
        
        # Tokenizing
        tokens = nltk.word_tokenize(descriptionSTR.lower())
        
        # Removing punctuations and stop words
        tokensC = [words for words in tokens if words.isalnum() and words not in stopWords]
        
        return ' '.join(tokensC) #Returning tokens as joined sentences

DATA['Description Islamic Teaching Cleaned']=DATA['Description Islamic Teaching'].apply(cleanDATA)
DATA['Description Scientific Discovery Cleaned']=DATA['Description Scientific Discovery'].apply(cleanDATA)
DATA['Heading Cleaned']=DATA['Heading'].apply(cleanDATA)
DATA.head()


# In[13]:


DATA.to_csv('DATASET_CLEANED.csv',index=False)       # Saving cleaned data  as csv file for later use


# In[14]:


data=pd.read_csv("DATASET_CLEANED.csv")  # Reading cleaned saved data for further use
data.head(2)


# In[15]:


# PREPROCESSING DATASET
# Performing one-hot encoding on the categorical coloumns named 'Category' , 'Type' & 'Source Name'
data=pd.read_csv("DATASET_CLEANED.csv")
data=pd.get_dummies(data,columns=['Category','Type','Source Name'])
data.head(2)


# In[16]:


data.to_csv('DATASET_PREPROCESSED.csv',index=False) # Saving preprocessed data for later use


# In[18]:


# Reading saved cleaned & preprocessed datas for further steps
import pandas as pd
dataC=pd.read_csv('DATASET_CLEANED.csv')    
dataP=pd.read_csv('DATASET_PREPROCESSED.csv')


# ## Data Sources: 
# ### Specify the sources of data to be used, including scientific literature, Islamic texts, historical records, and other relevant sources.

# In[19]:


groupedSources=dataC.groupby('Source URL')['Entry Number'].count() #Grouping data by source url & counting each occurrence
print("-----------> SOURCES TO BE USED ARE AS FOLLOWS:")
print(groupedSources)


# ->Most of the data is collected from the source url "https://www.al-islam.org/authenticity-quran-shaykh-muslim-bhanji/some-brief-examples-scientific-data-quran"

# ## Data Diversity: 
# ### Ensure a diverse dataset that covers various scientific disciplines and aspects of Islamic teachings.
# 
# ## Ethical Considerations:
# ### Emphasize the importance of treating the data with respect for both scientific and Islamic ethics.

# In[20]:


import matplotlib.pyplot as plt
# Checking the diversity of the sources of data
SOURCES=dataC.groupby('Source Name')['Entry Number'].count()
plt.title("Distribution of Sources of Data")
plt.pie(SOURCES.values,labels=SOURCES.index,autopct='%1.1f%%',colors=['pink','violet','plum','indigo','purple','magenta'])
plt.axis('equal')
plt.show()


# Majority of the data (around 47.1%) is colleced from the source named "www.al-islam.org"

# In[21]:


# Checking the diversity of the categories of data 
category=dataC.groupby('Category')['Entry Number'].count()
plt.title("Distribution of Category of Data")
plt.pie(category.values,labels=category.index,autopct='%1.1f%%',colors=['red', 'green', 'blue', 'yellow', 'purple', 'orange'])
plt.axis('equal')
plt.show()


# Majoirty of the content in the dataset collected falls under the category "Biology & Physiology" and "Natural Phenomena and Science" (around 29.4% ) 

# In[22]:


# Checking the distibution of type of data
TYPES=dataC.groupby('Type')['Entry Number'].count()

plt.bar(x=TYPES.index,height=TYPES.values,color=['pink','salmon','Coral'])
plt.title('Distribution of Type of Data')
plt.ylabel('Count of Types')
plt.xlabel('Type')
plt.xticks(rotation=45)
plt.show()


# Majority of the entries are both "Scientific Discovery & Islamic Teaching"

# ## Step 3 Exploratory Data Analysis (EDA): 
# ### Perform exploratory analysis to identify initial trends, patterns, & potential relationships between scientific concepts and Islamic principles.
# ## Ethical and Cultural Sensitivity:
# ### Ensure that all analyses respect Islamic ethical guidelines and cultural sensitivities

# In[23]:


from wordcloud import WordCloud
from collections import Counter

# Word Cloud For Scientific Discovery Headings

#First combining all the words in all the headings with type 'Scientific Discovery' 
scHEADINGS=''.join(map(str,dataC.loc[dataC['Type']=='Scientific Discovery','Heading Cleaned']))

# Generating Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(scHEADINGS)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud from Headings of Scientific Discoveries')
plt.show()


# "Music" is the most frequent word used in headings of entries which are Scientific Discovery only.

# In[24]:


# Word Cloud For Islamic Teachings Headings

#First combining all the words in all the headings with type 'Islamic Teachings' 
isHEADINGS=''.join(map(str,dataC.loc[dataC['Type']=='Islamic Teaching','Heading Cleaned']))

# Generating Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(isHEADINGS)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud from Headings of Islamic Teachings')
plt.show()


# "Belief" is the most common word used in headings of entries which are Islamic Teachings only.

# In[25]:


# Word Cloud For Both Scientific Discoveries & Islamic Teachings Headings

#First combining all the words in all the headings with type 'Scientific Discovery & Islamic Teaching' 
bothHEADINGS=''.join(map(str,dataC.loc[dataC['Type']=='Scientific Discovery & Islamic Teaching','Heading Cleaned']))

# Generating Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(bothHEADINGS)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud from Headings of Scientific Discoveries & Islamic Teachings')
plt.show()


# Majoirty of the words used in headings of both Scientific Discoveries & Islamic Teachings seem to fall under the catgeory "Natural Phenomena & Science"

# In[28]:


# Finding top 5 common words in description of Scientific Discoveries

from collections import Counter
import nltk
from nltk.corpus import stopwords

scDescriptions=''.join(map(str,dataC.loc[dataC['Type']=='Scientific Discovery','Description Scientific Discovery Cleaned']))

#Tokenzing 
tokensSC = nltk.word_tokenize(scDescriptions.lower())
wordCountsSC = Counter(tokensSC) #Counting words
commonWordsSC = wordCountsSC.most_common(8)  # Getting top 8 common words

wordsSC, countsSC = zip(*commonWordsSC)
plt.figure(figsize=(10, 5))
plt.bar(wordsSC, countsSC,edgecolor='black',color=['salmon'])
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 8 Common Words in Scientific Discovery Descriptions')
plt.show()


# "Health" is the most common word used in descriptions of Scientific Discoveries only.

# In[29]:


# Finding top 5 common words in description of Islamic Teachings
isDescriptions=''.join(map(str,dataC.loc[dataC['Type']=='Islamic Teaching','Description Islamic Teaching Cleaned']))

#Tokenzing 
tokensis = nltk.word_tokenize(isDescriptions.lower())

wordCountsis = Counter(tokensis) #Counting words
commonWordsis = wordCountsis.most_common(8)  # Getting top 8 common words

wordsis, countsis = zip(*commonWordsis)
plt.figure(figsize=(10, 5))
plt.bar(wordsis, countsis,edgecolor='black',color='pink')
plt.xlabel('Words')
plt.ylabel('Frequency of Occurrence')
plt.title('Top 8 Common Words in Islamic Teaching Descriptions')
plt.show()


# "God" is the most common word used in descriptions of Islamic Teachings only.

# In[31]:


# Finding top 5 common words in description of both Scientific Discovery & Islamic Teachings 
BOTHDescriptions=''.join(map(str,dataC.loc[dataC['Type']=='Scientific Discovery & Islamic Teaching','Description Islamic Teaching Cleaned'])) +''.join(map(str,dataC.loc[dataC['Type']=='Scientific Discovery & Islamic Teaching','Description Scientific Discovery Cleaned']))

#Tokenzing 
tokensBOTH = nltk.word_tokenize(BOTHDescriptions.lower())

wordCountsBOTH = Counter(tokensBOTH)             #Counting words
commonWordsBOTH = wordCountsBOTH.most_common(8)  # Getting top 8 common words

wordsBOTH, countsBOTH = zip(*commonWordsBOTH)
plt.figure(figsize=(10, 5))
plt.bar(wordsBOTH, countsBOTH,edgecolor='black',color='Coral')
plt.xlabel('Words')
plt.ylabel('Frequency of Occurrence')
plt.title('Top 8 Common Words in Scientific Discovery & Islamic Teaching Descriptions')
plt.show()


# "Pain" is the most common word used in descriptions of both Scientifc Discoveries & Islamic Teachings

# ## Step 4 Correlation Analysis: 
# ### Conduct statistical analyses to determine correlations between scientific advancements & concepts in Islam.
# 

# In[33]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Calculating the similarity between Scientific Discovery & Islamic Teachings
dataC2=dataC.loc[dataC['Type']=='Scientific Discovery & Islamic Teaching'].copy()
# Converting to lowercase
dataC2['Description Scientific Discovery Cleaned'] = dataC2['Description Scientific Discovery Cleaned'].str.lower()
dataC2['Description Islamic Teaching Cleaned'] = dataC2['Description Islamic Teaching Cleaned'].str.lower()

# Creating TF-IDF vectors
tfidfVectorizer = TfidfVectorizer()
tfidfMatrix = tfidfVectorizer.fit_transform(dataC2['Description Scientific Discovery Cleaned'] + ' ' + dataC2['Description Islamic Teaching Cleaned'])

# Calculating cosine similarity
cosineSimilarity = cosine_similarity(tfidfMatrix)
print(cosineSimilarity[0:2]) #For preview 


# In[35]:


import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
# Sentiment analysis of both type of descriptions
#Converting description column to string type
dataC['Description Scientific Discovery Cleaned'] = dataC['Description Scientific Discovery Cleaned'].astype(str)
dataC['Description Islamic Teaching Cleaned'] = dataC['Description Islamic Teaching Cleaned'].astype(str)

# Sentiment analysis 
sia = SentimentIntensityAnalyzer()
dataC['Sentiment Score Scientific Discovery'] = dataC['Description Scientific Discovery Cleaned'].apply(lambda x: sia.polarity_scores(x)['compound'])
dataC['Sentiment Score Islamic Teaching'] = dataC['Description Islamic Teaching Cleaned'].apply(lambda x: sia.polarity_scores(x)['compound'])
dataC.head(2)


# ## Step 5 Visualization:
# ### Develop visual representations that illustrate the identified relationships & intersections, aiding in clear communication of findings.

# In[37]:


import seaborn as sns
cosineSimilarityDF = pd.DataFrame(cosineSimilarity, columns=dataC2.index, index=dataC2.index)

# Creating a heatmap to visualize results on similarity
plt.figure(figsize=(10, 8))
sns.heatmap(cosineSimilarityDF, cmap='cividis', annot=True, fmt=".2f", linewidths=0.5)
plt.title('Cosine Similarity Heatmap')
plt.xlabel('Index')
plt.ylabel('Index')
plt.show()


# The closest match is visible between the following enteries:
# Index Number : 0 & 2 and 14&2 

# In[38]:


# Sentiment score distribution [Scientific Discovery]
plt.figure(figsize=(8, 6))
sns.histplot(data=dataC, x='Sentiment Score Scientific Discovery', bins=20,hue='Category',palette='rocket')
plt.title('Distribution of Sentiment Scores in Descriptions of Scientific Discoveries')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()


# The Histogram is skewed to the right which indicates that many descriptions have high sentiment scores, indicating positive sentiments in Descriptions of Scientific Discoveries.

# In[39]:


# Sentiment score distribution [Islamic Teaching]
plt.figure(figsize=(8, 6))
sns.histplot(data=dataC, x='Sentiment Score Islamic Teaching', bins=20,hue='Category',palette='cividis')
plt.title('Distribution of Sentiment Scores in Descriptions of Islamic Teachings')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()


# The Histogram is even more skewed to the right which indicates that many descriptions have high sentiment scores, indicating positive sentiments in Descriptions of Islamic Teachings. Evem more than is Scientific Discoveries.

# ## Step 6 Interpretation: 
# ### Provide meaningful interpretations of results, highlighting the alignment or disparities between science & Islamic teachings.

# In[40]:


print("Top 5 matching Scientific Discoveries & Islamic Teachings descriptions are as follows:")
for i in range (5):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ NUMBER ",i+1)
    print("\n<--Islamic Teaching-->\n",dataC2['Description Islamic Teaching'][i])
    print("\n<--Scientfic Discovery-->\n",dataC2['Description Scientific Discovery'][i])


# ## Interpretations of Results:
# #### -> Majority of the data (around 47.1%) is colleced from the source named "www.al-islam.org"
# 
# #### -> Majoirty of the content in the dataset collected falls under the category "Biology & Physiology" and "Natural Phenomena and Science" (around 29.4% ) 
# 
# #### -> Majority of the entries are both "Scientific Discovery & Islamic Teaching"
# #### -> "Music" is the most frequent word used in headings of entries which are Scientific Discovery only.
# 
# #### -> "Belief" is the most common word used in headings of entries which are Islamic Teachings only.
# #### -> Majoirty of the words used in headings of both Scientific Discoveries & Islamic Teachings seem to fall under the catgeory "Natural Phenomena & Science"
# 
# #### ->"Health" is the most common word used in descriptions of Scientific Discoveries only.
# #### -> "God" is the most common word used in descriptions of Islamic Teachings only.
# 
# #### -> "Pain" is the most common word used in descriptions of both Scientifc Discoveries & Islamic Teachings
# #### -> The closest match is visible between the following enteries: Index Number : 0 & 2 and 14&2 
# #### -> The Histogram is skewed to the right for both type of descriptions which indicates that many descriptions have high sentiment scores, indicating positive sentiments however the histogram is more skewed to the right for islamic teachings than for Scientific Discoveries Descriptions.

# ## Step 7 Documentation: 
# ### Create comprehensive documentation detailing data sources, preprocessing steps, analysis methods, findings, & interpretations.
