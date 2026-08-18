# پاسخ سؤال ۹ — محاسبه حقوق کارمند

work_hours = float(input("تعداد ساعت کار ماهانه را وارد کنید: "))
hourly_rate = float(input("نرخ دستمزد هر ساعت را وارد کنید: "))
shift = input("نوع شیفت را وارد کنید (روز/شب): ")

# بررسی تعداد ساعت کار
if work_hours < 0:
    print("تعداد ساعت کار نامعتبر است.")

# بررسی نرخ دستمزد
elif hourly_rate < 0:
    print("نرخ دستمزد نامعتبر است.")

# بررسی نوع شیفت
elif shift != "روز" and shift != "شب":
    print("نوع شیفت نامعتبر است.")

else:
    # محاسبه حقوق تا ۱۶۰ ساعت
    if work_hours <= 160:
        salary = work_hours * hourly_rate

    # محاسبه حقوق با اضافه‌کاری
    else:
        normal_salary = 160 * hourly_rate
        overtime_hours = work_hours - 160
        overtime_salary = overtime_hours * hourly_rate * 1.5
        salary = normal_salary + overtime_salary

    # محاسبه فوق‌العاده شیفت شب
    if shift == "شب":
        shift_bonus = salary * 20 / 100
    else:
        shift_bonus = 0

    salary_after_bonus = salary + shift_bonus

    # محاسبه مالیات
    if salary_after_bonus > 30000000:
        tax = salary_after_bonus * 10 / 100
    else:
        tax = 0

    final_salary = salary_after_bonus - tax

    print("حقوق قبل از فوق‌العاده:", salary)
    print("فوق‌العاده شیفت:", shift_bonus)
    print("مالیات:", tax)
    print("حقوق نهایی:", final_salary)
