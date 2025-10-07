# Tính trừu tượng
# Sử dụng module abc, tạo một lớp trừu tượng PaymentGateway
from abc import ABC, abstractmethod

# Trong lớp này, định nghĩa một phương thức trừu tượng là process_payment(self, amount)
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Tạo lớp con MomoPayment(PaymentGateway):
# Triển khai phương thức process_payment(self, amount) để in ra: "Đang xử lý thanh toán Momo số tiền [số tiền]... Vui lòng quét mã QR."
class MomoPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Đang xử lý thanh toán Momo số tiền {amount}... Vui lòng quét mã QR.")


# Tạo lớp con CreditCardPayment(PaymentGateway):
# Triển khai phương thức process_payment(self, amount) để in ra: "Đang xử lý thanh toán thẻ tín dụng số tiền [số tiền]... Vui lòng nhập thông tin thẻ."
class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Đang xử lý thanh toán thẻ tín dụng số tiền {amount}... Vui lòng nhập thông tin thẻ.")   
        
# Tạo các đối tượng và gọi phương thức process_payment với số tiền mẫu
momo = MomoPayment()
momo.process_payment(500000)
credit_card = CreditCardPayment()
credit_card.process_payment(1200000)

