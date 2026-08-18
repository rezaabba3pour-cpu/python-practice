# پاسخ سؤال ۱۰ — فروشگاه اینترنتی با چند نوع تخفیف

initial_amount = float(input("مبلغ سفارش را وارد کنید: "))
customer_type = input("نوع مشتری را وارد کنید (عادی/ویژه): ")
payment_method = input("روش پرداخت را وارد کنید (آنلاین/حضوری): ")
discount_code = input("کد تخفیف را وارد کنید: ")

# بررسی معتبر بودن مبلغ سفارش
if initial_amount < 0:
    print("مبلغ سفارش نامعتبر است.")

# بررسی معتبر بودن نوع مشتری
elif customer_type != "عادی" and customer_type != "ویژه":
    print("نوع مشتری نامعتبر است.")

# بررسی معتبر بودن روش پرداخت
elif payment_method != "آنلاین" and payment_method != "حضوری":
    print("روش پرداخت نامعتبر است.")

else:
    # مقدار اولیه تخفیف عضویت
    membership_discount = 0

    # محاسبه تخفیف مشتری ویژه
    if customer_type == "ویژه":
        if initial_amount > 3000000:
            membership_discount = initial_amount * 20 / 100

        elif initial_amount >= 1500000:
            membership_discount = initial_amount * 10 / 100

    # محاسبه تخفیف مشتری عادی
    else:
        if initial_amount > 3000000:
            membership_discount = initial_amount * 5 / 100

    amount_after_membership = initial_amount - membership_discount

    # محاسبه تخفیف کد PYTHON
    if discount_code == "PYTHON":
        code_discount = amount_after_membership * 5 / 100
    else:
        code_discount = 0

    amount_after_code = amount_after_membership - code_discount

    # محاسبه تخفیف پرداخت آنلاین
    if payment_method == "آنلاین":
        online_discount = amount_after_code * 2 / 100
    else:
        online_discount = 0

    amount_after_discounts = amount_after_code - online_discount

    # محاسبه هزینه ارسال بر اساس مبلغ اولیه سفارش
    if initial_amount > 2000000:
        shipping_cost = 0
    else:
        shipping_cost = 120000

    # محاسبه مجموع تخفیف‌ها و مبلغ نهایی
    total_discount = membership_discount + code_discount + online_discount
    final_amount = amount_after_discounts + shipping_cost

    print("مبلغ اولیه:", initial_amount)
    print("مجموع تخفیف:", total_discount)
    print("هزینه ارسال:", shipping_cost)
    print("مبلغ نهایی قابل پرداخت:", final_amount)
