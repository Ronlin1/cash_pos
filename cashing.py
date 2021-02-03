# Class definition of POS
class CashSystem:
    # Class Initializer or constructor
    def __init__(self, a=0, r=0, recieve=0, change=0, temp=0):
        # Displaying welcome screen
        print("\n\n***** WELCOME TO RON'S CAFETERIA!*****\n")
        # The class variables
        self.a = a
        self.r = r
        self.recieve = recieve
        self.change = change
        self.temp = temp

    # Defining The Main Function
    def foods(self):

        print("---> RON'S MENU <---")

        print("\n1.Ribs-->20,", "\n2.Pork chops-->30", "\n3.Fillet-->25", "\n4.Jerks-->45", "\n5.Cash Out", "\n6.EXIT")

        while True:
            choice = int(input("\nChoose:\n"))

            if choice == 1:
                no_of_dishes = int(input("Enter Quantity:\n"))
                self.r = self.r + 20 * no_of_dishes

            elif choice == 2:
                no_of_dishes = int(input("Enter Quantity:\n"))
                self.r = self.r + 30 * no_of_dishes

            elif choice == 3:
                no_of_dishes = int(input("Enter Quantity:\n"))
                self.r = self.r + 25 * no_of_dishes

            elif choice == 4:
                no_of_dishes = int(input("Enter Quantity:\n"))
                self.r = self.r + 45 * no_of_dishes

            elif choice == 5:
                print("Total is: ", self.r)
                if self.r > 0:
                    recieve = int(input("Input Cash Received:\n"))
                    print("Customer's Change is: ", recieve - self.r)
                    print("-----THANKS ESTEEMED CUSTOMER-----")
                    #quit()
                    #continue
            elif choice == 6:
                print("Ooops! What happened?? N'way return whenever you are ready!")
                #quit()
                break
            else:
                print("Invalid Option")


def main():
    call = CashSystem()
    while True:
        call.foods()


main()
