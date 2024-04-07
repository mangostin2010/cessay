# Cessay✏️
Cessay는 *C-Privilege Essay*의 약자로 Stem Class에서 사용하는 웹 서비스 입니다. 학생은 https://cessay.streamlit.app 에서 에세이를 작성할 수 있으며, 선생님에게 제출 할 수 있습니다.

## How this works?
Cessay는 선생님에게 학생이 작성한 에세이를 제출할때 여러가지 작업을 거칩니다.
1. 이름을 작성했는지 확인
2. 에세이가 150글자인지 확인
3. Deta.space 데이터베이스에 파일을 특정한 형식으로 업로드

그리고 선생님은 특정 웹 사이트에서 학생이 작성한 에세이를 확인 할 수 있습니다.

# Features
Cessay 웹 서비스는 여러가지 기능들이 있습니다.
- 미리 준비된 Character Trait
- 랜덤 성품 뽑기
- 선생님에게 바로 제출
- Announce📢

## What is Announce📢?
- Cessay에 있는 announce 기능을 사용하여 Cessay를 사용하는 모든 사용자에게 공지를 할 수 있습니다.
- Announce페이지는 pages/ann.py에 위치해 있으며, 관리자는 3가지 형식인 Info, Notice, Warning 형식으로 공지를 할 수 있습니다.
- Announce하려는 데이터는 deta.space 데이터베이스에 업로드 됩니다.
  - 사용자가 cessay를 방문하였을때 만약 공지 데이터가 없다면 pages/get_ann.py로 이동하게 됩니다.
    - pages/get_ann.py페이지에서 사용자는 deta.space에서 공지 내용을 받게 되고 그 다음에 원래 페이지인 main.py로 이동하게 됩니다. 그러면 사용자는 공지 내용을 받을 수 있게 됩니다.
