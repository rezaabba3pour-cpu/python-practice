# پاسخ سؤال ۱ — دستگاه ATM

balance = int(input("موجودی حساب را وارد کنید: "))
withdraw_amount = int(input("مبلغ برداشت را وارد کنید: "))

# بررسی معتبر بودن مبلغ برداشت
if (withdraw_amount <= 0):
    print("مبلغ برداشت باید بیشتر از صفر باشد.")

# بررسی مضرب ۵۰٬۰۰۰ بودن مبلغ
elif (withdraw_amount % 50000 != 0):
    print("مبلغ برداشت باید مضربی از ۵۰٬۰۰۰ تومان باشد.")

# بررسی سقف برداشت
elif (withdraw_amount > 5000000):
    print("مبلغ برداشت بیشتر از سقف مجاز ۵٬۰۰۰٬۰۰۰ تومان است.")

# بررسی کافی بودن موجودی
elif (withdraw_amount > balance):
    print("موجودی حساب کافی نیست.")

else:
    remaining_balance = balance - withdraw_amount

    print("برداشت با موفقیت انجام شد.")
    print("مبلغ برداشت‌شده:", withdraw_amount)
    print("موجودی باقی‌مانده:", remaining_balance)
