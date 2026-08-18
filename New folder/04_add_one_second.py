# پاسخ سؤال ۴ — اعتبارسنجی زمان و اضافه کردن یک ثانیه

hour = int(input("ساعت را وارد کنید: "))
minute = int(input("دقیقه را وارد کنید: "))
second = int(input("ثانیه را وارد کنید: "))

# بررسی معتبر بودن ساعت
if hour < 0 or hour > 23:
    print("ساعت نامعتبر است.")

# بررسی معتبر بودن دقیقه
elif minute < 0 or minute > 59:
    print("دقیقه نامعتبر است.")

# بررسی معتبر بودن ثانیه
elif second < 0 or second > 59:
    print("ثانیه نامعتبر است.")

else:
    # یک ثانیه به زمان اضافه می‌شود
    second = second + 1

    # اگر ثانیه به ۶۰ برسد، دقیقه افزایش پیدا می‌کند
    if second == 60:
        second = 0
        minute = minute + 1

        # اگر دقیقه به ۶۰ برسد، ساعت افزایش پیدا می‌کند
        if minute == 60:
            minute = 0
            hour = hour + 1

            # بعد از ۲۳:۵۹:۵۹ زمان به ۰۰:۰۰:۰۰ برمی‌گردد
            if hour == 24:
                hour = 0

    print(hour, ":", minute, ":", second)
