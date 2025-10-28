def main():
    a, b, c = map(int, input().split())
    num = a * 4 + b * 2 + c * 1
    if num == 1 or num == 2 or num == 4:
        print("Yes! Ship Unlocked.")
    else:
        print("No! Better luck next time.")

if __name__ == "__main__":
    main()
