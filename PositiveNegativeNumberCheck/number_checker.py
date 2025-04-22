import logging

# configure logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class NumberChecker:
    """
    A class to check whether a number is positive, negative or zero.
    """
    
    def __init__(self, number: float):
        """
        Initialize the NumberChecker with number

        Args:
            number (float): The number to check.
        """
        self.number = number
    
    def check(self) -> str:
        """
        Determine if the number is positive,negative or zero

        Returns:
            str: A string message indicating the number type
        """
        if self.number > 0:
            return "The number is positive."
        elif self.number < 0:
            return "The number is negative."
        else:
            return "The number is zero."
        
def main() -> None:
    """
    Main function to handle user input and perform the number check.
    """
    try:
        user_input = input("Enter a number: ").strip()
        number = float(user_input)
        checker = NumberChecker(number)
        result = checker.check()
        logging.info(result)
    except ValueError:
        logging.error("Invalid input. Please enter a valid number.")
        
if __name__ == "__main__":
    main()