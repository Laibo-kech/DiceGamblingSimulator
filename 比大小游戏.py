# Developer：shiwenxiang
# Time:2023/4/16 22:10
import random

def main():
    print("欢迎来到比大小游戏！本游戏创作者为石文祥")

    player_balance = 10000

    while True:
        print(f"\n您当前的本金为：{player_balance}元")

        if player_balance < 500:
            print("您的本金不足，无法继续游戏。")
            break

        bet = int(input("请输入您的赌注（500-10000）："))

        if bet < 500 or bet > 10000:
            print("无效的赌注，请输入500到10000之间的整数。")
            continue
        elif bet > player_balance:
            print("您的赌注超过了您的本金，请重新输入。")
            continue

        player_choice = input("请输入您的选择（大、小）或者输入'退出'来结束游戏：")
        if player_choice == "退出":
            print("感谢您的参与，再见！")
            break

        computer_number = random.randint(1, 6)
        player_number = random.randint(1, 6)

        print(f"您掷出了：{player_number}，电脑掷出了：{computer_number}")

        if player_choice == "大":
            if player_number > computer_number:
                print("恭喜您，您赢了！")
                player_balance += bet
            elif player_number < computer_number:
                print("很遗憾，您输了。")
                player_balance -= bet
            else:
                print("平局！")
        elif player_choice == "小":
            if player_number < computer_number:
                print("恭喜您，您赢了！")
                player_balance += bet
            elif player_number > computer_number:
                print("很遗憾，您输了。")
                player_balance -= bet
            else:
                print("平局！")
        else:
            print("无效输入，请重新输入。")

if __name__ == "__main__":
    main()
