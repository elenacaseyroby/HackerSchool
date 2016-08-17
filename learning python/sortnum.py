def sortnumbers(num_list):

    class sorted_numbers:
      def __init__(self, low=None, average=None, high=None):
          self.low = low
          self.average = average
          self.high = high

      def __getitem__ (self, low, average, high):
          return self.index
          return self.low
          return self.average 
          return self.high 
    error_message=None
    for num in num_list:
      if type(num) != int:
        error_message = "Error: Bad parameters for sortnumbers(num_list). Must enter exactly one list that contains only integer values."
    if not error_message:
      sortednum = sorted_numbers  
      total = 0;
      i = 0
      sortednum.low = 100^(10000000000000000)
      sortednum.high = -100^(10000000000000000)
      for num in num_list:
        total = total + num
        if num < sortednum.low:
          sortednum.low = num
        if num > sortednum.high:
          sortednum.high = num
          i = i+1;
      if i>0:
        sortednum.average = total/i
      else:
        sortednum.average = total

      return sortednum
    else:
      return error_message

num_list = [10, 30, "mewo"]

sorted_nums = sortnumbers(num_list)

print sorted_nums.low
print sorted_nums.high
print sorted_nums.average
