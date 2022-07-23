# 題目
# 人類和其他哺乳動物的雄性配子或精子細胞是異配子，包含兩種性染色體中的一種。它們是 X 或 Y。然而，雌配子或卵只包含 X 性染色體並且是同配子。
# 在這種情況下，精子細胞決定了個體的性別。如果含有 X 染色體的精子細胞使卵子受精，則產生的受精卵將是 XX 或雌性。如果精子細胞含有 Y 染色體，那麼產生的受精卵將是 XY 或男性。
# 根據男性精子中存在的 X 或 Y 染色體確定後代的性別是男性還是女性。
# 如果精子中包含 X 染色體，則返回“恭喜！您將有一個女兒。”；如果精子中含有 Y 染色體，則返回“恭喜！你將有一個兒子。”；


def chromosome_check(sperm):
    #Your code here
    if sperm == 'XY':
        return 'Congratulations! You\'re going to have a son.'
    else:
        return 'Congratulations! You\'re going to have a daughter.'