import numpy as np 
import pandas as pd 

import streamlit as st 

st.set_page_config(layout = 'wide')

st.header("Konoha - The Village Hidded in the Leaves")

st.subheader("List of Hokage") 

st.text("1. HashiRama Senju\n2. TobiRama Senju\n3. Hiruzen Sarutobi\n4. Minato Namikaze\n5. Tsunade Senju\n6. Kakashi Hatake\n7. Naruto Uzimaki\n8. Shikamaru Nara")

st.markdown("**Greatest Shinobi Of All Time** - *Naruto Uzimaki* (`God of Shadow Clone Jutsu`)[Click](https://naruto.fandom.com/wiki/Shadow_Clone_Technique)")

st.caption("Son of Minato Namikaze & Kushina Uzimaki")


code_sample = '''

def isPrime(n : int) -> bool:
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False 
    else:
        return True 
    
'''

st.code(code_sample, language= 'python')

st.write("Naruto Uzimaki") 
st.write(26) 
st.write(['Shadow Clone Jutsu', 'Raesengan', 'RasenShurican', 'Sage Mode'])

d = {
    "Country" : ['India', 'USA', 'China', 'Germany'], 
    "Capital" : ['New Delhi', 'Washington D.c.', 'Beijing', 'Berlin'], 
    "Currency" : ['INR','USD', 'Yuan', 'EUR'], 
    "Development Status" : ['Developing', 'Developed', 'Developed', 'Developed']
}

st.write(d) 

df = pd.DataFrame(d) 

st.write(df)

st.dataframe(df, use_container_width= True, hide_index= True) 

st.table(df)   

st.json(d) 