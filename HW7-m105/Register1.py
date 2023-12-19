import re

def check_registration_rules(username, password, phone_number, mobile_number):
    def validate_username(username):
        # Username validation - Example: Should have at least 4 alphanumeric characters
        return re.match(r"^[a-zA-Z0-9]{4,}$", username)

    def validate_password(password):
        # Password validation - Example: Should have at least 8 characters with at least one uppercase, one lowercase, one digit, and one special character
        return re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()-_=+[\]{}|;:',.<>/?`~])[\S]{8,}$", password)

    def validate_phone_number(phone_number):
        # Phone number validation - Example: Should be 11 digits and start with '09'
        return re.match(r"^09[0-9]{9}$", phone_number) is not None

    def validate_mobile_number(mobile_number):
        # Mobile number validation - Example: Should be 11 digits and start with '02'
        return re.match(r"^02[0-9]{8,}$", mobile_number) is not None

    # Validate each parameter using the corresponding validation function
    username_valid = validate_username(username)
    password_valid = validate_password(password)
    phone_number_valid = validate_phone_number(phone_number)
    mobile_number_valid = validate_mobile_number(mobile_number)

    # Return a dictionary indicating the validation results
    return {
        'username_valid': username_valid,
        'password_valid': password_valid,
        'phone_number_valid': phone_number_valid,
        'mobile_number_valid': mobile_number_valid
    }

def filter_users(users):
    # Filter users based on specified formats
    valid_users = []
    for user in users:
        # Check registration rules for each user
        validation_results = check_registration_rules(
            user['username'],
            user['password'],
            user['phone_number'],
            user['mobile_number']
        )

        # Check if all validation results are True
        if all(validation_results.values()):
            valid_users.append(user)
    return valid_users

# List of users (username, password, phone number, mobile number)
users_list = [
    {'username': 'Amir', 'password': 'Amir@123', 'phone_number': '09123456789', 'mobile_number': '02332501411'},
    {'username': 'user', 'password': 'vaLiad_pas1', 'phone_number': '09123456789', 'mobile_number': '02332501411'},
    {'username': 'valid_user', 'password': 'vaLiad_pas1', 'phone_number': '09123456789', 'mobile_number': '02332501411'},
    {'username': 'validuser', 'password': 'vaLiad_pas1', 'phone_number': '09123456789', 'mobile_number': '02332501411'}
]

# Filter and display valid users
valid_users = filter_users(users_list)
for user in valid_users:
    print("Valid User:")
    print("Username:", user['username'])
    print("Password:", user['password'])
    print("Phone Number:", user['phone_number'])
    print("Mobile Number:", user['mobile_number'])
    print("-------------------------")
