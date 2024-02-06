class BouncyBall:

 def __init__(self, price, size, brand):
   self.price = price 
   self._size = size 
   self._brand = brand

 @property
 def price(self):
   return self._price
   
 @price.setter
 def price(self, new_price):
   if isinstance(new_price, float):
     print("setter activated")
     self._price = new_price
   else:
     print("Please enter a valid price.")

ball = BouncyBall("öo", "c", 2)
print(ball.price)
print(ball._size)
print(ball._brand)