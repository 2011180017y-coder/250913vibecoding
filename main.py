import streamlit as st
st.title('나의 첫 웹앱!!!!!!!')
st.write('드가자')
import streamlit as st

# 서울 구 리스트
seoul_districts = [
    "종로구", "중구", "용산구", "성동구", "광진구", "동대문구", "중랑구",
    "성북구", "강북구", "도봉구", "노원구", "은평구", "서대문구", "마포구",
    "양천구", "강서구", "구로구", "금천구", "영등포구", "동작구", "관악구",
    "서초구", "강남구", "송파구", "강동구"
]

# 맛집 및 관광지 데이터 (예시)
recommendations = {
    "종로구": {
        "맛집": ["전통 한식당 (비빔밥)", "광화문 숨은 맛집"],
        "관광지": ["경희궁", "덕수궁", "북악팔각정"]
    },
    "마포구": {
        "맛집": ["찜 요리 중식당", "홍대 퓨전 음식점"],
        "관광지": ["홍제천 카페폭포"]
    },
    "강남구": {
        "맛집": ["해산물 파스타 이탈리안 레스토랑"],
        "관광지": ["가로수길", "롯데월드타워"]
    },
    "서대문구": {
        "맛집": ["티라미수 카페"],
        "관광지": ["돈의문 박물관 마을"]
    },
    "성동구": {
        "맛집": ["성수동 숨은 맛집"],
        "관광지": ["서울숲"]
    },
    "관악구": {
        "맛집": ["신림동 백반집"],
        "관광지": ["관악산 계곡"]
    },
    "강서구": {
        "맛집": ["마곡나루 맛집"],
        "관광지": ["서울식물원"]
    },
    "송파구": {
        "맛집": ["잠실 맛집"],
        "관광지": ["롯데월드"]
    }
}

# UI 구성
st.title("서울 구별 맛집 & 관광지 추천")
selected_districts = st.multiselect("서울의 구를 선택하세요", seoul_districts)

if selected_districts:
    for district in selected_districts:
        st.subheader(f"📍 {district}")
        data = recommendations.get(district)
        if data:
            st.markdown("**🍽️ 맛집 추천:**")
            for place in data["맛집"]:
                st.write(f"- {place}")
            st.markdown("**🗺️ 관광지 추천:**")
            for spot in data["관광지"]:
                st.write(f"- {spot}")
        else:
            st.write("추천 정보가 아직 준비되지 않았어요 😢")
