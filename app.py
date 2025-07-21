import streamlit as st
import pickle
import requests
st.title("Movie Recommender")
movies=pickle.load(open('movies.pkl','rb'))
movie_list=movies['title'].values
similarity=pickle.load(open('similarity.pkl','rb'))

def fetchPoster(movie_id):
    api_key="79e5885b115845749716ec6b2c7e9e0b"
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id,api_key))
    data=response.json()
    return 'http://image.tmdb.org/t/p/w500/'+ data['poster_path']

def recommend(movie):
    movie_index=int(movies[movies['title']==movie].index.values[0])
    distance=list(enumerate(similarity[movie_index]))
    sorted_list=sorted(distance,reverse=True,key=lambda x:x[1])[1:6]# 0 indexed movie is the 
    #same whose related movies we want
    cleaned=[(i,float(score)) for i,score in sorted_list]
    movie_list_names=[]
    posters=[]
    for i in cleaned:
        movie_id=movies.iloc[i[0]]['id']

        
        posters.append(fetchPoster(movie_id))
        
        movie_list_names.append(movies.iloc[i[0]]['title'])
    return movie_list_names,posters


choice=st.selectbox('Select the movie',movie_list)

if st.button('Recommend'):
    

    movies,posters=recommend(choice)

    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
      st.write(movies[0])
      st.image(posters[0])
    with col1:
      st.write(movies[1])
      st.image(posters[1])
    with col1:
      st.write(movies[2])
      st.image(posters[2])
    with col1:
      st.write(movies[3])
      st.image(posters[3])
    with col1:
      st.write(movies[4])
      st.image(posters[4])



