def compare_squares(x, y, language='uk'):
    abs_diff_squares = abs(x**2 - y**2)
    square_diff = (x - y)**2

    if abs_diff_squares > square_diff:
        result = f"|{x}^2 - {y}^2| = {abs_diff_squares} більше ніж ({x} - {y})^2 = {square_diff}"
    else:
        result = f"({x} - {y})^2 = {square_diff} більше ніж |{x}^2 - {y}^2| = {abs_diff_squares}"

    return translate_message(result, language)

def translate_message(message, language):
    translations = {
        'uk': {
            "Мова": "Мова",
            "Два числа": "Два числа",
        },
        'en': {
            "Мова": "Language",
            "Два числа": "Two numbers",
        }
    }
    
    return translations.get(language, translations['uk']).get(message, message)
