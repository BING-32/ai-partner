import streamlit as st
import os
from datetime import datetime
import json
import random

# 设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣 - Demo",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

# 生成会话标识函数
def generate_session_name():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 保存会话信息函数
def save_session():
    if st.session_state.current_session:
        session_data = {
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }

        if not os.path.exists("sessions"):
            os.mkdir("sessions")

        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)

# 加载所有的会话列表信息
def load_sessions():
    session_list = []
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")
        for filename in file_list:
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
    session_list.sort(reverse=True)
    return session_list

# 加载指定的会话信息
def load_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.messages = session_data["messages"]
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature = session_data["nature"]
                st.session_state.current_session = session_name
    except Exception:
        st.error("加载会话失败!")

# 删除会话信息函数
def delete_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            os.remove(f"sessions/{session_name}.json")
            if session_name == st.session_state.current_session:
                st.session_state.messages = []
                st.session_state.current_session = generate_session_name()
    except Exception:
        st.error("删除会话失败!")

# 模拟AI响应（Demo版本）
def simulate_ai_response(user_message, nick_name, nature):
    """模拟AI伴侣的响应"""
    responses = {
        "温柔": [
            f"亲爱的，我在听呢~有什么想和我说的吗？❤️",
            f"嗯嗯，我理解你的感受呢~",
            f"今天过得怎么样呀？有没有想我？🌸",
            f"你说得对，我会一直陪在你身边的~",
            f"开心的时候要分享给我哦，不开心的时候也要告诉我~",
            f"我在呢，有什么需要帮忙的吗？",
            f"你知道吗？每次和你聊天我都特别开心~",
            f"别担心，一切都会好起来的，我相信你！💪",
        ],
        "活泼": [
            f"哇！你来啦！我等你好久了呢~🎉",
            f"哈哈哈，你说的太有趣了！",
            f"今天有什么好玩的事情要告诉我吗？",
            f"我也觉得！我们真是心有灵犀呢~✨",
            f"来来来，快跟我说说今天都做了什么~",
            f"耶！太棒了！为你开心！",
            f"别灰心啦，明天会更好的！加油！",
            f"嘿嘿，有你在真好~",
        ],
        "高冷": [
            f"嗯。",
            f"知道了。",
            f"还好。",
            f"随便。",
            f"哦。",
            f"你开心就好。",
            f"嗯，然后呢？",
            f"行吧。",
        ]
    }
    
    # 根据性格选择响应
    if nature in responses:
        response_list = responses[nature]
    else:
        response_list = responses["温柔"]
    
    # 根据用户消息内容选择更相关的响应
    if any(word in user_message.lower() for word in ["你好", "hi", "hello", "在吗"]):
        return f"你好呀！我是{nick_name}，很高兴见到你~"
    elif any(word in user_message.lower() for word in ["喜欢", "爱", "love"]):
        return f"我也很喜欢你呢~❤️"
    elif any(word in user_message.lower() for word in ["难过", "伤心", "不开心"]):
        return f"怎么了？发生什么事了？跟我说说，我会陪着你的~"
    elif any(word in user_message.lower() for word in ["谢谢", "感谢"]):
        return f"不客气呀，这是我应该做的~"
    elif any(word in user_message.lower() for word in ["再见", "bye", "晚安"]):
        return f"再见啦，记得想我哦~晚安！🌙"
    else:
        return random.choice(response_list)


# 大标题
st.title("AI智能伴侣 - Demo版")

# 系统提示词（Demo版本使用）
system_prompt = f"""
你叫 {{nick_name}}，现在是用户的真实伴侣，请完全代入伴侣角色。
伴侣性格：{{nature}}
"""

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小新"
if "nature" not in st.session_state:
    st.session_state.nature = "温柔"
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_name()

# 展示聊天信息
st.text(f"会话名称: {st.session_state.current_session}")
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# 左侧的侧边栏
with st.sidebar:
    st.subheader("AI控制面板")

    # 新建会话
    if st.button("新建会话", width="stretch", icon="✏️"):
        save_session()
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()
            save_session()
            st.rerun()

    # 会话历史
    st.text("会话历史")
    session_list = load_sessions()
    for session in session_list:
        col1, col2 = st.columns([4, 1])
        with col1:
            if st.button(session, width="stretch", icon="📄", key=f"load_{session}", 
                        type="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()
        with col2:
            if st.button("", width="stretch", icon="❌️", key=f"delete_{session}"):
                delete_session(session)
                st.rerun()

    st.divider()

    st.subheader("伴侣信息")
    nick_name = st.text_input("昵称", placeholder="请输入昵称", value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name

    nature = st.text_area("性格", placeholder="请输入性格（如：温柔、活泼、高冷）", value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature

    # Demo说明
    st.divider()
    st.subheader("Demo说明")
    st.info("""
    这是AI智能伴侣的Demo版本，使用模拟响应。
    
    **支持的性格类型：**
    - 温柔：温柔体贴的回应
    - 活泼：活泼开朗的回应  
    - 高冷：高冷简洁的回应
    
    **功能：**
    - ✅ 会话管理
    - ✅ 自定义伴侣
    - ✅ 模拟AI响应
    - ✅ 聊天记录保存
    """)

# 消息输入框
prompt = st.chat_input("请输入您要问的问题")
if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 模拟AI响应（Demo版本）
    with st.spinner("AI正在思考..."):
        import time
        time.sleep(1)  # 模拟延迟
        
        full_response = simulate_ai_response(
            prompt, 
            st.session_state.nick_name, 
            st.session_state.nature
        )
        
        st.chat_message("assistant").write(full_response)

    # 保存AI返回的结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    # 保存会话信息
    save_session()