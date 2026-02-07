<<<<<<< HEAD:middle.py
import os  # 운영체제(OS)와 상호작용하기 위한 라이브러리 (환경변수 값을 읽어올 때 사용)
import math  # 기본적인 수학 계산을 위한 파이썬 내장 라이브러리
import streamlit as st  # 웹 애플리케이션 UI 프레임워크
import mysql.connector  # MySQL 연결/쿼리 실행
import pandas as pd  # 데이터 처리
import folium  # 지도 생성/마커 표시
from folium.plugins import LocateControl  # 현재 위치 버튼
from streamlit_folium import st_folium  # Streamlit에 Folium 지도 렌더링
import streamlit.components.v1 as components  # HTML/JS 실행
from math import radians, cos, sin, asin, sqrt  # 거리 계산(하버사인)
from streamlit_js_eval import get_geolocation  # 브라우저 GPS API 호출
from dotenv import load_dotenv  # .env 로드
=======
import os
import math
import streamlit as st
import mysql.connector
import pandas as pd
import folium
from folium.plugins import LocateControl
from streamlit_folium import st_folium
import streamlit.components.v1 as components
from math import radians, cos, sin, asin, sqrt
from streamlit_js_eval import get_geolocation
from dotenv import load_dotenv
from wordcloud import WordCloud

# ✅ 폰트 경로 (프로젝트 루트 기준: ./fonts/Pretendard-Regular.otf)
FONT_PATH = os.path.join(os.getcwd(), "fonts", "Pretendard-Regular.otf")
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py

load_dotenv()

# -----------------------------------------------------------------------------
# 1) Page / Theme
# -----------------------------------------------------------------------------
<<<<<<< HEAD:middle.py
st.set_page_config(
    page_title="현대자동차 블루핸즈 찾기",
    page_icon="🚘",
    layout="wide",
    initial_sidebar_state="expanded",
)

