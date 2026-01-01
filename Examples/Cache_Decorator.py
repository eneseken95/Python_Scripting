from functools import wraps


def open_web(func):

    cache = {}
            
    def wrapper(*args, **kwargs):
        if len(args) == 1 and not kwargs:
            key = args[0]

        elif len(kwargs) == 1 and not args:
            key = list(kwargs.values())[0]
        else:
            key = (args, tuple(sorted(kwargs.items())))

        try:
            hash(key)

        except:
            key = str(key)

        if key in cache:
            return cache[key]

        result = func(*args, **kwargs)
        cache[key] = result
        return result

    wrapper.cache = cache
    return wrapper


if __name__ == "__main__":
    call_count = 0

    @open_web
    def fetch(url):
        global call_count
        call_count += 1
        return f"Data: {url}"

    print("=" * 50)
    print("CACHE DECORATOR TEST")
    print("=" * 50)

    print("=" * 50)
    print("CACHE DECORATOR TEST")
    print("=" * 50)

    print("\n1. Call: fetch('https://ktu.edu.tr')")
    print(fetch("https://ktu.edu.tr"))
    print(f"Call count: {call_count}", fetch.cache)

    print("\n2. Call: fetch('https://ktu.edu.tr') - Same URL")
    print(fetch("https://ktu.edu.tr"))
    print(f"Call count: {call_count}")

    print("\n3. Call: fetch('https://ktu.edu.tr/comp')")
    print(fetch("https://ktu.edu.tr/comp"))
    print(f"Call count: {call_count}")

    print("\n4. Call: fetch('https://ktu.edu.tr/comp') - Same URL")
    print(fetch("https://ktu.edu.tr/comp"))
    print(f"Call count: {call_count}")

    print("\n" + "=" * 50)
    print(f"RESULT: Function ran only {call_count} times!")
    print(f"But total 4 calls were made.")
    print(f"Cache prevented {4 - call_count} unnecessary executions!")
    print("=" * 50)
