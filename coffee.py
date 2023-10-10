def coffee_machine():
    amount_due = 50
    total_payment = 0
    print(f"Нужная сумма: {amount_due - total_payment}")
    while total_payment < amount_due:
        coin = int(input("Вставьте монету: "))
        if coin not in [50, 20, 10, 5]:
            print(f"Нужная сумма: {amount_due - total_payment}")
            continue
        total_payment += coin
       ## print(f"Нужная сумма: {amount_due - total_payment}")
    change_owed = total_payment - amount_due
    print(f"Ваша сдача: {change_owed}")
coffee_machine()