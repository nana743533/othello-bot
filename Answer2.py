#!/usr/bin/env python3
"""
オセロボット - 角・辺優先戦略
角を取ることを優先し、次に辺を優先する
"""

import sys

# 角の座標（最優先）
CORNERS = {'a1', 'a8', 'h1', 'h8'}

# 辺の座標（優先）
EDGES = {
    'a2', 'a3', 'a4', 'a5', 'a6', 'a7',
    'b1', 'c1', 'd1', 'e1', 'f1', 'g1',
    'h2', 'h3', 'h4', 'h5', 'h6', 'h7',
    'b8', 'c8', 'd8', 'e8', 'f8', 'g8',
}

# X字（角の隣は危険）
X_SQUARES = {'b2', 'b7', 'g2', 'g7'}


def score_move(move):
    """手のスコアを計算"""
    if move in CORNERS:
        return 100
    elif move in X_SQUARES:
        return -50  # 角の隣は危険
    elif move in EDGES:
        return 10
    else:
        return 0


def main():
    player_id = int(input())
    board_size = int(input())

    turn = 1
    use_expert = True

    while True:
        turn += 1

        # 盤面読み込み
        board = []
        for _ in range(board_size):
            line = input().strip()
            board.append(line)

        # EXPERTモード時：相手の手履歴
        if turn > 2:
            last_moves = input()

        # 有効な手を読み込み
        action_count = int(input())
        actions = []
        for _ in range(action_count):
            action = input().strip()
            actions.append(action)

        # 手を選択
        if actions:
            # スコアでソート
            best_move = max(actions, key=score_move)
            msg = f"スコア:{score_move(best_move)}"
            if use_expert:
                print(f"EXPERT {best_move} MSG {msg}")
            else:
                print(f"{best_move} MSG {msg}")
        else:
            print("MSG パス...")

if __name__ == "__main__":
    main()
