import functools
import datetime

class LogToFileDecorator:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # ثبت زمان فراخوانی تابع
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # باز کردن یا ایجاد فایل برای نوشتن لاگ
            with open(self.log_file_path, 'a') as log_file:
                log_file.write(f"Function '{func.__name__}' called at {timestamp}\n")

            # فراخوانی تابع اصلی و بازگرداندن نتیجه
            result = func(*args, **kwargs)

            return result

        return wrapper

# مثال استفاده از کلاس دکوراتور
log_decorator = LogToFileDecorator('function_calls.log')

@log_decorator
def my_function():
    print("Executing my_function")

# فراخوانی تابع دارای دکوراتور
my_function()
