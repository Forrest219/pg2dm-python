# -*-coding=utf-8-*-
import codecs 
from math import sqrt

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0,
                      "Norah Jones": 4.5, "Phoenix": 5.0,
                      "Slightly Stoopid": 1.5,
                      "The Strokes": 2.5, "Vampire Weekend": 2.0},
         
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5,
                 "Deadmau5": 4.0, "Phoenix": 2.0,
                 "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0,
                  "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5,
                  "Slightly Stoopid": 1.0},
         
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0,
                 "Deadmau5": 4.5, "Phoenix": 3.0,
                 "Slightly Stoopid": 4.5, "The Strokes": 4.0,
                 "Vampire Weekend": 2.0},
         
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0,
                    "Norah Jones": 4.0, "The Strokes": 4.0,
                    "Vampire Weekend": 1.0},
         
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0,
                     "Norah Jones": 5.0, "Phoenix": 5.0,
                     "Slightly Stoopid": 4.5, "The Strokes": 4.0,
                     "Vampire Weekend": 4.0},
         
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0,
                 "Norah Jones": 3.0, "Phoenix": 5.0,
                 "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0,
                      "Phoenix": 4.0, "Slightly Stoopid": 2.5,
                      "The Strokes": 3.0}
        }

class recommender:

  def __init__(self, data, k=1, metric='pearson', n=5):
    """ initialize recommender
    currently, if data is dictionarey the recommender is initialized to it.
    For all other data types of data, no initialization occurs
    k is the k value for k nearest neighbor
    metric is which distance formyla to use
    n is the maxinum number of recommendations to make"""

    self.k = k
    self.n = n
    self.usersname2id = {}  #username->id的映射关系
    self.userid2name = {} #userid->name的映射关系
    self.productid2name = {}
    self.metric = metric
    if self.metric == 'pearson':
      self.fn = self.pearson

    #if data is dictionary set recommender data to it
    if type(data) == 'dict':
      self.data = data

    def coverProductID2name(self, id):
      """given product id number return product name"""
      if id in self.productid2name:
        return self.productid2name[id]
      else:
        return id

      def useridratings(self, id, n):
        """return n top ratings for users with id"""
        




