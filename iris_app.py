import pickle
import streamlit as st
from sklearn.tree import DecisionTreeClassifier
with open('iris_classifier.pickle','rb') as f:
    clf = pickle.load(f)

def main():
    st.title('Chào mừng bạn đến với các dự đoán của IRIS')

    st.title('Vui lòng nhập số đo hoa của bạn dưới đây:')
    SL = st.number_input('Chiều dài Sepal')
    SW = st.number_input('Chiều rộng Sepal')
    PL = st.number_input('Chiều dài cánh hoa')
    PW = st.number_input('Chiều rộng cánh hoa')

    if st.button('Dự Đoán'):
    	result = clf.predict([[SL,SW,PL,PW]])

    	if result == 0:
    		st.success('Setosa')
    	elif result == 1:
    		st.success('Versicolor')
    	else:
    		st.success('Virginica')
    		
if __name__=='__main__':
    main()