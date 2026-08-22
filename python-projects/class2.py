class Message:
    def __init__(self, sender_name, receiver_name, message_content, date_sent):
        self.sender_name= sender_name
        self.receiver_name= receiver_name
        self.message_content=message_content
        self.date_sent=date_sent
first_message=Message('Sondos', 'Ahmed', 'Hello, How are you?', '2023-06-01')
print(f'The first message is :\n Sender: {first_message.sender_name}\n Receiver: {first_message.receiver_name}\n Content: {first_message.message_content}\n Date Sent: {first_message.date_sent}')
second_message=Message('Ahmed', 'Sondos', 'I am fine, thank you!', '2023-06-02')
print(f'The second message is :\n{second_message.sender_name}\n Receiver: {second_message.receiver_name}\n Content: {second_message.message_content}\n Date Sent: {second_message.date_sent}')
third_message=Message('Sondos', 'Ahmed', 'Great to hear that!', '2023-06-03')
print(f'The third message is :\n{third_message.sender_name}\n Receiver: {third_message.receiver_name}\n Content: {third_message.message_content}\n Date Sent: {third_message.date_sent}')

class Product:
    def __init__(self, name, price, discription, quality):
        self.name= name
        self.price= price
        self.discription= discription
        self.quality= quality
first_product=Product('Laptop', 1000, 'A high-performance laptop', 'Excellent')
print(f'The first product is:\n{first_product.name}\n Price:{first_product.price}\n discription:{first_product.discription}\n Quality:{first_product.quality}')
second_product=Product('Smartphone', 500, 'A feature-rich smartphone', 'Good')
print(f'The second product is:\n{second_product.name}\n Price:{second_product.price}\n discription:{second_product.discription}\n Quality:{second_product.quality}')
third_product=Product('Headphones', 100, 'Noise-cancelling headphones', 'very Good')
print(f'The third product is:\n{third_product.name}\n Price:{third_product.price}\n discription:{third_product.discription}\n Quality:{third_product.quality}')