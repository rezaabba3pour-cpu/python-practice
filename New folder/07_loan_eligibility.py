# پاسخ سؤال ۷ — بررسی شرایط دریافت وام

age = int(input("سن را وارد کنید: "))
monthly_income = float(input("درآمد ماهانه را وارد کنید: "))
current_debt = float(input("مبلغ بدهی فعلی را وارد کنید: "))
returned_check = input("وضعیت سابقه چک برگشتی را وارد کنید (دارد/ندارد): ")

# بررسی معتبر بودن وضعیت چک برگشتی
if returned_check != "دارد" and returned_check != "ندارد":
    print("وضعیت چک برگشتی نامعتبر است.")

# بررسی معتبر بودن مقادیر مالی
elif monthly_income < 0 or current_debt < 0:
    print("مقادیر مالی نامعتبر هستند.")

# بررسی محدوده سنی
elif age < 20 or age > 60:
    print("درخواست وام رد شد؛ سن متقاضی خارج از محدوده مجاز است.")

# بررسی حداقل درآمد
elif monthly_income < 20000000:
    print("درخواست وام رد شد؛ درآمد کمتر از حداقل موردنیاز است.")

# بررسی نسبت بدهی به درآمد
elif current_debt > monthly_income * 3:
    print("درخواست وام رد شد؛ میزان بدهی بیشتر از حد مجاز است.")

# بررسی سابقه چک برگشتی
elif returned_check == "دارد":
    print("درخواست وام رد شد؛ متقاضی سابقه چک برگشتی دارد.")

else:
    # تعیین سطح وام
    if monthly_income > 50000000:
        print("وام سطح A")

    elif monthly_income >= 30000000:
        print("وام سطح B")

    else:
        print("وام سطح C")
