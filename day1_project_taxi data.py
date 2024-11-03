#!/usr/bin/env python
# coding: utf-8

# In[959]:


# 라이브러리 import
import pandas as pd
import numpy as np
import seaborn as sns


# In[960]:


# 데이터 불러오기
trip_df = pd.read_csv('/aiffel/data/trip.csv')


# In[961]:


# 첫 5행 확인하여 데이터 구조 보기
trip_df.head()


# In[962]:


trip_df


# In[963]:


# 데이터 정보 확인
trip_df.info()


# In[964]:


trip_df.describe()


# In[965]:


# 결측치 판단 및 처리
# 결측치의 유무와 비율을 살펴보고 적절한 방법으로 처리하기


# In[966]:


# 결측치 합계 확인하기
trip_df.isna().sum()


# In[967]:


# 결측치 비율 확인하기
trip_df.isna().mean()


# In[968]:


# fare_amount 칼럼 확인하기
trip_df['fare_amount']


# In[969]:


# fare_amount 칼럼 오름차순 정렬하기
trip_df['fare_amount'].sort_values()


# In[970]:


# 결측치 확인하기
trip_df['fare_amount'].isna()


# In[971]:


# 전체 칼럼에 대한 결측치 True 행 확인하기
trip_df[trip_df['fare_amount'].isna()]


# In[972]:


# 전체 비중에서 매우 작은 비중으로 결측값 있는 행 삭제하기
trip_df.dropna(subset = ['fare_amount'])


# In[973]:


# 덮어쓰기
trip_df = trip_df.dropna(subset = ['fare_amount'])


# In[974]:


# 결측치 행 호출해보기
trip_df[trip_df['fare_amount'].isna()].index


# In[975]:


# fare_amount 평균 확인하기
trip_df['fare_amount'].mean()


# In[976]:


fare_na_index


# In[977]:


trip_df.info()


# In[978]:


#전체 데이터 프레임 다시 확인
trip_df


# In[979]:


# passenger_count scatterplot으로 산점도 시각화하기
sns.scatterplot(x = trip_df.index, y = trip_df['passenger_count'])


# In[980]:


# passenger_count 내림차순 정렬하기
trip_df['passenger_count'].sort_values(ascending = False)


# In[981]:


# passenger_count=0 확인하기
trip_df[trip_df['passenger_count']==0]


# In[982]:


# passenger_count가 0인 경우의 전체 대비 비중
(trip_df['passenger_count'] == 0).mean()


# In[983]:


# passengar_count가 0인 경우와 아닌 경우를 따로 데이터셋 구분해두기
trip_df_zero = trip_df[trip_df['passenger_count'] == 0]
trip_df_non_zero = trip_df[trip_df['passenger_count'] > 0]


# In[984]:


# passenger_count가 0인 경우를 1로 대체
trip_df['passenger_count'] = trip_df['passenger_count'].apply(lambda x: 1 if x == 0 else x)


# In[985]:


# passenger_count=0 확인하기
trip_df[trip_df['passenger_count']==0]


# In[986]:


# 이상치 판단 및 처리
# 숫자형 변수 각각에 대해, 데이터의 index와 변수 값 사이의 scatter plot을 그려보고 이상치가 관찰될 경우 제거


# In[987]:


trip_df


# In[988]:


# trip_distance scatterplot으로 산점도 시각화하기
sns.scatterplot(x = trip_df.index, y = trip_df['trip_distance'])


# In[989]:


# tip_amount scatterplot으로 산점도 시각화하기
sns.scatterplot(x = trip_df.index, y = trip_df['tip_amount'])


# In[990]:


# tip_amount 오름차순 정렬하기
trip_df['tip_amount'].sort_values()


# In[991]:


# tip_amount 꼬리 20개 출력해보기
trip_df['tip_amount'].sort_values().tail(20)


# In[992]:


# 8478행 전체 출력하기
trip_df.loc[8478]


# In[993]:


# 8478행 이상치로 판단, 삭제하기
trip_df.drop(8478, inplace=True)


# In[994]:


# tip_amount 이상치 행 삭제 확인
trip_df['tip_amount'].sort_values()


# In[995]:


# fare_amount scatterplot으로 산점도 시각화하기
sns.scatterplot(x = trip_df.index, y = trip_df['fare_amount'])


# In[996]:


