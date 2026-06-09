from abc import ABC, abstractmethod

# PAYMENT INTERFACES (ISP)

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPIPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class WalletPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Wallet")

# NOTIFICATION INTERFACES


class NotificationService(ABC):

    @abstractmethod
    def send_notification(self, message):
        pass


class EmailNotification(NotificationService):

    def send_notification(self, message):
        print(f"Email Sent: {message}")


class SMSNotification(NotificationService):

    def send_notification(self, message):
        print(f"SMS Sent: {message}")


class PushNotification(NotificationService):

    def send_notification(self, message):
        print(f"Push Notification Sent: {message}")


# STORAGE INTERFACES
#

class Storage(ABC):

    @abstractmethod
    def save(self, order):
        pass


class DatabaseStorage(Storage):

    def save(self, order):
        print(f"Order {order.order_id} saved in Database")


class FileStorage(Storage):

    def save(self, order):
        print(f"Order {order.order_id} saved in File")


# ORDER CLASSES


class Order(ABC):

    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

    @abstractmethod
    def get_total(self):
        pass


class RegularOrder(Order):

    def get_total(self):
        return self.amount


class DiscountedOrder(Order):

    def get_total(self):
        return self.amount - (self.amount * 0.10)


class PriorityOrder(Order):

    def get_total(self):
        return self.amount + 100


# ORDER SERVICE (DIP)


class OrderService:

    def __init__(self, payment_method,
                 notification_service,
                 storage_service):

        self.payment_method = payment_method
        self.notification_service = notification_service
        self.storage_service = storage_service

    def place_order(self, order):

        total = order.get_total()

        print(f"\nProcessing Order ID: {order.order_id}")
        print(f"Final Amount: ₹{total}")

        self.payment_method.pay(total)

        self.notification_service.send_notification(
            f"Order {order.order_id} placed successfully"
        )

        self.storage_service.save(order)

        print("Order Completed Successfully")


# MAIN PROGRAM


# Create Order
x=int(input("Enter Order Type (1-Regular, 2-Discounted, 3-Priority): "))
id=int(input("Enter Order ID: "))
amount=int(input("Enter Order Amount: "))
if x==1:
    order1 = RegularOrder(id, amount)
elif x==2:
    order1 = DiscountedOrder(id, amount)
elif x==3:
    order1 = PriorityOrder(id, amount)

# Inject Dependencies
payment = UPIPayment()
notification = EmailNotification()
storage = DatabaseStorage()

# Create Service
service = OrderService(payment,
                       notification,
                       storage)

# Place Order
service.place_order(order1)