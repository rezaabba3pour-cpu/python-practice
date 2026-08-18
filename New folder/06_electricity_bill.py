# پاسخ سؤال ۶ — محاسبه قبض برق پلکانی

consumption = float(input("میزان مصرف برق را بر حسب kWh وارد کنید: "))

# مصرف نمی‌تواند منفی باشد
if consumption < 0:
    print("میزان مصرف نامعتبر است.")

else:
    # محاسبه هزینه برای مصرف تا ۱۰۰ واحد
    if consumption <= 100:
        bill = consumption * 1000

    # محاسبه هزینه برای مصرف بین ۱۰۱ تا ۳۰۰ واحد
    elif consumption <= 300:
        bill = (100 * 1000) + ((consumption - 100) * 1500)

    # محاسبه هزینه برای مصرف بیشتر از ۳۰۰ واحد
    else:
        bill = (100 * 1000) + (200 * 1500) + ((consumption - 300) * 2500)

    # محاسبه مالیات در صورت بیشتر بودن قبض از ۵۰۰٬۰۰۰ تومان
    if bill > 500000:
        tax = bill * 5 / 100
    else:
        tax = 0

    final_bill = bill + tax

    print("مبلغ قبض قبل از مالیات:", bill)
    print("مالیات:", tax)
    print("مبلغ نهایی قبض:", final_bill)
