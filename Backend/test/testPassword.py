from passlib.context import CryptContext

# Create password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash the password
password = "sparsh1200#"
hashed_password = pwd_context.hash(password)
print(hashed_password)