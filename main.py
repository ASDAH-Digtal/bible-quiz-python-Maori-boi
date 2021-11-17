# Amount of points earned from correct answers
score = 0

for i in range(1):

  """ 
  Print statements used to print out a barrier to seperate each sentence
  As well as print statements which introduce the user to the Bible quiz
  """
  print("====================================================================")
  print("Welcome to Micah's bible quiz")
  print("====================================================================")
  print("You will be scored out of ten points.")
  print("====================================================================")
  print("If you score 0-3 points you need to Read your Bible!")
  print("====================================================================")
  print("If you score 4-7 points, there's room for improvement.")
  print("====================================================================")
  print("If you score 8-10 points, your pretty damn Good then.")
  print("====================================================================")
  break

# While true statement
while True:

  """
   Variable names use the Snake case technique
   input for question one
  """

  question_one = input("Where in the Bible does the 'Beast' come out of the sea?\n (a) Colossians\n (b) Hebrews\n (c) John\n (d) Revelation\n>>")
  
  # Available answers given both correct and incorrect answers 
  correct_q1 = ["D","d","(d)","Revelation", "revelation"]
  incorrect_q1 = ["A","a","(a)","Colossians","colossians","B","b","(b)","Hebrews","hebrews","C","c","(c)","John","john"]

  # if statement being used to check if given input is correct
  if question_one.lower() in correct_q1:
    print("====================================================================")
    print("Great Job, you got the answer right.")
    score += 1
    print("You now have: {} point".format(score))
    break

  # else/if statement being used to check if given input is incorrect
  elif question_one.lower() in incorrect_q1:
    print("Not the answer i'm looking for. Nice try.")
    score += 0
    print("You now have: {} point".format(score))
    break

  # else statement being used to tell user that the input answer must be one of the given answers above.
  else:
    print("You did not choose one of the options")
print("====================================================================")

# While true statement
while True:

  # input for question two
  question_two = input("How many books are in the New Testament?\n (a) 27\n (b) 33\n (c) 39\n (d) 28\n>>")

  # Available answers given both correct and incorrect answers
  correct_q2 = ["A","a","(a)","27"]
  incorrect_q2 = ["B","b","(b)","33","C","c","(c)","39","D","d","(d)","28"]

  # if statement being used to check if given input is correct
  if question_two.lower() in correct_q2:
    print("====================================================================")
    print("Great Job, you got the answer right.")
    score += 1
    print("You now have: {} points".format(score))
    break

  # else/if statement being used to check if given input is incorrect
  elif question_two.lower() in incorrect_q2:
    print("Not the answer i'm looking for. Nice try.")
    score += 0
    print("You now have: {} points".format(score))
    break

  # else statement being used to tell user that the input answer must be one of the given answers above.
  else:
    print("You did not choose one of the options")
print("====================================================================")

# While true statement
while True:

  # input for question three
  question_three = input("How many books are in the Bible?\n (a) 27\n (b) 66\n (c) 34\n (d) 53\n>>")

  # Available answers given both correct and incorrect answers
  correct_q3 = ["B","b","(b)","66"]
  incorrect_q3 = ["A","a","(a)","27","C","c","(c)","34","D","d","(d)","53"]

  # if statement being used to check if given input is correct
  if question_three.lower() in correct_q3:
    print("====================================================================")
    print("Great Job, you got the answer right.")
    score += 1
    print("You now have: {} points".format(score))
    break

  # else/if statement being used to check if given input is incorrect
  elif question_three.lower() in incorrect_q3:
    print("Not the answer i'm looking for. Nice try.")
    score += 0
    print("You now have: {} points".format(score))
    break

  # else statement being used to tell user that the input answer must be one of the given answers above.
  else:
    print("You did not choose one of the options")
print("====================================================================")

# While true statement
while True:

  # input for question four
  question_four = input("Where is Jesus place of Birth?\n (a) Jerusalem\n (b) Babylon\n (c) Bethlehem\n (d) Nazareth\n>>")

  # Available answers given both correct and incorrect answers
  correct_q4 = ["C","c","(c)","Bethlehem","bethlehem"]
  incorrect_q4 = ["A","a","(a)","Jerusalem","jerusalem","B","b","(b)","Babylon","babylon","D","d","(d)","Nazareth","nazareth"]

  # if statement being used to check if given input is correct
  if question_four.lower() in correct_q4:
    print("====================================================================")
    print("Great Job, you got the answer right.")
    score += 1
    print("You now have: {} points".format(score))
    break

  # else/if statement being used to check if given input is incorrect
  elif question_four.lower() in incorrect_q4:
    print("Not the answer i'm looking for. Nice try.")
    score += 0
    print("You now have: {} points".format(score))
    break

  # else statement being used to tell user that the input answer must be one of the given answers above.
  else:
    print("You did not choose one of the options")
print("====================================================================")

# While true statement
while True:

  # input for question five
  question_five = input("How many disciples did Jesus have?\n (a) 13\n (b) 10\n (c) 8\n (d) 12\n>>")

  # Available answers given both correct and incorrect answers
  correct_q5 = ["D","d","(d)","12"]
  incorrect_q5 = ["A","a","(a)","13","B","b","(b)","10","C","c","(c)","8"]

  # if statement being used to check if given input is correct
  if question_five.lower() in correct_q5:
    print("====================================================================")
    print("Great Job, you got the answer right.")
    score += 1
    print("You now have: {} points".format(score))
    break

  # else/if statement being used to check if given input is incorrect
  elif question_five.lower() in incorrect_q5:
    print("Not the answer i'm looking for. Nice try.")
    score += 0
    print("You now have: {} points".format(score))
    break

  # else statement being used to tell user that the input answer must be one of the given answers above.
  else:
    print("You did not choose one of the options")
