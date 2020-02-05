from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from konlpy.tag import Okt
from konlpy.tag import Mecab
import pandas as pd
import tensorflow as tf
import os
import getpass
import numpy as np
from numpy import dot
from numpy.linalg import norm
import mat

#dataframe에 null값이 있는 경우 공백을 넣어 null값 제거
def avoid_null(data, header):
    data[header] = data[header].fillna('')
    return data[header]

#tfidf값을 이용해 코사인유사도를 계산하기 위한 함수
def cos_sim(A, B):
    return dot(A, B)/(norm(A)*norm(B))
    
#입력받은 dataframe의 title과 content열의 값을 가져와 tfidf를 계산해주는 함수
#입력되는 dataframe의 header에 반드시 title, content가 포함되어야 함!
def tfidf(dataframe, TfidfVectorizer):
    #title데이터의 내용을 null 없이 가져옴
    dataframe['title'] = avoid_null(dataframe, 'title')

    #tf-idf계산 후 출력
    tfidf_metrix_of_tit = TfidfVectorizer.fit_transform(dataframe['title'])
    return tfidf_metrix_of_tit

#입력되는 train의 질문과 질문 데이터셋의 코사인유사도 값 중 상위 50개 질문목록을 가져오는 함수
def top10_indices(data, q_num):
    #입력된 데이터의 코사인유사도 계산
    cos_sim = linear_kernel(data, data)

    cos_sim_score = list(enumerate(cos_sim[q_num])) 
    cos_sim_score = sorted(cos_sim_score, key = lambda x : x[1], reverse = True)
    #상위 100개 항목을 가져옴
    score = cos_sim_score[1:11]
    tag_indices = [i[0] for i in score]

    return tag_indices

with tf.device('/gpu:1'):
    okky_data = pd.read_csv(r'게시물 데이터.csv', encoding = "utf-8", low_memory = False)
    
    tfidf_gen = TfidfVectorizer() #일반적인 방식

    #ti-idf를 계산하여 title과 content 열의 값을 각각 받아옴
    data_tit = tfidf(okky_data, tfidf_gen) 

    for i in range(len(okky_data)):
        print(i, '/', len(okky_data))
        #질문 제목과 데이터셋의 유사도를 10위까지 가져옴
        tit_10_q = okky_data['title'].iloc[top100_indices(data_tit, i)]
        print(str(i),"번 질문과 유사한 제목을 가진 질문목록\n", tit_10_q) 
        