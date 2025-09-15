def sort(width, height, length, mass):
    volume = width * height * length
    bulky = True if (volume >= 1000000 or width >= 150 or height >= 150 or length >= 150) else False
    heavy = True if mass >= 20 else False  
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
if __name__ == "__main__":
    print(sort(100, 100, 100, 10)) 
    print(sort(200, 50, 50, 10))     
    print(sort(100, 100, 100, 25))   
    print(sort(200, 200, 200, 25))  
