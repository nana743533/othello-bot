#!/usr/bin/env python3
"""
オセロボット - Codingame用
シンプルな戦略：左上の有効な手を選ぶ
"""

import sys

def main():
    # 初回入力（プレイヤーIDと盤面サイズ）
    player_id = int(input())
    board_size = int(input())

    turn = 1

    while True:
        turn += 1

        # 毎ターン、盤面を読み込む
        board = []
        for _ in range(board_size):
            line = input().strip()
            board.append(line)

        # EXPERTモード時：相手の手履歴
        if turn > 2:
            last_moves = input()

        # 有効な手の数
        action_count = int(input())

        # 有効な手の座標を読み込み
        actions = []
        for _ in range(action_count):
            action = input().strip()
            actions.append(action)

        # 手を選択（例: 左上の有効な手）
        if actions:
            best_move = actions[0]
            print(f"{best_move} MSG 何でもできるよ")
        else:
            # パス（有効な手がない場合）
            print("MSG パス...")

if __name__ == "__main__":
    main()
