total_price = 1000000
lower_price = total_price * 0.2
higher_price = total_price * 0.1

buyer_has_good_credit = True
buyer_has_bad_credit = True

if buyer_has_good_credit:
    print(lower_price)
elif buyer_has_bad_credit:
    print(higher_price)
else:
    print('What am I doing with my life')
