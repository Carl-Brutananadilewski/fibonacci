def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lambda_handler(event, context):
    try:
        event
    except ValueError:
        print("Please specify number for Fibonacci sequence")
    if event < 1:
        print("Number must be positive")
    else:
        return fibonacci(event)

if __name__ == "__main__":
    event = {"number":7}
    context = {}
    print(lambda_handler(event, context))
