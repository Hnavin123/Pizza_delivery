from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
# from sqlalchemy_utils.types import ChoiceType 
from sqlalchemy_utils import ChoiceType
# from sqlalchemy.utils.types.choice import ChoiceType

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(256), unique=True)
    email = Column(String(256), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders=relationship('Order', back_populates='user')
    
    
    def __repr__(self):
        return f"<User{self.username}>"
    
class Order(Base):
    ORDER_STATUS = (
            ('PENDING', 'Pending'),
            ('IN-TRANSIT', 'In-Transit'),
            ('DELIVERED', 'Delivered'),
        )
        
    PIZZA_SIZES = (
            ('SMALL', 'Small'),
            ('MEDIUM', 'Medium'),
            ('LARGE', 'Large'),
            ('EXTRA-LARGE', 'Extra-Large'),
        )   
        
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=True)
    order_status = Column(ChoiceType(ORDER_STATUS), default='PENDING')
    pizza_sizes = Column(ChoiceType(PIZZA_SIZES), default='SMALL')
    user_id = Column(Integer, ForeignKey('users.id'))
    user=relationship('User', back_populates='orders')
        
    def __repr__(self):
        return f"<Order {self.id}>"
        
        
        
    
    
    
    
    
    