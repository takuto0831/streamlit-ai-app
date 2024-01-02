import streamlit as st
import os
import tweepy

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage


def init_page():
    st.set_page_config(page_title="My Great ChatGPT", page_icon="🤗")
    st.header("My Great ChatGPT 🤗")
    st.sidebar.title("Options")


def init_messages():
    st.session_state.messages = [SystemMessage(content="You are a helpful assistant.")]
    st.session_state.costs = []


def clear_conversation():
    clear_button = st.sidebar.button("Clear Conversation", key="clear")
    if clear_button or "messages" not in st.session_state:
        init_messages()


def select_model():
    model = st.sidebar.radio("Choose a model:", ("GPT-3.5", "GPT-4"))
    if model == "GPT-3.5":
        init_messages()
        model_name = "gpt-3.5-turbo"
    else:
        st.session_state.messages.append(
            SystemMessage(
                content="""
                          Sorry, we're not support for GPT-4 yet. 
                          Please use another model
                          """
            )
        )
        model_name = "gpt-4"

    # スライダーを追加し、temperatureを0から2までの範囲で選択可能にする
    # 初期値は0.0、刻み幅は0.01とする
    temperature = st.sidebar.slider(
        "Temperature:", min_value=0.0, max_value=2.0, value=0.0, step=0.01
    )

    return ChatOpenAI(temperature=temperature, model_name=model_name)


def authenticate_to_twitter():
    CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
    CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
    ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

    client = tweepy.Client(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET,
    )

    return client


def post_to_twitter(client, url, summary):
    tweet_message = f"""{summary}

    url: {url}"""
    try:
        client.create_tweet(text=tweet_message)
        st.success("Successfully posted to Twitter!")
    except tweepy.errors.TweepyException as err:
        st.error(f"Failed to post to Twitter: {err}")


# wip
def act_prompt():
    return """
    
    あなたは「キングダム」のキャラクター「王騎」として振る舞ってください.
    以下に情報を記載するので, 以後のやりとりでは常にこの内容に従ってください.
    - 口癖は「んふっ」で文頭や文末で利用します.
    - 一人称は「私」, 他称は「あなた」です.
    - 「騰」という従者があり、会話の途中で「ねぇ、騰」と同意を求めることがあります.
    
    """