print("====================================================================")

# While true statement
while True:

  # input for question six
  question_six = input("Who is the oldest person in the Bible?\n (a) Abraham\n (b) Enoch\n (c) Moses\n (d) Methuselah\n>>")

  # Available answers given both correct and incorrect answers
  correct_q6 = ["D","d","(d)","Methuselah","methuselah"]
  incorrect_q6 = ["A","a","(a)","Methuselah","methuselah","B","b","(b)","Enoch","enoch","C","c","(c)","Moses","moses"]

  # if statement being used to check if given input is correct
  if question_six.lower() in correct_q6:
    print("====================================================================")
    print("Great Job, you got the answer right.")
    score += 1
    print("You now have: {} points".format(score))
    break

  # else/if statement being used to check if given input is incorrect
  elif question_six.lower() in incorrect_q6:
    print("Not the answer i'm looking for. Nice try.")
    score += 0
    print("You now have: {} points".format(score))
    break

  # else statement being used to tell user that the input answer must be one of the given answers above.
  else:
    print("You did not choose one of the options")
print("====================================================================")

# While true statement
while True:

  # input for question seven
  question_seven = input("Who split the red sea?\n (a) Elisha\n (b) Abraham\n (c) Moses\n (d) Elijah\n>>")

  # Available answers given both correct and incorrect answers
  correct_q7 = ["C","c","(c)","Moses","moses"]
  incorrect_q7 = ["A","a","(a)","Elisha","elisha","B","b","(b)","Abraham","abraham","D","d","(d)","Elijah","elijah"]

  # if statement being used to check if given input is correct
  if question_seven.lower() in correct_q7:
    print("====================================================================")
    print("Great Job, you got the answer right.")
    score += 1
    print("You now have: {} points".format(score))
    break
 
  # else/if statement being used to check if given input is incorrect
  elif question_seven.lower() in incorrect_q7:
    print("Not the answer i'm looking for. Nice try.")
    score += 0
    print("You now have: {} points".format(score))
    break
 
  # else statement being used to tell user that the input answer must be one of the given answers above. 
  else:
    print("You did not choose one of the options")
print("====================================================================")

# While true statement
while True:

  # input for question eight
  question_eight = input("Who was the next King of Israel after King Saul?\n (a) King Solomon\n (b) King David\n (c) King Herod\n (d) King Nebuchadnezzar\n>>")

  # Available answers given both correct and incorrect answers
  correct_q8 = ["B","b","(b)","King David","king david","David","david"]
  incorrect_q8 = ["A","a","(a)","King Solomon","king solomon","Solomon","solomon","C","c","(c)","King Herod","king herod","Herod","herod","D","d","(d)","King Nebuchadnezzar","king nebuchadnezzar","Nebuchanezzar","nebuchanezzar"]


  # if statement being used to check if given input is correct
  if question_eight.lower() in correct_q8:
    print("====================================================================")
    print("Great Job, you got the answer right.")
    score += 1
    print("You now have: {} points".format(score))
    break
 
  # else/if statement being used to check if given input is incorrect 
  elif question_eight.lower() in incorrect_q8:
    print("Not the answer i'm looking for. Nice try.")
    score += 0
    print("You now have: {} points".format(score))
    break
 
  # else statement being used to tell user that the input answer must be one of the given answers above. 
  else:
    print("You did not choose one of the options")
print("====================================================================")

# While true statement
while True:

  # input for question nine
  question_nine = input("How many tribes are there in Israel?\n (a) 12\n (b) 4\n (c) 13\n (d) 7\n>>")

  # Available answers given both correct and incorrect answers
  correct_q9 = ["A","a","(a)","12"]
  incorrect_q9 = ["B","b","(b)","4","C","c","(c)","13","D","d","(d)","7"]

  
  # if statement being used to check if given input is correct  
  if question_nine.lower() in correct_q9:
    print("====================================================================")
    print("Great Job, you got the answer right.")
    score += 1
    print("You now have: {} points".format(score))
    break
 
  # else/if statement being used to check if given input is incorrect
  elif question_nine.lower() in incorrect_q9:
    print("Not the answer i'm looking for. Nice try.")
    score += 0
    print("You now have: {} points".format(score))
    break
 
  # else statement being used to tell user that the input answer must be one of the given answers above. 
  else:
    print("You did not choose one of the options")
print("====================================================================")

# While true statement
while True:

  # input for question ten
  question_ten = input("Which book in the Bible has the most comprehensive sweep of history?\n (a) Judges\n (b) 1 Kings\n (c) Daniel\n (d) Esther\n>>")

  # Available answers given both correct and incorrect answers
  correct_q10 = ["C","c","(c)","Daniel","daniel"]
  incorrect_q10 = ["A","a","(a)","Judges","judges","B","b","(b)","1 Kings","1 kings","D","d","(d)","Esther","esther"]

  # if statement being used to check if given input is correct
  if question_ten.lower() in correct_q10:
    print("====================================================================")
    print("Great Job, you got the answer right.")
    score += 1
    break
 
  # else/if statement being used to check if given input is incorrect 
  elif question_ten.lower() in incorrect_q10:
    print("Not the answer i'm looking for. Nice try.")
    score += 0
    break
 
  # else statement being used to tell user that the input answer must be one of the given answers above. 
  else:
    print("You did not choose one of the options")
print("====================================================================")


print("Your final score: {}/10".format(score))
print("====================================================================")
print("Thank you for taking part in Micah's Bible Quiz!")
print("====================================================================")