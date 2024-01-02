# streamlit-ai-app


- submit buttonを置かない場合は, 2行目を削除すると" press enter to apply" みたいなのがデフォルトで表示される

```
 user_input = st.text_area(label='Message: ', key='input', height=100)
 submit_button = st.form_submit_button(label='Send')
```

- 利用可能なmodelは以下のコードで確認する. (表示件数が多いので任意のファイルに保存すると良い)
https://platform.openai.com/docs/api-reference/introduction


```
curl https://api.openai.com/v1/models \\n  -H "Authorization: Bearer $OPENAI_API_KEY" > test.txt
```

- tweepy exceptions
https://docs.tweepy.org/en/stable/exceptions.html
