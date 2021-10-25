import Models.Provider as Provider
from flask_sqlalchemy import SQLAlchemy



#Insert Keywords
def Insert_Keywords(category,content,score):
    query = "INSERT INTO Keywords ('category','content',score) VALUES ('{}','{}',{}) ".format(category,content,score)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Update_Keywords(category,content,score,idKeyword):
    query = "UPDATE Keywords SET category ='{}', content='{}', score={} WHERE idKeyword={}".format(category,content,score,idKeyword)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Delete_Keywords(idKeyword):
    query = "DELETE FROM Keywords WHERE idKeyword={}".format(idKeyword)
    msg = Provider.ExecuteNonQuery(query)
    return msg


#Test
# Insert_Keywords('Positive','Good',1)
# Update_Keywords('Nev','Goo',-1,1)
# Delete_Keywords(1)


#
# def SentimentAnalysisProcess(self,tweet,positivelist,negativelist):
#     ps = PorterStemmer()
#     # PorterStemmer using for look up words have 1 root word
#     # For example : Root Word : Like include Likes Liking Liked Likely
#
#     tweet = word_tokenize(tweet)
#     tweet_list = []
#     score = 0
#
#     for word in tweet:
#         word = ps.stem(word)
#         if word in positivelist:
#             score += score
#
#         elif word in negativelist:
#             score -= score
#
#         else:
#             pass
#     return score
#
# def checkRank(self,score,rank):
#     query = "SELECT ranked FROM Comments"
#     rank = Provider.ExecuteQuery(query)
#     if (score > 0):
#         rank = "Good"
#     elif (score == 0):
#         rank = "Neutral"
#     else:
#         rank = "Bad"
#     return rank
#
#
#
#
#
#




