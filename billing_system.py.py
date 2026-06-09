# SUPERMARKET BILLING SYSTEM
# Complete working solution for SmartBuy Supermarket

def display_receipt(products, grand_total, discount, final_amount):
    """Display a well-formatted receipt"""
    print("\n" + "=" * 45)
    print("         SMARTBUY SUPERMARKET")
    print("              RECEIPT")
    print("=" * 45)
    print(f"{'Item':<20} {'Qty':<6} {'Price':<10} {'Total':<10}")
    print("-" * 45)
    
    # Loop through all products and print each row
    for item in products:
        name = item[0]
        qty = item[1]
        price = item[2]
        line_total = item[3]
        print(f"{name:<20} {qty:<6} Le {price:<8.2f} Le {line_total:<8.2f}")
        print("-" * 45)
    print(f"{'Subtotal:':>35} Le {grand_total:.2f}")
    
    # Show discount if applied
    if discount > 0:
        print(f"{'Discount (10%):':>35} Le {discount:.2f}")
    
    print(f"{'FINAL TOTAL:':>35} Le {final_amount:.2f}")
    print("=" * 45)
    print("      Thank you for shopping with us!")
    print("=" * 45 + "\n")


def main():
    """Main program loop for multiple customers"""
    print("\n" + "=" * 45)
    print("  WELCOME TO SMARTBUY BILLING SYSTEM")
    print("=" * 45)
    
    continue_program = True
    while continue_program:
        # List to store products for current customer
        products = []
        grand_total = 0.0
        
        print("\n--- Enter Products for this Customer ---")
        more_items = True
        
        # Input products for current customer
        while more_items:
            print()
            product_name = input("Enter product name: ")
            
            # Input quantity with validation
            while True:
                    quantity = int(input("Enter quantity: "))
                    if quantity > 0:
                        break
                    else:
                        print("Quantity must be positive. Try again.")
                    print("Invalid input. Please enter a whole number.")
            
            # Input price with validation
            while True:
                try:
                    price = float(input("Enter price per unit (Le): "))
                    if price > 0:
                        break
                    else:
                        print("Price must be positive. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            
            # Calculate line total
            line_total = quantity * price
            grand_total += line_total
            
            # Store product as a list
            products.append([product_name, quantity, price, line_total])
# Ask if more items
            while True:
                choice = input("\nAdd another product? (y/n): ").lower()
                if choice == 'y' or choice == 'n':
                    break
                print("Please enter 'y' or 'n'")
            
            if choice == 'n':
                more_items = False
        
        # Calculate discount (10% if total > 500)
        if grand_total > 500:
            discount = grand_total * 0.10
            final_amount = grand_total - discount
        else:
            discount = 0
            final_amount = grand_total
            # Display receipt
        display_receipt(products, grand_total, discount, final_amount)
        
        # Ask if cashier wants to process another customer
        while True:
            next_customer = input("Process next customer? (y/n): ").lower()
            if next_customer == 'y' or next_customer == 'n':
                break
            print("Please enter 'y' or 'n'")
        
        if next_customer == 'n':
            continue_program = False
    
    print("\n" + "=" * 45)
    print("  Thank you for using SmartBuy System!")
    print("  Goodbye!")
    print("=" * 45)
# Run the program
# Run the program
if __name__ == "__main__":
    main()