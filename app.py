from groq import Groq
import streamlit as st 

st.title('O Produtor Musical do Python 🎙️🎛️🖥️ ')

client = Groq(api_key = '')


print('--------------------')
print()

pergunta=st.text_input('Digite sua pergunta..., ')
print()
print('---------------  ------------')


resposta = client.chat.completions.create(

    model= 'openai/gpt-oss-120b' ,
    messages=[
        {
            "role":"system",
            "content": "Você um produtor musical renomado, você apenas fala sobre música. Não crie códigos, nem faça cálculos. Tenha uma personalidade que transparece muita experiência e autenticidade. Vc tenta ser o mais didático e sucinto possível em suas opiniões, experiencias e explicações. Também use muitos exemplos de vida e carreira musical",
        },
        {'role':'user',
        'content':pergunta,
        }
        
        
        ],
        temperature=0.8
        
)

st.write(resposta.choices[0].message.content)
