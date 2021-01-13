def hellofunction():
  #print("Keep it logically awesome.")
  """
  f = open("quotes.txt", "a")
  f.write("\nFirst Line\n")
  f.write("Second Line")

  f = open("quotes.txt", "r")
  quotes = f.readlines()
  f.close()
 

  print(quotes[13], end='')
  print(quotes[0], end='')
  print(quotes[19], end='')
  print(quotes[20])
  """
  with open("quotes.txt", "r") as f:
    lines = f.readlines()                     #open txt and close
  with open("quotes.txt", "w") as f:
    for line in lines:
      if line.strip("\n") != "First Line":
        f.write(line)
  with open("quotes.txt", "r") as f:
    lines = f.readlines() 
  with open("quotes.txt", "w") as f:
    for line in lines:
      if line.strip("\n") != "Second Line":
        f.write(line)
  """with open("quotes.txt", "r") as f:
    quotes = f.readlines()   

  print(quotes[13], end='')
  print(quotes[0], end='')
  print(quotes[19], end='')
  print(quotes[20])"""




if __name__== "__main__":
  hellofunction()
