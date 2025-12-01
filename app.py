import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

def get_llm_response(input_text, expert_type):
    """
    入力テキストと専門家の種類に基づいてLLMの応答を取得する関数。

    Args:
        input_text (str): ユーザーからの入力テキスト。
        expert_type (str): 選択された専門家の種類。

    Returns:
        str: LLMからの応答。
    """
    # 専門家の種類に基づくシステムメッセージを定義
    expert_prompts = {
        "Historian": "あなたは世界史の専門家です。",
        "Scientist": "あなたは物理学を専門とする科学者です。",
        "Chef": "あなたは国際料理の専門家であるプロのシェフです。"
    }

    system_message = expert_prompts.get(expert_type, "あなたは役に立つアシスタントです。")

    # LLMを初期化
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    # LLMに渡すメッセージを作成
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text),
    ]

    # LLMからの結果を取得
    result = llm(messages)
    return result.content

# Streamlitアプリ
st.title("LLMによる専門家アシスタント")

# アプリの説明を表示
st.markdown(
    """
    ### アプリ概要
    このアプリでは、AIを活用してさまざまな専門家として振る舞うアシスタントと対話できます。
    専門家の種類を選択し、質問を入力すると、選択した専門分野に応じた回答が得られます。

    ### 使い方
    1. ラジオボタンでAIに振る舞わせたい専門家の種類を選択します。
    2. テキスト入力欄に質問を入力します。
    3. 「送信」ボタンを押して回答を取得します。
    """
)

# 専門家の種類を選択するためのラジオボタン
expert_type = st.radio(
    "専門家の種類を選択してください:",
    ("Historian", "Scientist", "Chef")
)

# ユーザーの質問を入力するためのテキスト入力欄
user_input = st.text_input("質問を入力してください:")

# 送信ボタン
if st.button("送信"):
    if user_input:
        # LLMの応答を取得
        response = get_llm_response(user_input, expert_type)

        # 応答を表示
        st.markdown("### 回答:")
        st.write(response)
    else:
        st.warning("送信する前に質問を入力してください。")