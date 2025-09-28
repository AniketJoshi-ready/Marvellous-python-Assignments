import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
"""kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)"""
def k_means_clustering(feature_x,k):
    kmeans=KMeans(n_clusters=k,random_state=42,n_init=10)
    clusters=kmeans.fit_predict(feature_x)
    return clusters,kmeans



def main():
    
   df=pd.read_csv("student-mat.csv",sep=";")

   print(df.shape)
   print(df.head())
   print(df.info())

   # selecting  feature 
   features=["G1","G2","G3","studytime","failures","absences"]
   x=df[features]
   #print(x)

   # scaling the features
   scale=StandardScaler()
   
   # passing feature for scaling  transformation 
   x_scaled=scale.fit_transform(x)
   
   #clustering algorithm kmeans:k=3
   k=3
   Clusters,kmeans=k_means_clustering(x_scaled,k)
   df["clusters"]=Clusters
   print(df.shape)
   print(df.head())

   # map the clusters to human words
   mapping={0:"Struggling",1:"Average",2:"Top Performer"}
   df["performance_group"]=df["clusters"].map(mapping)

   print("look overall clustering of data with performer groups:\n",df.head())
   
   



   sil_score = silhouette_score(x_scaled, Clusters)
   print("Silhouette Score:", sil_score)

   # Show cluster centers (scaled values)

   cluster_center=pd.DataFrame(kmeans.cluster_centers_,columns=features)
   print("cluster centers:\n",cluster_center)





    
if __name__=="__main__":
    main()    