# fare_amount 살펴보기
trip_df['fare_amount'].sort_values()


# In[997]:


# fare_amount 0보다 작거나 같은 경우
trip_df[trip_df['fare_amount'] <= 0]


# In[998]:


# fare_amount가 0보다 큰 경우를 남기고 필터링
trip_df = trip_df[trip_df['fare_amount'] >0]


# In[999]:


# fare_amount 칼럼 오름차순 확인하기
trip_df['fare_amount'].sort_values()


# In[1000]:


# 20314 행이 이상치인지, 문제가 있는 데이터인지 확인하기 위해 체크 -- 탔다가 바로 내린 경우로 보임 -- 삭제결정
trip_df.loc[20314]


# In[1001]:


# 20314행 삭제하기
trip_df.drop(20314, inplace=True)


# In[1002]:


print(trip_df.index)


# In[1003]:


# fare_amount 칼럼 오름차순 확인하기 -- 450 값 삭제 확인완료
trip_df['fare_amount'].sort_values()


# In[1004]:


# tolls_amount scatterplot
sns.scatterplot(x = trip_df.index, y = trip_df['tolls_amount'])


# In[1005]:


trip_df['tolls_amount'].describe()


# In[1006]:


trip_df['tolls_amount'].sort_values().tail(20)


# In[1007]:


#이동 시간 분석하기


# In[1008]:


trip_df = trip_df.copy()


# In[1009]:


trip_df


# In[1010]:


# tpep_pickup_datetime 및 tpep_dropoff_datetime을 datetime 형식으로 변환
trip_df['tpep_pickup_datetime'] = pd.to_datetime(trip_df['tpep_pickup_datetime'], format='%m/%d/%Y %I:%M:%S %p')
trip_df['tpep_dropoff_datetime'] = pd.to_datetime(trip_df['tpep_dropoff_datetime'], format='%m/%d/%Y %I:%M:%S %p')


# In[1011]:


# 변환된 tpep_pickup_datetime 열 확인
print(trip_df['tpep_pickup_datetime'].head())


# In[1012]:


# 이동 시간 계산 (분 단위)
trip_df['trip_duration'] = (trip_df['tpep_dropoff_datetime'] - trip_df['tpep_pickup_datetime']).dt.total_seconds() / 60


# In[1013]:


# 이동 시간 통계 확인
print(trip_df['trip_duration'].describe())


# In[1014]:


trip_df['trip_duration'].sort_values()


# In[1015]:


# trip_duration 칼럼의 scatterplot 확인하기
sns.scatterplot(x = trip_df.index, y = trip_df['trip_duration'])


# In[1016]:


1439/60


# In[1017]:


600/60


# In[1018]:


# 음수이거나 600분이 넘는 trip_duration 행 필터링 및 출력
trip_df[(trip_df['trip_duration'] < 0) | (trip_df['trip_duration'] > 600)]


# In[1019]:


outliers_duration = trip_df[(trip_df['trip_duration'] < 0) | (trip_df['trip_duration'] > 600)]


# In[1020]:


#outliers 갯수, 전체 행 갯수 체크
outliers_count = outliers.shape[0]
total_count = trip_df.shape[0]


# In[1021]:


#outliers 비중 계산하기
outliers_ratio = outliers_count/total_count
outliers_ratio


# In[1022]:


# 이상치 제거
trip_df = trip_df[(trip_df['trip_duration'] >= 0) & (trip_df['trip_duration'] <= 600)]


# In[1023]:


print(trip_df['trip_duration'].describe())


# In[1024]:


332/60


# In[1025]:


trip_df['trip_duration'].sort_values()


# In[1026]:


trip_df.loc[5053]


# In[1027]:


trip_df


# In[1028]:


#택시의 주행 시간과 주행 거리, 요금 등의 상관 관계
trip_df[['trip_duration', 'trip_distance', 'fare_amount']].corr()


# In[1029]:


trip_df = trip_df.copy()


# In[1030]:


#Credit Card와 Debit Card를 구분없이 "Card"라는 이름으로 만들기
trip_df['payment_method'] = trip_df['payment_method'].replace({'Credit Card': 'Card', 'Debit Card': 'Card'})


# In[1031]:


trip_df['payment_method']


# In[1032]:


trip_df


# In[1033]:


## --- End of the Project -- ##

