import pickle
import streamlit as st
from sklearn.tree import DecisionTreeClassifier
with open('iris_classifier.pickle','rb') as f:
    clf = pickle.load(f)

def main():
    st.title('(^_^)__Hello You, Tôi là Bảo đây!!__(^_^)')
    st.subheader('Come on!! Hãy dự đoán tên loài hoa thuộc dòng IRIS cùng tôi nào!!')

    st.header('Vui lòng nhập số đo mà bạn dự đoán dưới đây:')
    SL = st.number_input('Chiều dài đài hoa')
    SW = st.number_input('Chiều rộng đài hoa')
    PL = st.number_input('Chiều dài cánh hoa')
    PW = st.number_input('Chiều rộng cánh hoa')

    if st.button('Dự Đoán'):
    	result = clf.predict([[SL,SW,PL,PW]])

    	if result == 0:
    		st.success('Hey! Kết quả là Setosa,Giỏi lắm!')
    	elif result == 1:
    		st.success('Yeah! Kết quả là Versicolor,Tuyệt vời!')
    	else:
    		st.success('Yess! Kết quả là Virginica,Hoàn hảo!')
    		
if __name__=='__main__':
    main()
