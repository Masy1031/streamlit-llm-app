import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

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
        "世界史": "あなたは世界史の専門家です。",
        "物理学": "あなたは物理学を専門とする科学者です。",
        "国際料理": "あなたは国際料理の専門家であるプロのシェフです。"
    }

    # デバッグ用の出力を追加
    st.write(f":wrench: Debug: 選択されたキー = {expert_type}")

    system_message = expert_prompts.get(expert_type, "あなたは役に立つアシスタントです。")
    st.info(f":robot_face: 現在のシステム設定: {system_message}")

    # LLMを初期化
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    # LLMに渡すメッセージを作成
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text),
    ]

    # LLMからの結果を取得（新しいinvokeメソッドを使用）
    result = llm.invoke(messages)
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

# 専門家の種類を選択するためのラジオボタン（日本語に変更）
expert_type = st.radio(
    "専門家の種類を選択してください:",
    ("世界史", "物理学", "国際料理")
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