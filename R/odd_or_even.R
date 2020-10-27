# Write a program that asks the user to enter a number and prints whether the entered number is even or odd.

# install.packages('glue')
library(glue)

number <- readline(prompt = "Enter number: ")

odd_or_even <- "ODD"
if (number %% 2 == 0) {
  odd_or_even <- "EVEN"
}

cat(glue("\nThat number is {odd_or_even}\n"))
