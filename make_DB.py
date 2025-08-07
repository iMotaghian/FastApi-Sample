from sqlalchemy import create_engine,Column,Integer,String,Boolean
from sqlalchemy.orm import sessionmaker, declarative_base,relationship

SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"
# SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

# for postgres or other relational databases
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver:5432/db"
# SQLALCHEMY_DATABASE_URL = "mysql://username:password@localhost/db_name"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False  # only for sqlite
                  }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# create base class for declaring tables
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(30))
    last_name = Column(String(30),nullable=True)
    age = Column(Integer)
    # email = Column(String())
    # password = Column(String())
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)

    def __repr__(self):
        return f"User(id={self.id},name={self.last_name},age={self.age})"

# example

'''
class UserType(PythonEnum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

class SampleModel(Base):
    __tablename__ = "sample_model"

    id = Column(Integer, primary_key=True)
    uuid_field = Column(UUID)
    string_field = Column(String(100))
    text_field = Column(Text)
    boolean_field = Column(Boolean)
    integer_field = Column(Integer)
    float_field = Column(Float)
    numeric_field = Column(Numeric(10, 2)) # lke float
    date_field = Column(Date)
    datetime_field = Column(DateTime)
    time_field = Column(Time)
    interval_field = Column(Interval) # time 1970 ...
    enum_field = Column(Enum(UserType)) # Enum (select filed)
    array_field = Column(ARRAY(Integer)) # [1,3,4,5,6,6]
    json_field = Column(JSON) # dict
    foreign_key_field = Column(Integer, ForeignKey('related_table.id')) #ForeignKey
    binary_field = Column(LargeBinary)
'''
# need to create table
Base.metadata.create_all(engine)

session = SessionLocal()

# add one data
mehrdad = User(first_name="mehrdad",age=36)
session.add(mehrdad)
session.commit()

# add bulk data
naeim = User(first_name="naeim",age=36)
hami = User(first_name="hami",age=1)
new_users = [naeim,hami]
session.add_all(new_users)
session.commit()

# retrieve data / GET DATA
users = session.query(User).all() # GET ALL

# get data with filter
user_mehr = session.query(User).filter_by(first_name="mehrdad",age=36).all()
user_first = session.query(User).filter_by(age=36).first()
user_none = session.query(User).filter_by(first_name="mehrdad",age=36).one_or_none()

# update data
user_none.last_name = "motaghian"
session.commit()

# delete
if user_none:
    session.delete(user_none)
    session.commit()
    
    
# Assume 'session' is a configured SQLAlchemy Session and 'User' is an ORM model.
users_all = session.query(User).all()

# query all users with age greater than or equal to 25
users_filtered = session.query(User).filter(User.age >= 25).all()

print("ALL Users: ", len(users_all))
print("Filtered Users: ", len(users_filtered))

# add multiple filters
# query all users with age greater than or equal to 25 and name equals to something
users_filtered = session.query(User).filter(User.age >= 25, User.first_name == "ali").all()

# or you can use where
users_filtered = session.query(User).where(User.age >= 25, User.first_name == "ali").all()

# users with similar name containing specific substrings
users_similar_name = session.query(User).filter(User.first_name.like("%ali%")).all()

# users with case insensitive match
users_similar_name = session.query(User).filter(User.first_name.ilike("%ali%")).all()

# users with starting and ending chars
users_starting_ali = session.query(User).filter(User.first_name.like("Ali%")).all()
users_ending_ali = session.query(User).filter(User.first_name.like("%Ali")).all()


from sqlalchemy import or_, and_, not_

# Assume 'session' is a configured SQLAlchemy Session and 'User' is an ORM model.

# query those who has ali as name or age above 25
users_filtered = session.query(User).filter(or_(User.age >= 25, User.first_name == "ali")).all()

# query those who has ali as name and age above 25
users_filtered = session.query(User).filter(and_(User.age >= 25, User.first_name == "ali")).all()

