# Othello Bot for Codingame

[Codingame Othello](https://www.codingame.com/multiplayer/bot-programming/othello-1) 対戦用ボットです。

**入力・出力フォーマットは [MultiStruct/Othello](https://github.com/MultiStruct/Othello) を参考にしています。**

## 入力フォーマット

```
# ターン1
0          # プレイヤーID (0 or 1)
8          # 盤面サイズ
........   # 盤面1行目 (.=空白, 0=黒, 1=白)
........
...01...
...10...
........
........
........
6          # 有効な手の数
c3
c4
d2
e2
f4
f5

# ターン2以降
...01...   # 盤面状態
...10...
...011..
......
c3;        # 相手の手履歴（EXPERTモード時のみ）
4          # 有効な手の数
c2
d1
e1
f3
```

## 出力フォーマット

```
EXPERT c3 MSG メッセージ
```

- `EXPERT`: 付けると相手の手履歴が受け取れる（省略可）
- `座標`: 有効な手（例: c3, d5）
- `MSG`: 表示メッセージ（省略可）

## 実行方法

```bash
python Answer.py
```

## 戦略

- `Answer.py`: シンプル（左上の手を選択）
- `Answer2.py`: 角・辺を優先する戦略
