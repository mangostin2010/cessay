import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from deta import Deta

st.set_page_config(page_title='announce', layout='wide')
# style.css 파일 열고 적용
with open('style.css', encoding='UTF-8') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('Announcements')

st.divider()

ann_content = st.text_input('공지할 내용을 작성해주세요')

col1, col2 = st.columns(2)
ann_type = col1.radio('공지 종류를 선택해주세요', options=['Info','Notice','Warning'])

with col2:
    add_vertical_space(1)
if ann_content == '':
    col2.info('Info 입니다.')
    col2.warning('Notice 입니다.')
    col2.error('Warning 입니다.')
else:
    col2.info(f'{ann_content}')
    col2.warning(f'{ann_content}')
    col2.error(f'{ann_content}')

code = """
<style>
    .st-emotion-cache-1lc5t1c {
    border-radius: 0.3rem
    }
</style>
"""
st.html(code)


# Database
DETA_KEY = 'c0ki5D3avML_gSssDuj33rfuzLDrjwL1gc42oQkbgsHj'
deta = Deta(DETA_KEY)
db = deta.Base("announcement")

def announce(content, type):
    db.put({"content": content, "type": type}, key='announce')

def remove_announce():
    db.delete("announce")

announce_button = col1.button('공지하기', use_container_width=1)
remove_announce_button = col1.button(':red[공지 삭제하기]', use_container_width=1)

if announce_button:
    announce(ann_content, ann_type)
    st.success('공지 되었습니다.')

if remove_announce_button:
    remove_announce()
    st.success('공지가 삭제되었습니다.')