# query those who name is not ali
users_filtered = session.query(User).filter(not_(User.first_name == "ali")).all()

# getting users which are not named ali or age between 35,60
users = session.query(User).filter(or_(not_(User.first_name == "ali"), and_(User.age > 35, User.age < 60)))


from sqlalchemy import func

# 1. Count Total Users
total_users = session.query(func.count(User.id)).scalar()
print("Total Users:", total_users)  # Total Users: 6

# 2. Find the Average Age of Users
average_age = session.query(func.avg(User.age)).scalar()
print("Average Age:", average_age)  # Average Age: 32.833333333333336

# 3. Find the Maximum and Minimum Age
max_age = session.query(func.max(User.age)).scalar()
min_age = session.query(func.min(User.age)).scalar()
print(f"Max Age: {max_age}, Min Age: {min_age}")  # Max Age: 45, Min Age: 22

# 4. Find the Total Number of Orders
total_orders = session.query(func.count(Order.id)).scalar()
print("Total Orders:", total_orders)  # Total Orders: 7

# 5. Find the Sum of All Order Amounts
total_revenue = session.query(func.sum(Order.total_amount)).scalar()
print("Total Revenue:", total_revenue)  # Total Revenue: 987.00

# 6. Find the Average Order Value
average_order_value = session.query(func.avg(Order.total_amount)).scalar()
print("Average Order Value:", average_order_value)  # Average Order Value: 141.0

# 7. Find Users Who Have Placed the Most Orders
most_active_users = session.query(
    User.name,
    func.count(Order.id).label("order_count")
).join(Order).group_by(User.id).order_by(func.count(Order.id).desc()).limit(5).all()
print("Top 5 Active Users by Order Count:", most_active_users)  # Top 5 Active Users by Order Count: [('Ali', 3), ('Sara', 2), ('Reza', 1), ('Maryam', 1)]

# 8. Find Users with the Highest Total Spending
top_spenders = session.query(
    User.name,
    func.sum(Order.total_amount).label("total_spent")
).join(Order).group_by(User.id).order_by(func.sum(Order.total_amount).desc()).limit(5).all()
print("Top 5 Users by Spending:", top_spenders)  # Top 5 Users by Spending: [('Ali', 320.75), ('Reza', 300.00), ('Sara', 290.50), ('Maryam', 75.75)]

# 9. Find Users Who Have Not Placed Any Orders
users_without_orders = session.query(User).outerjoin(Order).filter(Order.id == None).all()
print("Users Without Orders:", [user.name for user in users_without_orders])  # Users Without Orders: ['Nima', 'Zahra']

# 10. Find the Most Recent Order Date
latest_order_date = session.query(func.max(Order.created_at)).scalar()
print("Most Recent Order Date:", latest_order_date)  # Most Recent Order Date: 2025-08-07 16:00:00

# Close the session
session.close()

#######################################################################

from sqlalchemy import text

# Assume 'session' is a configured SQLAlchemy Session.

# Example 1: Count Users with a Specific Condition (Raw SQL)
query = text("SELECT COUNT(*) FROM user WHERE age >= :min_age")
result = session.execute(query, {"min_age": 25}).scalar()
print("Users with age >= 25:", result)

# Example 2: Find the Average Age of Users (Raw SQL)
query = text("SELECT AVG(age) FROM user")
result = session.execute(query).scalar()
print("Average Age of Users:", result)

# Example 3: Get Users with a Specific Name (Raw SQL)
query = text("SELECT * FROM user WHERE name = :name")
result = session.execute(query, {"name": "Ali"}).fetchall()
print("Users named Ali:", [user.name for user in result])

# Example 4: Aggregate Query for the Total Revenue (Raw SQL)
query = text("SELECT SUM(total_amount) FROM \"order\"")
result = session.execute(query).scalar()
print("Total Revenue:", result)