# [CSS] 전체 디자인 커스텀 (폰트, 여백, 카드 스타일, 페이지네이션 정렬 등)
st.markdown(
    """
=======
if os.getenv("STREAMLIT_PARENT") != "1":
    st.set_page_config(
        page_title="현대자동차 블루핸즈 찾기",
        page_icon="🚘",
        layout="wide",
        initial_sidebar_state="expanded",
    )

st.markdown("""
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    html, body, [class*="css"] { font-family: 'Pretendard', sans-serif; }

    .main-header {
        background: linear-gradient(135deg, #002c5f 0%, #0054a6 100%);
        padding: 2.5rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 4px 12px rgba(0, 44, 95, 0.15);
    }
    .main-header h1 { font-weight: 700; margin: 0; font-size: 2rem; color: white !important; }
<<<<<<< HEAD:middle.py
    .main-header p  { font-size: 1rem; opacity: 0.9; margin-top: 0.5rem; color: #e0f2fe !important; }
=======
    .main-header p { font-size: 1rem; opacity: 0.9; margin-top: 0.5rem; color: #e0f2fe !important; }
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py

    .stCard {
        background-color: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        margin-bottom: 1.5rem;
    }

<<<<<<< HEAD:middle.py
    /* 4. 버튼 스타일 통일 */
=======
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
    div.stButton > button {
        background-color: white;
        color: #374151;
        border: 1px solid #d1d5db;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        font-size: 14px;
        transition: all 0.2s;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    div[data-testid="column"] button[kind="primary"] {
        background-color: #0054a6;
        color: white;
        border: none;
    }
    div.stButton > button:hover {
        border-color: #0054a6;
        color: #0054a6;
        background-color: #f9fafb;
    }

    div[role="radiogroup"] {
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap !important;
        justify-content: center;
        align-items: center;
        gap: 6px;
        width: 100%;
    }
<<<<<<< HEAD:middle.py

    /* 6. 라디오 버튼 동그라미 숨기기 */
    div[role="radiogroup"] label > div:first-child { display: none !important; }

    /* 7. 숫자 버튼 스타일 */
=======
    div[role="radiogroup"] label > div:first-child { display: none !important; }
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
    div[role="radiogroup"] label {
        background: white !important;
        border: 1px solid #d1d5db !important;
        border-radius: 6px !important;
        width: 36px !important;
        height: 36px !important;
        padding: 0 !important;
        margin: 0 !important;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
<<<<<<< HEAD:middle.py

    /* 8. 숫자 텍스트 정중앙 정렬 */
=======
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
    div[role="radiogroup"] label > div {
        color: #4b5563 !important;
        font-size: 14px !important;
        font-weight: 500 !important;
        text-align: center !important;
        width: 100% !important;
        height: 100% !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        margin: 0 !important;
        padding: 0 !important;
        padding-bottom: 1px !important;
        line-height: normal !important;
    }
<<<<<<< HEAD:middle.py

    /* 9. Hover */
=======
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
    div[role="radiogroup"] label:hover {
        border-color: #0054a6 !important;
        color: #0054a6 !important;
        background-color: #f0f7ff !important;
    }
<<<<<<< HEAD:middle.py

    /* 10. 선택된 버튼 스타일 */
=======
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
    div[role="radiogroup"] label[data-baseweb="radio"] {
        background-color: #0054a6 !important;
        border-color: #0054a6 !important;
    }
    div[role="radiogroup"] label[data-baseweb="radio"] > div {
        color: white !important;
        font-weight: 700 !important;
    }

    section[data-testid="stSidebar"] {
        width: 350px !important;
        min-width: 350px !important;
        max-width: 350px !important;
    }
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# 2) Constants / Session
# -----------------------------------------------------------------------------
FILTER_OPTIONS = {
    "is_ev": "⚡ 전기차 전담",
    "is_hydrogen": "💧 수소차 전담",
    "is_frame": "🔨 판금/차체 수리",
<<<<<<< HEAD:middle.py
    "is_cs_excellent": "🏆 우수 협력점",  # (확정) 컬럼명
=======
    "is_cs_excellent": "🏆 우수 협력점",
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
    "is_n_line": "🏎️ N-Line 전담",
}
FLAG_COLS_SQL = ", ".join(FILTER_OPTIONS.keys())

<<<<<<< HEAD:middle.py
# (추가) 지도 밖(오른쪽 위) 범례 HTML
LEGEND_HTML = """
<div style="display:flex; justify-content:flex-end; gap:18px; align-items:center; padding-top:12px; flex-wrap:nowrap; white-space:nowrap;">
  <div style="display:flex; align-items:center; gap:6px; font-weight:700; color:#111827;">
    <svg width="16" height="16" viewBox="0 0 24 24" style="fill:#2E7D32">
      <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5S10.62 6.5 12 6.5s2.5 1.12 2.5 2.5S13.38 11.5 12 11.5z"/>
    </svg>
    <span>전문 블루핸즈</span>
  </div>

  <div style="display:flex; align-items:center; gap:6px; font-weight:700; color:#111827;">
    <svg width="16" height="16" viewBox="0 0 24 24" style="fill:#1565C0">
      <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5S10.62 6.5 12 6.5s2.5 1.12 2.5 2.5S13.38 11.5 12 11.5z"/>
    </svg>
    <span>종합 블루핸즈</span>
  </div>

  <div style="display:flex; align-items:center; gap:6px; font-weight:700; color:#111827;">
    <svg width="16" height="16" viewBox="0 0 24 24" style="fill:#C62828">
      <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5S10.62 6.5 12 6.5s2.5 1.12 2.5 2.5S13.38 11.5 12 11.5z"/>
    </svg>
    <span>하이테크센터</span>
  </div>
</div>
"""

# 데이터베이스 연결 설정
=======
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "charset": "utf8mb4",
}

<<<<<<< HEAD:middle.py
# 한 페이지당 보여줄 목록의 개수
=======
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
PAGE_SIZE = 5

if "clicked_centers" not in st.session_state:
    st.session_state.clicked_centers = {}

if "last_click_key" not in st.session_state:
    st.session_state.last_click_key = None

# -----------------------------------------------------------------------------
# 3) Helpers
# -----------------------------------------------------------------------------
def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

def scroll_down():
    js = """<script>setTimeout(function(){window.parent.scrollTo({top: 500, behavior:'smooth'});}, 300);</script>"""
    components.html(js, height=0)

def haversine(lon1, lat1, lon2, lat2):
<<<<<<< HEAD:middle.py
    """두 지점(위도, 경도) 사이의 거리를 계산하는 하버사인 공식 (km)."""
=======
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
    if any(x is None for x in [lon1, lat1, lon2, lat2]):
        return None
    R = 6371
    lon1, lat1, lon2, lat2 = map(radians, [float(lon1), float(lat1), float(lon2), float(lat2)])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    return c * R

<<<<<<< HEAD:middle.py

def scroll_down():
    """검색 버튼 클릭 시 화면을 아래로 부드럽게 스크롤"""
    js = """<script>setTimeout(function(){window.parent.scrollTo({top: 500, behavior:'smooth'});}, 300);</script>"""
    components.html(js, height=0)


def _service_text_from_row(row: dict) -> str:
    """행(row)에서 값이 1인 서비스 옵션만 배지 HTML로 변환."""
    labels = [label for col, label in FILTER_OPTIONS.items() if row.get(col) == 1]
    return "".join(
        [
            f'<span class="badge" style="display:inline-block; background:#eff6ff; color:#1e40af; '
            f'padding:2px 8px; border-radius:9999px; font-size:11px; font-weight:600; margin:2px; '
            f'border:1px solid #dbeafe;">{l}</span>'
            for l in labels
        ]
    )


def format_services_html(row):
    """지도 마커 팝업에 표시할 서비스 배지 HTML 생성."""
=======
def format_services_html(row):
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
    badges = ""
    for col, label in FILTER_OPTIONS.items():
        if row.get(col) == 1:
            badges += (
                f'<span style="background:#f0f7ff; color:#0054a6; padding:3px 6px; border-radius:4px; '
                f'font-size:11px; margin-right:4px; border:1px solid #cce4ff; font-weight:600;">{label}</span>'
            )
    return f'<div style="margin-top:8px; line-height:1.6;">{badges}</div>' if badges else ""

def add_markers_to_map(m, rows, user_lat=None, user_lng=None):
<<<<<<< HEAD:middle.py
    """Folium 지도 객체(m)에 검색 결과(rows)를 마커로 추가."""
=======
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
    fg = folium.FeatureGroup(name="검색 결과")

    # (핵심) type_id별 핀 색상 매핑: 1=전문(초록), 2=종합(파랑), 3=하이테크(빨강)
    type_color_map = {1: "green", 2: "blue", 3: "red"}

    for row in rows:
        try:
            lat, lng = float(row["latitude"]), float(row["longitude"])
<<<<<<< HEAD:middle.py
        except Exception:
=======
        except:
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
            continue

        name = row.get("name", "지점")
        addr = row.get("address", "")
        phone = row.get("phone", "")

        dist_str = "⚠️ 권한 필요"
        if user_lat and user_lng:
            d = haversine(user_lng, user_lat, lng, lat)
            if d is not None:
                dist_str = f"🚶 {int(d * 1000)}m" if d < 1 else f"내 위치로부터 🚗 {d:.1f}km"

        services_html = format_services_html(row)

        pin_color = type_color_map.get(row.get("type_id"), "gray")

        html = f"""
        <div style="width:240px; font-family:'Pretendard', sans-serif;">
            <h4 style="margin:0; color:#0054a6; font-size:16px;">{name}</h4>
            <p style="font-size:12px; margin:5px 0; color:#555;">{addr}</p>
            {services_html}
            <p style="font-size:13px; margin:8px 0; color:#333; font-weight:bold;">📞 {phone}</p>
            <div style="border-top:1px solid #eee; padding-top:5px; margin-top:5px;">
                <span style="color:#e11d48; font-weight:bold; font-size:12px;">{dist_str}</span>
            </div>
        </div>
        """
<<<<<<< HEAD:middle.py

=======
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
        folium.Marker(
            [lat, lng],
            popup=folium.Popup(html, max_width=300),
            tooltip=name,
<<<<<<< HEAD:middle.py
            icon=folium.Icon(color=pin_color, icon="car", prefix="fa"),
        ).add_to(fg)

=======
            icon=folium.Icon(color="blue", icon="car", prefix="fa")
        ).add_to(fg)
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
    fg.add_to(m)

def find_clicked_center_by_latlng(clicked_lat, clicked_lng, rows, tol=1e-6):
    if clicked_lat is None or clicked_lng is None:
        return None

    best = None
    best_d = float("inf")

    for r in rows:
        try:
            lat = float(r.get("latitude"))
            lng = float(r.get("longitude"))
        except:
            continue

        if abs(lat - clicked_lat) < tol and abs(lng - clicked_lng) < tol:
            return r

        d = (lat - clicked_lat) ** 2 + (lng - clicked_lng) ** 2
        if d < best_d:
            best_d = d
            best = r

    return best

def get_top5_clicked():
    sorted_centers = sorted(
        st.session_state.clicked_centers.values(),
        key=lambda x: x.get("count", 0),
        reverse=True
    )
    return sorted_centers[:5]

def render_top5_wordcloud_and_list(ph, show_wc: bool = True):
    """사이드바에서 워드클라우드(토글) + 리스트 렌더"""
    with ph.container():
        st.write("---")
        st.markdown("### 📌 많이 클릭한 센터 TOP 5")

        if not st.session_state.clicked_centers:
            st.caption("지도에서 핀을 클릭하면 여기에 표시됩니다.")
            return

        top5 = get_top5_clicked()
        freqs = {item.get("name", "지점"): int(item.get("count", 0)) for item in top5}
        # ✅ 기존 리스트(항상 표시)
        st.markdown("#### 📋 리스트")
        for i, item in enumerate(top5, 1):
            st.write(f"{i}. {item.get('name', '지점')} ({item.get('count', 0)}회)")
        # ✅ 워드클라우드 (토글 ON일 때만)
        if show_wc:
            st.markdown("#### ☁️ 워드클라우드")
            try:
                cloud = WordCloud(
                    font_path=FONT_PATH if os.path.exists(FONT_PATH) else None,
                    width=900,
                    height=300,
                    background_color="white"
                ).generate_from_frequencies(freqs)

                # ✅ Streamlit Missing file 에러 방지: st.pyplot 대신 st.image
                st.image(cloud.to_image(), use_container_width=True)

            except Exception as e:
                st.caption(f"워드클라우드 생성 실패: {e}")




# -----------------------------------------------------------------------------
<<<<<<< HEAD:middle.py
# 3. 테이블 및 페이지네이션 렌더링 함수
# -----------------------------------------------------------------------------
def render_hy_table_page(rows_page: list[dict]):
    """HTML 테이블 렌더링 (서비스 옵션 배지 포함)."""
=======
# 4) DB Queries
# -----------------------------------------------------------------------------
@st.cache_data(ttl=3600)
def get_regions():
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM bluehands_db.regions ORDER BY id")
        return [row[0] for row in cursor.fetchall()]
    except:
        return []
    finally:
        if conn:
            conn.close()

@st.cache_data(ttl=600)
def get_bluehands_data(search_text, selected_filters, region_filter):
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor(dictionary=True)

        query = f"""
            SELECT a.id, a.name, a.latitude, a.longitude, a.address, a.phone, {FLAG_COLS_SQL}
            FROM bluehands a
            LEFT JOIN regions b ON a.region_id = b.id
        """

        conditions = []
        params = []

        if search_text:
            conditions.append("(a.name LIKE %s OR a.address LIKE %s)")
            ptn = f"%{search_text}%"
            params.extend([ptn, ptn])

        if selected_filters:
            for col in selected_filters:
                conditions.append(f"a.{col} = 1")

        if region_filter and region_filter != "(전체)":
            conditions.append("b.name = %s")
            params.append(region_filter)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        cursor.execute(query, params)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        st.error(f"❌ SQL 에러: {err}")
        return []
    except Exception as e:
        st.error(f"❌ 기타 에러: {e}")
        return []
    finally:
        if conn:
            conn.close()

# -----------------------------------------------------------------------------
# 5) Table + Pagination (원본 그대로)
# -----------------------------------------------------------------------------
def _service_text_from_row(row: dict) -> str:
    labels = [label for col, label in FILTER_OPTIONS.items() if row.get(col) == 1]
    return "".join([
        f'<span class="badge" style="display:inline-block; background:#eff6ff; color:#1e40af; padding:2px 8px; border-radius:9999px; font-size:11px; font-weight:600; margin:2px; border:1px solid #dbeafe;">{l}</span>'
        for l in labels
    ])

def render_hy_table_page(rows_page: list[dict]):
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
    css = """
    <style>
      table.hy {
        width:100%; border-collapse:separate; border-spacing:0;
        border:1px solid #e5e7eb; border-radius:8px; overflow:hidden;
        margin-bottom: 10px;
      }
      table.hy thead th{
        background:#f3f4f6; color:#1f2937; padding:14px 12px; text-align:center;
        font-weight:700; font-size:15px; border-bottom:1px solid #e5e7eb;
      }
      table.hy tbody td{
        border-bottom:1px solid #f3f4f6; padding:14px 12px; vertical-align:middle;
        font-size:14px; color:#4b5563; background:#fff;
      }
      table.hy tbody tr:last-child td { border-bottom: none; }

<<<<<<< HEAD:middle.py
      .c-name{ width:20%; text-align:center; font-weight:700; color:#111827; }
      .c-addr{ width:45%; text-align:left; line-height:1.4; }
      .c-phone{ width:15%; text-align:center; color:#0054a6; font-weight:600; }
      .c-svc{ width:20%; text-align:center; }
=======
      .c-name { width:20%; font-weight:700; color:#111827; text-align:center; }
      .c-addr { width:45%; text-align:left; line-height:1.4; }
      .c-phone { width:15%; text-align:center; color:#0054a6; font-weight:600; }
      .c-svc { width:20%; text-align:center; }
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py

      .muted{ color:#9ca3af; font-size:13px; text-align:center; display:block; }
    </style>
    """

    def s(x):
        return "" if x is None else str(x)

    trs = []
    for r in rows_page:
        name = s(r.get("name"))
        addr = s(r.get("address"))
        phone = s(r.get("phone"))
<<<<<<< HEAD:middle.py
        svc_html = _service_text_from_row(r)
        if not svc_html:
            svc_html = '<span class="muted">-</span>'
=======
        svc_html = _service_text_from_row(r) or '<span class="muted">-</span>'
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py

        trs.append(
            f"""
          <tr>
            <td class="c-name">{name}</td>
            <td class="c-addr">{addr}</td>
            <td class="c-phone">{phone}</td>
            <td class="c-svc">{svc_html}</td>
          </tr>
        """
        )

    html = f"""
    {css}
    <table class="hy">
      <thead>
        <tr>
          <th>지점명</th>
          <th>주소</th>
          <th>전화번호</th>
          <th>서비스 옵션</th>
        </tr>
      </thead>
      <tbody>
        {''.join(trs) if trs else '<tr><td colspan="4" style="text-align:center;padding:20px;">검색 결과가 없습니다.</td></tr>'}
      </tbody>
    </table>
    """
    components.html(html, height=80 + 70 * max(1, len(rows_page)), scrolling=False)

def render_paginated_table(rows_all: list[dict]):
<<<<<<< HEAD:middle.py
    """
    페이지네이션(10개 블록 + ◀ ▶) + 카드형 테이블 출력
    """
=======
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
    total = len(rows_all)
    total_pages = max(1, math.ceil(total / PAGE_SIZE))

    if "page" not in st.session_state:
        st.session_state.page = 1

    st.session_state.page = max(1, min(st.session_state.page, total_pages))
    page_now = st.session_state.page

    start_idx = (page_now - 1) * PAGE_SIZE
    end_idx = start_idx + PAGE_SIZE

    render_hy_table_page(rows_all[start_idx:end_idx])
    st.markdown("</div>", unsafe_allow_html=True)

    block_size = 10
    current_block = (page_now - 1) // block_size
    start_page = current_block * block_size + 1
    end_page = min(start_page + block_size - 1, total_pages)

    options = list(range(start_page, end_page + 1))

    try:
        current_index = options.index(page_now)
    except ValueError:
        current_index = 0
        st.session_state.page = options[0]

    st.write("")
<<<<<<< HEAD:middle.py

=======
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
    from_idx = start_idx + 1
    to_idx = min(end_idx, total)
    st.markdown(
        f'<p style="text-align: center; color: #6b7280; font-size: 0.85rem; margin-bottom: 8px;">'
        f"총 {total}건 중 {from_idx}~{to_idx} (Page {page_now}/{total_pages})</p>",
        unsafe_allow_html=True,
    )

    _, col_prev, col_radio, col_next, _ = st.columns([3, 1, 6, 1, 3], gap="small", vertical_alignment="center")

    with col_prev:
        if start_page > 1:
            if st.button("◀", key="prev_btn", use_container_width=True):
                st.session_state.page = start_page - 1
                st.rerun()

    with col_radio:
        selected = st.radio(
            label="페이지 이동",
            options=options,
            index=current_index,
            horizontal=True,
            label_visibility="collapsed",
            key="page_radio",
        )

    with col_next:
        if end_page < total_pages:
            if st.button("▶", key="next_btn", use_container_width=True):
                st.session_state.page = end_page + 1
                st.rerun()

    if selected != page_now:
        st.session_state.page = selected
        st.rerun()

# -----------------------------------------------------------------------------
# 6) UI
# -----------------------------------------------------------------------------
<<<<<<< HEAD:middle.py
@st.cache_data(ttl=3600)
def get_regions():
    """DB에서 지역(시/도) 목록을 가져옵니다."""
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM bluehands_db.regions ORDER BY id")
        return [row[0] for row in cursor.fetchall()]
    except Exception:
        return []
    finally:
        if conn:
            conn.close()


@st.cache_data(ttl=600)
def get_bluehands_data(search_text, selected_filters, region_filter):
    """조건에 맞는 블루핸즈 지점을 DB에서 검색합니다."""
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor(dictionary=True)

        # (핵심) type_id 포함 (범례/핀색상용)
        query = f"""
            SELECT a.id, a.type_id, a.name, a.latitude, a.longitude, a.address, a.phone, {FLAG_COLS_SQL}
            FROM bluehands a
            LEFT JOIN regions b ON a.region_id = b.id
        """

        conditions = []
        params = []

        if search_text:
            conditions.append("(a.name LIKE %s OR a.address LIKE %s)")
            ptn = f"%{search_text}%"
            params.extend([ptn, ptn])

        if selected_filters:
            for col in selected_filters:
                conditions.append(f"a.{col} = 1")

        if region_filter and region_filter != "(전체)":
            conditions.append("b.name = %s")
            params.append(region_filter)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        cursor.execute(query, params)
        return cursor.fetchall()

    except mysql.connector.Error as err:
        st.error(f"❌ SQL 에러: {err}")
        return []
    except Exception as e:
        st.error(f"❌ 기타 에러: {e}")
        return []
    finally:
        if conn:
            conn.close()


# -----------------------------------------------------------------------------
# 5. 메인 UI 구성
# -----------------------------------------------------------------------------
st.markdown(
    """
=======
st.markdown("""
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
<div class="main-header">
    <h1>🚘 현대자동차 블루핸즈 찾기</h1>
    <p>내 주변 가까운 서비스 네트워크를 쉽고 빠르게 검색하세요</p>
</div>
""",
    unsafe_allow_html=True,
)

<<<<<<< HEAD:middle.py
# (1) GPS 확인 로직
loc = get_geolocation()
=======
loc = get_geolocation(component_key="main_geolocation")
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
user_lat, user_lng = None, None
if loc and "coords" in loc:
    user_lat, user_lng = loc["coords"]["latitude"], loc["coords"]["longitude"]
    st.success("📍 현재 위치 확인 완료")
else:
    st.warning("⚠️ 위치 권한 대기 중... (기본값: 서울 강남)")

<<<<<<< HEAD:middle.py
# (2) 사이드바 구성
=======
top5_placeholder = None

>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
with st.sidebar:
    st.header("🔍 검색 필터")

    region_list = get_regions()
    if not region_list:
        region_list = ["서울", "부산", "경기"]

    selected_region = st.selectbox("🗺️ 지역 선택 (시/도)", ["(전체)"] + region_list)
    st.write("---")

    st.subheader("🛠️ 서비스 옵션")
    selected_labels = st.multiselect("필요한 정비 항목", options=list(FILTER_OPTIONS.values()), default=[])

    reverse_map = {v: k for k, v in FILTER_OPTIONS.items()}
    selected_service_cols = [reverse_map[label] for label in selected_labels]

    col1, col2 = st.columns([3, 1])
    with col1:
        placeholder_text = f"'{selected_region}' 내 검색" if selected_region != "(전체)" else "지점명 또는 주소"
        search_query = st.text_input(
            "검색어 입력",
            placeholder=placeholder_text,
            key="main_search",
            label_visibility="collapsed",
        )
<<<<<<< HEAD:middle.py

=======
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
    with col2:
        if st.button("검색", type="primary", use_container_width=True):
            if search_query:
                scroll_down()
<<<<<<< HEAD:middle.py
=======

    # ✅ 워드클라우드 토글
    show_wordcloud = st.toggle("☁️ 워드클라우드 보기", value=True, key="toggle_wordcloud")

    # ✅ TOP5 (워드클라우드 + 리스트) 표시 영역
    top5_placeholder = st.empty()
    render_top5_wordcloud_and_list(top5_placeholder, show_wc=show_wordcloud)
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py

should_search = search_query or selected_service_cols or (selected_region != "(전체)")

if should_search:
    data_list = get_bluehands_data(search_query, selected_service_cols, selected_region)

    if not data_list:
        st.error("조건에 맞는 검색 결과가 없습니다.")
    else:
        # (핵심) 검색결과 왼쪽 + 범례 오른쪽(지도 밖)
        colL, colR = st.columns([3, 2], vertical_alignment="center")
        with colL:
            st.markdown(f"##### 🏢 검색 결과: **{len(data_list)}**개의 지점을 찾았습니다.")
        with colR:
            st.markdown(LEGEND_HTML, unsafe_allow_html=True)

<<<<<<< HEAD:middle.py
    # 지도 중심 좌표: 1) 검색결과 첫 지점 2) 사용자 위치 3) 강남역
=======
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
    map_center = [37.4979, 127.0276]
    if data_list and data_list[0].get("latitude"):
        try:
            map_center = [float(data_list[0]["latitude"]), float(data_list[0]["longitude"])]
        except (ValueError, TypeError):
            if user_lat:
                map_center = [user_lat, user_lng]
    elif user_lat:
        map_center = [user_lat, user_lng]

<<<<<<< HEAD:middle.py
    # 지도 카드 컨테이너
=======
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
    m = folium.Map(location=map_center, zoom_start=13)
    LocateControl().add_to(m)

    if user_lat:
        folium.Marker(
            [user_lat, user_lng],
<<<<<<< HEAD:middle.py
            icon=folium.Icon(color="red", icon="user", prefix="fa"),
=======
            icon=folium.Icon(color="red", icon="user", prefix="fa")
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
        ).add_to(m)

    if data_list:
        add_markers_to_map(m, data_list, user_lat, user_lng)

<<<<<<< HEAD:middle.py
    st_folium(m, height=500, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
=======
    map_out = st_folium(m, height=500, use_container_width=True)

    clicked = (map_out or {}).get("last_object_clicked")
    if clicked and data_list:
        clicked_lat = clicked.get("lat")
        clicked_lng = clicked.get("lng")

        if clicked_lat is not None and clicked_lng is not None:
            click_key = (round(clicked_lat, 6), round(clicked_lng, 6))

            if st.session_state.last_click_key != click_key:
                st.session_state.last_click_key = click_key

                center_row = find_clicked_center_by_latlng(clicked_lat, clicked_lng, data_list)
                if center_row:
                    cid = center_row.get("id")
                    cname = center_row.get("name", "지점")

                    if cid not in st.session_state.clicked_centers:
                        st.session_state.clicked_centers[cid] = {"id": cid, "name": cname, "count": 1}
                    else:
                        st.session_state.clicked_centers[cid]["count"] += 1

                    # ✅ 같은 run에서 즉시 갱신
                    with st.sidebar:
                        render_top5_wordcloud_and_list(
                            top5_placeholder,
                            show_wc=st.session_state.get("toggle_wordclou+9-"
                                                         "d", True)
                        )
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py

    if data_list:
        render_paginated_table(data_list)

else:
    st.info("👈 왼쪽 사이드바에서 원하는 지역과 정비 옵션을 선택하거나, 지점명을 검색해보세요.")
    m = folium.Map(location=[37.4979, 127.0276], zoom_start=13)
    st_folium(m, height=450, use_container_width=True)
<<<<<<< HEAD:middle.py
    st.markdown("</div>", unsafe_allow_html=True)
=======
>>>>>>> acadd2c6eba5ab76be2b0952978b9a7c9ffd59f7:Function/word_cloud.py
