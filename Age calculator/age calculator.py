from datetime import datetime

import jdatetime
from dateutil.relativedelta import relativedelta


def age_calculator(birth_year, birth_month, birth_day):
    """
    Calculate the exact age in years, months, and days based on the given Jalali (Persian) date.

    Parameters:
    - birth_year (int): The birth year in the Jalali calendar.
    - birth_month (int): The birth month in the Jalali calendar.
    - birth_day (int): The birthday in the Jalali calendar.

    Returns:
    - tuple: A tuple containing the age in years, months, and days.

    Raises:
    - ValueError: If the given date is invalid.
    """
    try:
        # Convert the Jalali birthdate to Gregorian
        birth_date_jalali = jdatetime.date(birth_year, birth_month, birth_day)
        birth_date_gregorian = birth_date_jalali.togregorian()

        # Get the current Gregorian date
        today_gregorian = jdatetime.date.today().togregorian()

        # Convert to datetime objects
        birth_date = datetime(birth_date_gregorian.year, birth_date_gregorian.month, birth_date_gregorian.day)
        today_date = datetime(today_gregorian.year, today_gregorian.month, today_gregorian.day)

        # Calculate the difference using relative delta to get the exact years, months, and days
        difference = relativedelta(today_date, birth_date)

        years = difference.years
        months = difference.months
        days = difference.days

        # Return the calculated age
        return years, months, days

    except ValueError as fve:
        # Handle invalid date values
        raise ValueError("Invalid birth date. Please check the inputs for year, month, and day.") from fve

    except Exception as fe:
        # Handle any other unexpected errors
        raise RuntimeError("An unexpected error occurred while calculating the age.") from fe


# Example usage:
try:
    year = int(input("Please enter a year (Jalali): "))
    month = int(input("Please enter a month (Jalali): "))
    day = int(input("Please enter a day (Jalali): "))

    age = age_calculator(year, month, day)
    print(f"Age: {age[0]} years, {age[1]} months, {age[2]} days")

except ValueError as ve:
    print(f"Error: {ve}")

except Exception as e:
    print(f"Error: {e}")
