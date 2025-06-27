

# 🧾 Restaurant Billing System (Console-Based)

Welcome to the **Restaurant Billing System**, a simple **Python console application** that simulates an order-taking and billing process for a restaurant. This project is perfect for Python beginners who want to learn about dictionaries, loops, conditionals, and string handling.

---

## 💡 Features

* 🧾 Displays menu with prices
* 🔤 Accepts user input (case-insensitive) for orders
* ➕ Adds multiple items to the order
* ❌ Handles unavailable items gracefully
* 💰 Calculates and displays total bill amount

---

## 📋 Sample Menu

```python
menu = {
    'Pizza': 100,
    'Burger': 70,
    'Pasta': 60,
    'Salad': 30,
    'Coffee': 50
}
```

---

## 🖥️ How It Works

1. The user is shown a menu.
2. The user selects one item to start the order.
3. The app asks if they want to add more items.
4. If yes, it keeps asking and updating the bill.
5. If no, it shows the final total.

---

## ▶️ How to Run

1. Clone the repo:

```bash
git clone https://github.com/SyamantakPathak/resturant-billing.git
cd resturant-billing
```

2. Run the Python script:

```bash
python simple_resturant_billing.py
```

> Make sure you have Python 3 installed on your system.

---

## 🧠 Concepts Used

* Python `dictionary` for menu storage
* `input()` for user interaction
* String methods like `.lower()` for case-insensitive comparison
* `while` loop for taking multiple orders
* Basic `if-else` conditionals

---

## 📌 Example Output

```
Hello! Welcome to our Resturant: 
Here all the items from our resturant: 
Pizza  :  100
Burger  :  70
Pasta  :  60
Salad  :  30
Coffee  :  50
Enter the name of item that you want to order !! pizza
your item pizza has been added to your order
Do you want to add another item ? (Yes/No) yes
Enter the next item you want to add !!coffee
the item coffee is added to your order 
Do you want to add another item ? (Yes/No) no
The total amount of item to pay is  150
Thank You !!!
```

---

## 📁 File Structure

```
resturant_billing_/
├── simple_resturant_billing.py        # Main script file
├── README.md      # Project documentation
```

---

## ✍️ Author

**Your Name** – \[https://github.com/SyamantakPathak]

---

## 🪪 License

This project is licensed under the MIT License – feel free to use, modify, and share.

---