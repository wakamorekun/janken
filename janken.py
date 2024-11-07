import random
cpu = random.randint(1, 3)
janken = int(input(f"1.グー\n2.チョキ\n3.パー\nあなたの手を選択してください。>"))


print(f"あなたの手：{janken}\nコンピュータの手：{cpu}")

if janken == cpu:
    print("<><><><><><><><><><><>\n引き分けです!\n<><><><><><><><><><><>")
elif(janken == 1 and cpu == 2) or (janken == 2 and cpu == 3) or (janken == 3 and cpu == 1):
    print("<><><><><><><><><><><>\nあなたの勝ちです！\n<><><><><><><><><><><>")
    you_win += 1
else:
    print("<><><><><><><><><><><>\nコンピュータの勝ちです！\n<><><><><><><><><><><>")
    cpu_win += 1