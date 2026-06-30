while True:

    pw = input("Enter a strong password: ")

    strength_score = 0

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Check length
    if len(pw) >= 8:
        strength_score += 1
    else:
        print("Password should contain at least 8 characters.")
        continue

    # Check each character
    for ch in pw:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True

    # Increase score
    if has_upper:
        strength_score += 1

    if has_lower:
        strength_score += 1

    if has_digit:
        strength_score += 1

    if has_special:
        strength_score += 1

    # Final result
    if strength_score == 5:
        print("Strong Password.")
        break
    else:
        print("Password must contain:")

        if not has_upper:
            print("- At least one uppercase letter")

        if not has_lower:
            print("- At least one lowercase letter")

        if not has_digit:
            print("- At least one digit")

        if not has_special:
            print("- At least one special character")

        print("Please try again.\n")