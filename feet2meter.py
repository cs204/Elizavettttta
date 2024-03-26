def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
    numeric_part = v.replace('ft', '')
    feet_value = float(numeric_part)
    meters = feet_value * 0.3048
    return meters

main()
