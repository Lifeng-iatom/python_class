#!/usr/bin/env python3.11
import flight

SAMPLE = [
      "12:00 AF6123 PARIS-ORLY",
      "12:00 SN3668 BRUSSELS",
      "12:10 TK0804 ISTANBUL",
      "12:20 AF7523 PARIS-CDG",
      "12:40 EZY438 LYON",
      "12:40 TAP491 LISBON",
      "12:50 EW7433 HAMBURG",
]

def main():

      allflights = SAMPLE

      while True:
            # Print menu        
            print("\t\t\t ------- MENU -------");
            print("\t\t\t Display flights    0");
            print("\t\t\t Find flights       1");
            print("\t\t\t Enter a New Flight 2");
            print("\t\t\t Delete a Flight    3");
            print("\t\t\t Quit               q");
            print("\t\t\t --------------------");

            choice = input("\t\t\t Your choice? ")
            if choice == "0":
                  flight.display(allflights)
            if choice == "1":
                  flight.find(allflights)
            elif choice == "2":
                  flight.add(allflights)
            elif choice == "3":
                  flight.delete(allflights)
            elif choice.lower() == "q":
                  break

main()
