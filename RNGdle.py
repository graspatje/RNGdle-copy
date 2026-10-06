# this is the part that makes the numbers
import random
import time
numberone = (random.randint( 0, 100000))
numbertwo = (random.randint( 0, 100000))
numberthree = (random.randint( 0, 100000))
numberfour = (random.randint( 0, 100000))
numberfive = (random.randint( 0, 100000))
numbersix = (random.randint( 0, 100000))

number = numberone + numbertwo + numberthree + numberfour + numberfive + numbersix

ep = 0


# this prints them out
print(numberone)
time.sleep(1.5)

print(numbertwo)
time.sleep(1.5)

print(numberthree)
time.sleep(1.5)

print(numberfour)
time.sleep(1.5)

print(numberfive)
time.sleep(1.5)

print(numbersix)
time.sleep(1)
print("Add it all up and ya get:")
time.sleep(3)
print(" ")
print(number)
print(" ")
print("Total EP:", ep)

# here's all the badges, you can add more if u want js copy the style

if number > 999990:
    print("5M EP+ NUMBER ABOVE 999.99K")
    ep += 5000000

elif number > 999000:
    print ("1M EP+ Number above 999K")
    ep += 1000000
elif number > 900000:
    print ("750K EP+ Number above 900K")
    ep += 750000
elif number > 800000:
    print("500K EP+ Number above 800K")
    ep += 500000
elif number > 700000:
    print("100K EP+ Number above 700K")
    ep += 100000
elif number > 600000:
    print("50K EP+ Number above 600K")
    ep += 50000
elif number > 500000:
    print("10K EP+ Number above 500K")
    ep += 10000
elif number > 400000:
    print("5K EP+ Number above 400k")
    ep += 5000
elif number > 300000:
    print("3K EP+ Number above 300k")
    ep += 3000
elif number > 200000:
    print("2K EP+ Number above 200k")
    ep += 2000
elif number > 100000:
    print("1K EP+ Number above 100k")
    ep += 1000
elif number < 10:
    print("5M EP+ SINGLE DIGIT NUMBER")
    ep += 5000000

elif number < 100:
    print("2.5M EP+ DOUBLE DIGIT NUMBER")
    ep += 2500000

elif number < 1000:
    print("1M EP+ Number under 1K")
    ep += 1000000

elif number < 10000:
    print("100K EP+ Number under 10K")
    ep += 100000

if "420" in str(number):
    print("42K EP+ Contains 420 (nice)")
    ep += 420000
if "69" in str(number):
    print("6.9K EP+ Contains 69 (nice)")
    ep += 6900
if "67" in str(number):
    print("6.7K EP+ Contains 67 hahahahahahahahahaha")
    ep += 6700
if "8008" in str(number):
    print("808K EP+ Contains BOOB (very nice)")
    ep += 808000
if "123456" in str(number):
    print("10M EP+ 123456 PERFECT COUNT")
    ep += 10000000
if "654321" in str(number):
    print("10M EP+ PERFECT COUNT BACKWARDS")
    ep += 10000000