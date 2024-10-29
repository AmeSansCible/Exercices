def calculate_total(jar):
    sum = 0 #On part de 0 dans notre jar
    for amount in jar:
        sum += amount
    return sum


# Example usage:
jar_of_money = [10, 20, 5, 15, 25]
total_amount = calculate_total(jar_of_money)

print(f"The total amount of money in the jar is: {total_amount}")
