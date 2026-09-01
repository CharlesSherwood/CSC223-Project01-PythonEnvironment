from Rectangle import Rectangle

def main():
    box = Rectangle(5.0, 3.0)

    print("Valid Rectangle")
    print(f"Length:{box.get_length()}")
    print(f"width:{box.get_width()}")
    print(f"area:{box.get_area()}")

    invalid_box = Rectangle(-4.0, 6.0)
   
    print()
    print("Invalid Rectangle")
    print(f"Length: {invalid_box.get_length()}")
    print(f"width: {invalid_box.get_width()}")
    print(f"area: {invalid_box.get_area()}")

if __name__ =="__main__":
    main()