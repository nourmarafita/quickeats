FOR (INT i = 1; i <= 5; i++)
  FOR (INT j = 1; j <= i; j++)
    print(" ")
  END FOR  
  FOR (INT j = 5; j >= i; j--)
    print("* ")
  END FOR
  print("\n")
END FOR